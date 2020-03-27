# coding: utf-8

"""
    Lilt REST API

    The Lilt REST API enables programmatic access to the full-range of Lilt backend services including:   * Training of and translating with interactive, adaptive machine translation   * Large-scale translation memory   * The Lexicon (a large-scale termbase)   * Programmatic control of the Lilt CAT environment   * Translation memory synchronization  Requests and responses are in JSON format. The REST API only responds to HTTPS / SSL requests. ## Authentication Requests are authenticated via REST API key, which requires the Business plan.  Requests are authenticated using [HTTP Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication). Add your REST API key as both the `username` and `password`.  For development, you may also pass the REST API key via the `key` query parameter. This is less secure than HTTP Basic Auth, and is not recommended for production use.   # noqa: E501

    The version of the OpenAPI document: v2.0
    Contact: support@lilt.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.document_pretranslating import DocumentPretranslating  # noqa: E501
from openapi_client.rest import ApiException

class TestDocumentPretranslating(unittest.TestCase):
    """DocumentPretranslating unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DocumentPretranslating
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.document_pretranslating.DocumentPretranslating()  # noqa: E501
        if include_optional :
            return DocumentPretranslating(
                id = 123.0, 
                import_in_progress = False, 
                import_succeeded = True, 
                import_error_message = '0', 
                is_processing = False, 
                is_pretranslating = True, 
                status = {"pretranslation":"running"}
            )
        else :
            return DocumentPretranslating(
        )

    def testDocumentPretranslating(self):
        """Test DocumentPretranslating"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
