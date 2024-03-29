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

import lilt
from lilt.models.job import Job  # noqa: E501
from lilt.rest import ApiException

class TestJob(unittest.TestCase):
    """Job unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Job
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = lilt.models.job.Job()  # noqa: E501
        if include_optional :
            return Job(
                name = 'My New Job', 
                creation_status = 'COMPLETE', 
                delivered_at = 56, 
                status = 'active', 
                due = '2021-06-03T13:43:00.000Z', 
                id = 241, 
                is_processing = 0, 
                stats = lilt.models.job_stats.JobStats(
                    exact_words = 0, 
                    fuzzy_words = 0, 
                    new_words = 0, 
                    num_delivered_projects = 0, 
                    num_language_pairs = 0, 
                    num_projects = 0, 
                    percent_reviewed = 0, 
                    percent_translated = 0, 
                    projects = [
                        lilt.models.job_project.JobProject(
                            id = 56, 
                            src_lang = 'en', 
                            src_locale = 'US', 
                            trg_lang = 'fr', 
                            trg_locale = 'CA', 
                            name = 'My new project', 
                            due = '2021-10-03T13:43:00.000Z', 
                            is_complete = False, 
                            is_archived = False, 
                            state = 'inProgress', 
                            num_source_tokens = 2134, 
                            created_at = '2021-04-01T13:43:00.000Z', 
                            updated_at = '2021-06-03T13:43:00.000Z', 
                            is_deleted = False, 
                            memory_id = 2134, )
                        ], 
                    source_words = 0, 
                    unique_language_pairs = 1, 
                    unique_linguists = 1, )
            )
        else :
            return Job(
        )

    def testJob(self):
        """Test Job"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
