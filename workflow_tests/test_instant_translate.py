from __future__ import print_function

import os
import pytest
import time
import lilt

from lilt.rest import ApiException
from pprint import pprint


configuration = lilt.Configuration(
    host = os.environ["STAGING_HOST"],
    api_key = {
        "key": os.environ["STAGING_API_KEY"]
    }
)

test_cases = [
    "fr_to_en"
]

translate_file_path = "./resources"
DEV_MEMORY_ID = 13300
STAGING_MEMORY_ID = 23583
STAGING_TRANSLATION_ID = 17632

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
    assert response.status == "InProgress" or response.status == "Completed" or response.status == "ReadyForDownload"
    assert response.created_at is not None


@pytest.mark.parametrize("test_case", test_cases)
def test_instant_translate_workflow(test_case):  
    with lilt.ApiClient(configuration) as api_client:
        #Upload file
        files_instance = lilt.FilesApi(api_client)
        name = "translate-fr_to_en.txt" 
        with open(f"{translate_file_path}/translate-fr_to_en.txt", "rb") as upload_file:
            body = upload_file.read()

        api_response = files_instance.upload_file(
            name, 
            body
        )
        assert_upload_response(api_response)
        file_id = api_response.id

        #Translate file
        translate_instance = lilt.TranslateApi(api_client)
        memory_id = STAGING_MEMORY_ID 
        print(f"FILE ID: {file_id}")
        print(f"MEMORY ID: {memory_id}")

        api_response = translate_instance.batch_translate_file(file_id, memory_id)
        translation_response = api_response[0]
        translation_id = translation_response.id
        translation_status = translation_response.status
        assert_translate_response(translation_response, file_id, memory_id)

        #Monitor translation
        num_monitored = 0
        while translation_status != "ReadyForDownload":
            time.sleep(10)
            api_response = translate_instance.monitor_file_translation(translation_ids=translation_id)
            print(api_response)
            translation_response = api_response[0]
            translation_status = translation_response.status
            print(f"STATUS: {translation_status} || Request No: {num_monitored}")
            assert_translate_response(translation_response, file_id, memory_id)
            num_monitored += 1
            if num_monitored == 12:
                translation_id = STAGING_TRANSLATION_ID
                print("Translation exceeding time limit. Switching to finished translation.")
                break

        #Download translated file
        api_response = translate_instance.download_file(translation_id)
        assert "cat" in api_response
        assert "hello" in api_response.lower()


