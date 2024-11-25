from dotenv import load_dotenv

import os
from io import BytesIO
from zipfile import ZipFile

import pytest
import lilt

from tenacity import (
    retry,
    stop_after_delay,
    wait_exponential,
    retry_if_result,
)

load_dotenv()


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
def api(client):
    return lilt.JobsApi(client)


@pytest.fixture(scope="module")
def uploaded_file(client):
    api = lilt.FilesApi(client)
    name = "test_file.txt"
    body = b"hello world"
    response = api.upload_file(name, body)
    yield response
    api.delete_file(response.id)


@pytest.fixture(scope="module")
def memory(client):
    api = lilt.MemoriesApi(client)
    body = lilt.MemoryCreateParameters(
        name="test_memory",
        srclang="en",
        srclocale="US",
        trglang="de",
        trglocale="DE",
    )
    response = api.create_memory(body)
    yield response
    api.delete_memory(response.id)


@pytest.fixture(scope="module")
def job(api, memory, uploaded_file):
    lang = lilt.LanguagePair(trg_lang=memory.trglang, memory_id=memory.id)
    body = lilt.JobCreateParameters(
        name="test_job",
        src_lang="en",
        src_locale="US",
        language_pairs=[lang],
        file_ids=[uploaded_file.id],
    )
    response = api.create_job(body)
    yield response
    api.delete_job(response.id)


@retry(
    retry=retry_if_result(lambda jobs: len(jobs) == 0),
    stop=stop_after_delay(2 * 60),
    wait=wait_exponential(),
)
def wait_for_job_creation(api, job_id):
    api.deliver_job(job_id)
    return api.retrieve_all_jobs(is_delivered="true", is_archived="false")


def test_verified_translate_monitor_job_status(api, job):
    jobs = wait_for_job_creation(api, job.id)
    assert len(jobs) > 0


@retry(
    retry=retry_if_result(lambda is_processing: is_processing != 0),
    stop=stop_after_delay(2 * 60),
    wait=wait_exponential(),
)
def wait_for_job_export(api, job_id):
    job = api.get_job(job_id)
    return job.is_processing


def test_verified_translate_download_job(api, job):
    api.export_job(job.id, type="files")
    wait_for_job_export(api, job.id)
    response = api.download_job(job.id, _preload_content=False)
    zip_file = BytesIO(response.data)
    with ZipFile(zip_file) as zip_ref:
        contents = zip_ref.infolist()
        assert len(contents) == 2
        translated_file = contents[1]
        with zip_ref.open(translated_file) as tf:
            assert tf.read() == b"hello world"


def test_verified_translate_archive_job(api, job):
    api.archive_job(job.id)
    updated_job = api.get_job(job.id)
    assert updated_job.status == "archived"
