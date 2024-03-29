# coding: utf-8

"""
    Lilt REST API

    The Lilt REST API enables programmatic access to the full-range of Lilt backend services including:   * Training of and translating with interactive, adaptive machine translation   * Large-scale translation memory   * The Lexicon (a large-scale termbase)   * Programmatic control of the Lilt CAT environment   * Translation memory synchronization  Requests and responses are in JSON format. The REST API only responds to HTTPS / SSL requests.  ## Authentication  Requests are authenticated via REST API key, which requires the Business plan.  Requests are authenticated using [HTTP Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication). Add your REST API key as both the `username` and `password`.  For development, you may also pass the REST API key via the `key` query parameter. This is less secure than HTTP Basic Auth, and is not recommended for production use.  ## Quotas  Our services have a general quota of 4000 requests per minute. Should you hit the maximum requests per minute, you will need to wait 60 seconds before you can send another request.   # noqa: E501

    The version of the OpenAPI document: v2.0
    Contact: support@lilt.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import lilt
from lilt.api.documents_api import DocumentsApi  # noqa: E501
from lilt.rest import ApiException


class TestDocumentsApi(unittest.TestCase):
    """DocumentsApi unit test stubs"""

    def setUp(self):
        self.api = lilt.api.documents_api.DocumentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_assign_document(self):
        """Test case for assign_document

        Assign a Document  # noqa: E501
        """
        pass

    def test_create_document(self):
        """Test case for create_document

        Create a Document  # noqa: E501
        """
        pass

    def test_delete_document(self):
        """Test case for delete_document

        Delete a Document  # noqa: E501
        """
        pass

    def test_download_document(self):
        """Test case for download_document

        Download a Document  # noqa: E501
        """
        pass

    def test_get_document(self):
        """Test case for get_document

        Retrieve a Document  # noqa: E501
        """
        pass

    def test_mark_review_done(self):
        """Test case for mark_review_done

        Mark review done  # noqa: E501
        """
        pass

    def test_mark_translation_done(self):
        """Test case for mark_translation_done

        Mark translation done  # noqa: E501
        """
        pass

    def test_pretranslate_documents(self):
        """Test case for pretranslate_documents

        Pretranslate a Document  # noqa: E501
        """
        pass

    def test_unlock_documents(self):
        """Test case for unlock_documents

        Unlock documents  # noqa: E501
        """
        pass

    def test_upload_document(self):
        """Test case for upload_document

        Upload a File  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
