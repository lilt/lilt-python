from __future__ import print_function
from dotenv import load_dotenv

import os
import pytest
import time
import lilt

load_dotenv()


sign_cases = [
    "none",
    "signed",
    "unsigned",
    "non_boolean_1",
    "non_boolean_0"
]

generate_content_char_cases = [
    "none",
    "normal",
    "over500"
]

generate_content_sections_cases = [
    "none",
    "one",
    "multiple"
]


def get_sign(sign_case):
    match sign_case:
        case "none":
            return None
        case "unsigned":
            return False
        case "signed":
            return True
        case "non_boolean_1":
            return 1
        case "non_boolean_0":
            return 0


def get_summary(char_case):
    match char_case:
        case "none":
            return ""
        case "normal":
            return "a blog post about how important bees are to my honey farm"
        case "over500":
            return "a blog post about how important bees are to my honey farm" * 10


def get_section(section_case):
    match section_case:
        case "none":
            return []
        case "one":
            return ["Bees and me"]
        case "multiple":
            return ["Bees and me", "Honey for you", "Conclusion"]


def expected_chars(char_case):
    match char_case:
        case "none":
            return {
                "language": "en-US",
                "preferences": None,
                "template": "blog-post",
                "template_params": {
                    "content_length": 1000,
                    "language": "en-US",
                    "sections": ["Bees and me", "Honey for you", "Conclusion"],
                    "summary": ""
                }
            }
        case "normal":
            return {
                "language": "en-US",
                "preferences": None,
                "template": "blog-post",
                "template_params": {
                    "content_length": 1000,
                    "language": "en-US",
                    "sections": ["Bees and me", "Honey for you", "Conclusion"],
                    "summary": "a blog post about how important bees are to my honey farm"
                }
            }
        case "over500":
            return {
                "language": "en-US",
                "preferences": None,
                "template": "blog-post",
                "template_params": {
                    "content_length": 1000,
                    "language": "en-US",
                    "sections": ["Bees and me", "Honey for you", "Conclusion"],
                    "summary": 'a blog post about how important bees are to '
                                'my honey farma blog post about how important '
                                'bees are to my honey farma blog post about '
                                'how important bees are to my honey farma blog '
                                'post about how important bees are to my honey '
                                'farma blog post about how important bees are '
                                'to my honey farma blog post about how '
                                'important bees are to my honey farma blog '
                                'post about how important bees are to my honey '
                                'farma blog post about how important bees are '
                                'to my honey farma blog post about how '
                                'important bees are to my honey farma blog '
                                'post about how important bees are to my honey '
                                'farm'
                }
            }


def expected_section(section_case):
    match section_case:
        case "none":
            return {
                "language": "en-US",
                "preferences": None,
                "template": "blog-post",
                "template_params": {
                    "content_length": 1000,
                    "language": "en-US",
                    "sections": [],
                    "summary": "a blog post about how important bees are to my honey farm"
                }
            }
        case "one":
            return {
                "language": "en-US",
                "preferences": None,
                "template": "blog-post",
                "template_params": {
                    "content_length": 1000,
                    "language": "en-US",
                    "sections": ["Bees and me"],
                    "summary": "a blog post about how important bees are to my honey farm"
                }
            }
        case "multiple":
            return {
                "language": "en-US",
                "preferences": None,
                "template": "blog-post",
                "template_params": {
                    "content_length": 1000,
                    "language": "en-US",
                    "sections": ["Bees and me", "Honey for you", "Conclusion"],
                    "summary": "a blog post about how important bees are to my honey farm"
                }
            }


def assert_response(create_content_obj, expected):
    assert create_content_obj.language == expected["language"]
    assert create_content_obj.preferences == expected["preferences"]
    assert create_content_obj.template == expected["template"]
    template_params = create_content_obj.template_params
    assert template_params.content_length == expected["template_params"]["content_length"]
    assert template_params.language == expected["template_params"]["language"]
    assert template_params.sections == expected["template_params"]["sections"]
    assert template_params.summary == expected["template_params"]["summary"]


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
def create_api(client):
    return lilt.CreateApi(client)


@pytest.fixture(scope="function")
def sign(create_api):
    signed_agreement = lilt.CreateConverterConfigParameters(True)
    return create_api.sign_lilt_create_terms(signed_agreement)


@pytest.mark.parametrize("sign_case", sign_cases)
def test_sign(sign_case, create_api):
    sign = get_sign(sign_case)

    try:
        signed_agreement = lilt.CreateConverterConfigParameters(sign)
        api_response = create_api.sign_lilt_create_terms(signed_agreement)
        assert api_response.signed_agreement == bool(sign)
    except ValueError as e:
        print("Exception when calling CreateApi->sign_lilt_create_terms: %s\n" % e)
        if sign_case != "none":
            raise e


@pytest.mark.parametrize("char_case", generate_content_char_cases)
def test_create_content_chars(create_api, sign, char_case):
    assert sign.signed_agreement

    # Generate content
    template_params = lilt.LiltCreateContentTemplateParams(
        content_length=1000,
        language="en-US",
        summary=get_summary(char_case),
        sections=["Bees and me", "Honey for you", "Conclusion"]
    )
    preferences = lilt.LiltCreateContentPreferences(
        tone="formal"
    )
    request_body = lilt.LiltCreateContent(
        language="en-US",
        template="blog-post",
        template_params=template_params,
        preferences=preferences
    )

    create_api.generate_lilt_create_content(request_body)
    time.sleep(5)
    api_response = create_api.get_lilt_create_content()
    latest_content = api_response.contents[-1]
    assert_response(latest_content, expected_chars(char_case))

    create_api.delete_lilt_create_content(latest_content.id)


@pytest.mark.parametrize("section_case", generate_content_sections_cases)
def test_create_content_sections(create_api, sign, section_case):
    assert sign.signed_agreement

    # Generate content
    template_params = lilt.LiltCreateContentTemplateParams(
        content_length=1000,
        language="en-US",
        summary="a blog post about how important bees are to my honey farm",
        sections=get_section(section_case)
    )
    preferences = lilt.LiltCreateContentPreferences(
        tone="formal"
    )
    request_body = lilt.LiltCreateContent(
        language="en-US",
        template="blog-post",
        template_params=template_params,
        preferences=preferences
    )

    create_api.generate_lilt_create_content(request_body)
    time.sleep(5)
    api_response = create_api.get_lilt_create_content()
    latest_content = api_response.contents[-1]
    assert_response(latest_content, expected_section(section_case))

    create_api.delete_lilt_create_content(latest_content.id)
