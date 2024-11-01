from __future__ import print_function
from dotenv import load_dotenv

import os
import pytest
import time
import lilt

load_dotenv()

configuration = lilt.Configuration(
    host=os.environ["API_HOST"],
    api_key={
        "key": os.environ["API_KEY"]
    }
)

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
    "over500",
    #"non_string"
]

generate_content_sections_cases = [
    "none",
    "one",
    "multiple",
    #"non_list",
    #"non_string_elements"
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
        case "non_string":
            return 1


def get_section(section_case):
    match section_case:
        case "none":
            return []
        case "one":
            return ["Bees and me"]
        case "multiple":
            return ["Bees and me", "Honey for you", "Conclusion"]
        case "non_list":
            return 1
        case "non_string_elements":
            return [1, 2]


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
        case "non_string":
            return {
                "language": "en-US",
                "preferences": None,
                "template": "blog-post",
                "template_params": {
                    "content_length": 1000,
                    "language": "en-US",
                    "sections": ["Bees and me", "Honey for you", "Conclusion"],
                    "summary": "1"
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
        case "non_list":
            return {
                "language": "en-US",
                "preferences": None,
                "template": "blog-post",
                "template_params": {
                    "content_length": 1000,
                    "language": "en-US",
                    "sections": "1",
                    "summary": "a blog post about how important bees are to my honey farm"
                }
            }
        case "non_string_elements":
            return {
                "language": "en-US",
                "preferences": None,
                "template": "blog-post",
                "template_params": {
                    "content_length": 1000,
                    "language": "en-US",
                    "sections": "[1, 2]",
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


@pytest.mark.parametrize("sign_case", sign_cases)
def test_sign(sign_case):
    api_client = lilt.ApiClient(configuration)

    # Sign terms and conditions
    api_instance = lilt.CreateApi(api_client)
    sign = get_sign(sign_case)

    try:
        signed_agreement = lilt.CreateConverterConfigParameters(sign)
        api_response = api_instance.sign_lilt_create_terms(signed_agreement)
        assert api_response.signed_agreement == bool(sign)
    except ValueError as e:
        print("Exception when calling CreateApi->sign_lilt_create_terms: %s\n" % e)
        if sign_case != "none":
            raise e


@pytest.mark.parametrize("char_case", generate_content_char_cases)
def test_create_content_chars(char_case):
    api_client = lilt.ApiClient(configuration)

    # Sign agreement
    api_instance = lilt.CreateApi(api_client)
    signed_agreement = lilt.CreateConverterConfigParameters(True)
    api_response = api_instance.sign_lilt_create_terms(signed_agreement)
    assert api_response.signed_agreement

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

    api_instance.generate_lilt_create_content(request_body)
    time.sleep(5)
    api_response = api_instance.get_lilt_create_content()
    latest_content = api_response.contents[-1]
    assert_response(latest_content, expected_chars(char_case))


@pytest.mark.parametrize("section_case", generate_content_sections_cases)
def test_create_content_sections(section_case):
    api_client = lilt.ApiClient(configuration)

    # Sign agreement
    api_instance = lilt.CreateApi(api_client)
    signed_agreement = lilt.CreateConverterConfigParameters(True)
    api_response = api_instance.sign_lilt_create_terms(signed_agreement)
    assert api_response.signed_agreement

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

    api_instance.generate_lilt_create_content(request_body)
    time.sleep(5)
    api_response = api_instance.get_lilt_create_content()
    latest_content = api_response.contents[-1]
    assert_response(latest_content, expected_section(section_case))
