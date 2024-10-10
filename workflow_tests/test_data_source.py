from __future__ import print_function
from dotenv import load_dotenv

import os
import pytest
import time
import lilt

from lilt.rest import ApiException
from pprint import pprint

load_dotenv()


configuration = lilt.Configuration(
    host=os.environ["API_HOST"],
    api_key={
        "key": os.environ["API_KEY"]
    }
)

create_data_source_cases = [
    "none_src",
    "none_trg",
    "none_both",
    "english",
    "non_english",
    "source_is_target",
    "unsupported_languages"
]

tmx_file_cases = [
    "wrong_data",
    "normal"
]

translate_file_path = "./workflow_tests/resources"


def get_data_source_parameters(data_source_case):
    if data_source_case == "none_src":
        return {
            "name": "test-non-src",
            "srclang": None,
            "trglang": "en",
            "srclocale": "US",
            "trglocale": None
        }
    elif data_source_case == "none_trg":
        return {
            "name": "test-none-trg",
            "srclang": "en",
            "trglang": None,
            "srclocale": "US",
            "trglocale": None
        }
    elif data_source_case == "none_both":
        return {
            "name": "test-none-both",
            "srclang": None,
            "trglang": None,
            "srclocale": "US",
            "trglocale": None
        }
    elif data_source_case == "english":
        return {
            "name": "test-english",
            "srclang": "en",
            "trglang": "es",
            "srclocale": "US",
            "trglocale": None
        }
    elif data_source_case == "non_english":
        return {
            "name": "test-non-english",
            "srclang": "de",
            "trglang": "fr",
            "srclocale": "DE",
            "trglocale": "FR"
        }
    elif data_source_case == "source_is_target":
        return {
            "name": "test-source-is-target",
            "srclang": "fr",
            "trglang": "fr",
            "srclocale": "FR",
            "trglocale": "FR"
        }
    elif data_source_case == "unsupported_languages":
        return {
            "name": "test-unsupported-languages",
            "srclang": "ac",
            "trglang": "ad",
            "srclocale": None,
            "trglocale": None
        }
    elif data_source_case == "fr_to_en":
        return {
            "name": "test-fr-to-en",
            "srclang": "fr",
            "trglang": "en",
            "srclocale": "FR",
            "trglocale": "US"
        }


def get_tmx_settings(tmx_settings_case):
    if tmx_settings_case == "wrong_data":
        return {
            "name": "get_documents.json",
            "body": f"{translate_file_path}/get_documents.json"
        }
    elif tmx_settings_case == "normal":
        return {
            "name": "fr_to_en.tmx",
            "body": f"{translate_file_path}/test-fr_to_en.tmx"
        }


def get_expected_data_source(data_source_case):
    if data_source_case == "english":
        return {
            "is_processing": None,
            "name": "test-english",
            "resources": None,
            "srclang": "en",
            "srclocale": "US",
            "trglang": "es",
            "trglocale": None,
            "version": 0
        }
    elif data_source_case == "non_english":
        return {
            "is_processing": None,
            "name": "test-non-english",
            "resources": None,
            "srclang": "de",
            "srclocale": "DE",
            "trglang": "fr",
            "trglocale": "FR",
            "version": 0
        }
    elif data_source_case == "source_is_target":
        return {
            "is_processing": None,
            "name": "test-source-is-target",
            "resources": None,
            "srclang": "fr",
            "srclocale": "FR",
            "trglang": "fr",
            "trglocale": "FR",
            "version": 0
        }
    elif data_source_case == "fr_to_en":
        return {
            "is_processing": None,
            "name": "test-fr-to-en",
            "resources": None,
            "srclang": "fr",
            "srclocale": "FR",
            "trglang": "en",
            "trglocale": "US",
            "version": 0
        }


def get_expected_query():
    return {
        "metadata": {
            "resource_name": "fr_to_en.tmx",
            "user_email": ["apikeyuser", "@lilt.com"]
        },
        "score": 100,
        "source": "chatte",
        "target": "cat"
    }


