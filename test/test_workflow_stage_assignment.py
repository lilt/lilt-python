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
import datetime

import lilt
from lilt.models.workflow_stage_assignment import WorkflowStageAssignment  # noqa: E501
from lilt.rest import ApiException

class TestWorkflowStageAssignment(unittest.TestCase):
    """WorkflowStageAssignment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test WorkflowStageAssignment
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = lilt.models.workflow_stage_assignment.WorkflowStageAssignment()  # noqa: E501
        if include_optional :
            return WorkflowStageAssignment(
                workflow_stage_template_id = 12345, 
                user_id = 123, 
                email = 'username@domain.com'
            )
        else :
            return WorkflowStageAssignment(
                workflow_stage_template_id = 12345,
        )

    def testWorkflowStageAssignment(self):
        """Test WorkflowStageAssignment"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()