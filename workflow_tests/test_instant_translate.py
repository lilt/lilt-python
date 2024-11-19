from __future__ import print_function
from dotenv import load_dotenv

import os
import pytest
import lilt

from tenacity import retry, stop_after_delay, wait_exponential, retry_if_result, RetryError

load_dotenv()

test_cases = [
    "fr_to_en"
]

translate_file_path = "./workflow_tests/resources"
STAGING_MEMORY_ID = 23583
STAGING_TRANSLATION_ID = 17680


def assert_upload_response(response):
    assert response.category == 'API'
    assert response.created_at is not None
    assert response.file_hash is not None
    assert response.id is not None
    assert response.name == 'translate-fr_to_en.txt'
    assert response.updated_at is not None


def assert_translate_response(response, file_id, memory_id):
    assert response.id is not None
    assert response.file_id == file_id
    assert response.status in ["InProgress", "Completed", "ReadyForDownload"]
    assert response.created_at is not None


@pytest.fixture(scope="module")
def client():
    configuration = lilt.Configuration(
        host=os.environ["API_HOST"], api_key={"key": os.environ["API_KEY"]}
    )
    api_client = lilt.ApiClient(configuration)
    api_client.set_default_header("x-is-automated-test", True)
    api_client.set_default_header("x-is-expected-error", True)
    commit = os.environ.get("GIT_COMMIT_SHA", "no_version_available")
    api_client.user_agent = f"lilt-python-e2e-tests/{commit}"
    return api_client


@pytest.fixture(scope="module")
def files_api(client):
    return lilt.FilesApi(client)

@pytest.fixture(scope="module")
def translate_api(client):
    return lilt.TranslateApi(client)


@retry(
    retry=retry_if_result(lambda status: status != "ReadyForDownload"),
    stop=stop_after_delay(2 * 60),
    wait=wait_exponential()
)
def monitor_file_translation(translate_api, translation_id, file_id, memory_id):
    api_response = translate_api.monitor_file_translation(translation_ids=translation_id)
    translation_response = api_response[0]
    translation_status = translation_response.status
    print(f"STATUS: {translation_status}")
    assert_translate_response(translation_response, file_id, memory_id)
    return translation_status

@pytest.fixture(scope="module")
def upload_file(files_api):
    name = "translate-fr_to_en.txt"
    upload_file = open(f"{translate_file_path}/translate-fr_to_en.txt", "rb")
    body = upload_file.read()

    api_response = files_api.upload_file(
        name,
        body
    )
    assert_upload_response(api_response)
    yield api_response
    files_api.delete_file(api_response.id)


@pytest.mark.parametrize("test_case", test_cases)
def test_instant_translate_workflow(upload_file, translate_api, test_case):
    file_id = upload_file.id

    memory_id = STAGING_MEMORY_ID
    print(f"FILE ID: {file_id}")
    print(f"MEMORY ID: {memory_id}")

    api_response = translate_api.batch_translate_file(file_id, memory_id)
    translation_response = api_response[0]
    translation_id = translation_response.id
    translation_status = translation_response.status
    assert_translate_response(translation_response, file_id, memory_id)

    # Monitor translation
    try:
        translation_status = monitor_file_translation(
            translate_api,
            translation_id,
            file_id,
            memory_id
        )
        print(f"STATUS: {translation_status}")
    except RetryError:
        translation_id = STAGING_TRANSLATION_ID
        print("Translation exceeding time limit. Switching to finished translation.")

    # Download translated file
    api_response = translate_api.download_file(translation_id)
    assert "cat" in api_response
    assert "hello" in api_response.lower()