def assert_data_source_response(data_source_object, expected):
    assert data_source_object.is_processing == expected["is_processing"]
    assert data_source_object.name == expected["name"]
    assert data_source_object.resources == expected["resources"]
    assert data_source_object.srclang == expected["srclang"]
    assert data_source_object.srclocale == expected["srclocale"]
    assert data_source_object.trglang == expected["trglang"]
    assert data_source_object.trglocale == expected["trglocale"]
    assert data_source_object.version == expected["version"]
    assert data_source_object.created_at is not None
    assert data_source_object.updated_at is not None
    assert data_source_object.id is not None


def assert_query_response(query_object, expected):
    metadata = query_object.metadata
    assert metadata["resource_name"] == expected["metadata"]["resource_name"]
    assert metadata["user_email"].startswith(expected["metadata"]["user_email"][0])
    assert metadata["user_email"].endswith(expected["metadata"]["user_email"][1])
    assert metadata["created_at"] is not None
    assert query_object.score == expected["score"]
    assert query_object.source == expected["source"]
    assert query_object.target == expected["target"]


@pytest.mark.parametrize("data_source_case", create_data_source_cases)
def test_create_data_source_workflow(data_source_case):
    api_client = lilt.ApiClient(configuration)

    # Create data source
    api_instance = lilt.MemoriesApi(api_client)

    try:
        data_source_parameters = get_data_source_parameters(data_source_case)
        body = lilt.MemoryCreateParameters(
            name=data_source_parameters["name"],
            srclang=data_source_parameters["srclang"],
            trglang=data_source_parameters["trglang"],
            srclocale=data_source_parameters["srclocale"],
            trglocale=data_source_parameters["trglocale"]
        )
    except ValueError as e:
        print("Value error when calling MemoriesApi->create_memory: %s\n" % e)
        if data_source_case in ["none_src", "none_trg", "none_both"]:
            return
        else:
            raise e

    try:
        api_response = api_instance.create_memory(body)
        pprint(api_response)
        assert_data_source_response(api_response, get_expected_data_source(data_source_case))
    except ApiException as e:
        print("Exception when calling MemoriesApi->create_memory: %s\n" % e)
        if data_source_case == "unsupported_languages":
            assert e.status == 400
        else:
            raise e


@pytest.mark.parametrize("tmx_file_case", tmx_file_cases)
def test_upload_tmx_file_workflow(tmx_file_case):
    api_client = lilt.ApiClient(configuration)

    # Create data source
    api_instance = lilt.MemoriesApi(api_client)
    data_source_parameters = get_data_source_parameters("fr_to_en")
    body = lilt.MemoryCreateParameters(
        name=data_source_parameters["name"],
        srclang=data_source_parameters["srclang"],
        trglang=data_source_parameters["trglang"],
        srclocale=data_source_parameters["srclocale"],
        trglocale=data_source_parameters["trglocale"]
    )
    api_response = api_instance.create_memory(body)
    assert_data_source_response(api_response, get_expected_data_source("fr_to_en"))
    memory_id = api_response.id
    print(f"Memory ID: {memory_id}")

    # Upload file
    print(os.getcwd())
    tmx_settings = get_tmx_settings(tmx_file_case)
    upload_file = open(tmx_settings["body"], "rb")
    body = upload_file.read()
    print("-----FILE START-----")
    print(body)
    print("-----FILE END-----")
    api_response = api_instance.import_memory_file(
        memory_id=memory_id,
        name=tmx_settings["name"],
        body=body
    )
    pprint(api_response)
    assert api_response.id == memory_id
    assert api_response.is_processing == 1
    time.sleep(10)

    # Query memory
    query = "chatte"
    api_response = api_instance.query_memory(memory_id, query)
    if tmx_file_case == "wrong_data":
        assert api_response == []
    else:
        assert len(api_response) > 0
        assert_query_response(api_response[0], get_expected_query())
