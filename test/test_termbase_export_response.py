# coding: utf-8

"""
    Lilt REST API

    Lilt REST API Support: https://lilt.atlassian.net/servicedesk/customer/portals    The Lilt REST API enables programmatic access to the full-range of Lilt backend services including:   * Training of and translating with interactive, adaptive machine translation   * Large-scale translation memory   * The Lexicon (a large-scale termbase)   * Programmatic control of the Lilt CAT environment   * Translation memory synchronization  Requests and responses are in JSON format. The REST API only responds to HTTPS / SSL requests.  The base url for this REST API is `https://api.lilt.com/`.  ## Authentication  Requests are authenticated via REST API key, which requires the Business plan.  Requests are authenticated using [HTTP Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication). Add your REST API key as both the `username` and `password`.  For development, you may also pass the REST API key via the `key` query parameter. This is less secure than HTTP Basic Auth, and is not recommended for production use.  ## Quotas  Our services have a general quota of 4000 requests per minute. Should you hit the maximum requests per minute, you will need to wait 60 seconds before you can send another request.   # noqa: E501

    The version of the OpenAPI document: v3.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import lilt
from lilt.models.termbase_export_response import TermbaseExportResponse  # noqa: E501
from lilt.rest import ApiException

class TestTermbaseExportResponse(unittest.TestCase):
    """TermbaseExportResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TermbaseExportResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = lilt.models.termbase_export_response.TermbaseExportResponse()  # noqa: E501
        if include_optional :
            return TermbaseExportResponse(
                id = 123, 
                is_processing = 1
            )
        else :
            return TermbaseExportResponse(
        )

    def testTermbaseExportResponse(self):
        """Test TermbaseExportResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
