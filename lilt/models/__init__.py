# coding: utf-8

# flake8: noqa
"""
    Lilt REST API

    Lilt REST API Support: https://lilt.atlassian.net/servicedesk/customer/portals    The Lilt REST API enables programmatic access to the full-range of Lilt backend services including:   * Training of and translating with interactive, adaptive machine translation   * Large-scale translation memory   * The Lexicon (a large-scale termbase)   * Programmatic control of the Lilt CAT environment   * Translation memory synchronization  Requests and responses are in JSON format. The REST API only responds to HTTPS / SSL requests.  The base url for this REST API is `https://api.lilt.com/`.  ## Authentication  Requests are authenticated via REST API key, which requires the Business plan.  Requests are authenticated using [HTTP Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication). Add your REST API key as both the `username` and `password`.  For development, you may also pass the REST API key via the `key` query parameter. This is less secure than HTTP Basic Auth, and is not recommended for production use.  ## Quotas  Our services have a general quota of 4000 requests per minute. Should you hit the maximum requests per minute, you will need to wait 60 seconds before you can send another request.   # noqa: E501

    The version of the OpenAPI document: v3.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from lilt.models.add_file_label_request import AddFileLabelRequest
from lilt.models.create_converter_config_parameters import CreateConverterConfigParameters
from lilt.models.delete_segment_from_memory_response import DeleteSegmentFromMemoryResponse
from lilt.models.document_with_segments import DocumentWithSegments
from lilt.models.document_without_segments import DocumentWithoutSegments
from lilt.models.document_without_segments_status import DocumentWithoutSegmentsStatus
from lilt.models.error import Error
from lilt.models.file_delete_response import FileDeleteResponse
from lilt.models.get_lilt_create_content_response import GetLiltCreateContentResponse
from lilt.models.inline_response200 import InlineResponse200
from lilt.models.job import Job
from lilt.models.job_create_parameters import JobCreateParameters
from lilt.models.job_delete_response import JobDeleteResponse
from lilt.models.job_leverage_stats import JobLeverageStats
from lilt.models.job_project import JobProject
from lilt.models.job_stats import JobStats
from lilt.models.job_update_parameters import JobUpdateParameters
from lilt.models.language_pair import LanguagePair
from lilt.models.languages_response import LanguagesResponse
from lilt.models.lilt_create_content import LiltCreateContent
from lilt.models.lilt_create_content_preferences import LiltCreateContentPreferences
from lilt.models.lilt_create_content_template_params import LiltCreateContentTemplateParams
from lilt.models.memory import Memory
from lilt.models.memory_create_parameters import MemoryCreateParameters
from lilt.models.memory_delete_response import MemoryDeleteResponse
from lilt.models.memory_import_response import MemoryImportResponse
from lilt.models.memory_update_parameters import MemoryUpdateParameters
from lilt.models.project import Project
from lilt.models.project_create_parameters import ProjectCreateParameters
from lilt.models.project_delete_response import ProjectDeleteResponse
from lilt.models.project_stats import ProjectStats
from lilt.models.sdlxliff_filter import SDLXLIFFFilter
from lilt.models.segment import Segment
from lilt.models.sign_lilt_create_terms_response import SignLiltCreateTermsResponse
from lilt.models.source_file import SourceFile
from lilt.models.termbase_export_response import TermbaseExportResponse
from lilt.models.translate_segment_body import TranslateSegmentBody
from lilt.models.translation import Translation
from lilt.models.translation_info import TranslationInfo
from lilt.models.translation_list import TranslationList
from lilt.models.translation_memory_entry import TranslationMemoryEntry
from lilt.models.workflow_stage_assignment import WorkflowStageAssignment
from lilt.models.workflow_stage_template import WorkflowStageTemplate
from lilt.models.workflow_template import WorkflowTemplate
