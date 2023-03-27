# coding: utf-8

# flake8: noqa

"""
    Lilt REST API

    The Lilt REST API enables programmatic access to the full-range of Lilt backend services including:   * Training of and translating with interactive, adaptive machine translation   * Large-scale translation memory   * The Lexicon (a large-scale termbase)   * Programmatic control of the Lilt CAT environment   * Translation memory synchronization  Requests and responses are in JSON format. The REST API only responds to HTTPS / SSL requests.  ## Authentication  Requests are authenticated via REST API key, which requires the Business plan.  Requests are authenticated using [HTTP Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication). Add your REST API key as both the `username` and `password`.  For development, you may also pass the REST API key via the `key` query parameter. This is less secure than HTTP Basic Auth, and is not recommended for production use.  ## Quotas  Our services have a general quota of 4000 requests per minute. Should you hit the maximum requests per minute, you will need to wait 60 seconds before you can send another request.   # noqa: E501

    The version of the OpenAPI document: v2.0
    Contact: support@lilt.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from lilt.api.comments_api import CommentsApi
from lilt.api.connectors_api import ConnectorsApi
from lilt.api.converter_config_api import ConverterConfigApi
from lilt.api.documents_api import DocumentsApi
from lilt.api.files_api import FilesApi
from lilt.api.jobs_api import JobsApi
from lilt.api.languages_api import LanguagesApi
from lilt.api.lexicon_api import LexiconApi
from lilt.api.memories_api import MemoriesApi
from lilt.api.projects_api import ProjectsApi
from lilt.api.qa_api import QAApi
from lilt.api.root_api import RootApi
from lilt.api.segments_api import SegmentsApi
from lilt.api.settings_api import SettingsApi
from lilt.api.translate_api import TranslateApi
from lilt.api.workflows_api import WorkflowsApi

# import ApiClient
from lilt.api_client import ApiClient
from lilt.configuration import Configuration
from lilt.exceptions import OpenApiException
from lilt.exceptions import ApiTypeError
from lilt.exceptions import ApiValueError
from lilt.exceptions import ApiKeyError
from lilt.exceptions import ApiException
# import models into sdk package
from lilt.models.add_file_label_request import AddFileLabelRequest
from lilt.models.annotation import Annotation
from lilt.models.api_root import ApiRoot
from lilt.models.assignment_details import AssignmentDetails
from lilt.models.assignment_error import AssignmentError
from lilt.models.auto_assignment_parameters import AutoAssignmentParameters
from lilt.models.auto_assignment_response import AutoAssignmentResponse
from lilt.models.bad_request import BadRequest
from lilt.models.comment import Comment
from lilt.models.comment_body import CommentBody
from lilt.models.comment_delete_response import CommentDeleteResponse
from lilt.models.connector import Connector
from lilt.models.connector_arguments import ConnectorArguments
from lilt.models.connector_delete_response import ConnectorDeleteResponse
from lilt.models.connector_job import ConnectorJob
from lilt.models.converter_config_update_response import ConverterConfigUpdateResponse
from lilt.models.create_converter_config_parameters import CreateConverterConfigParameters
from lilt.models.document_assignment_parameters import DocumentAssignmentParameters
from lilt.models.document_assignment_response import DocumentAssignmentResponse
from lilt.models.document_comments import DocumentComments
from lilt.models.document_delete_response import DocumentDeleteResponse
from lilt.models.document_done_update_parameters import DocumentDoneUpdateParameters
from lilt.models.document_done_update_parameters1 import DocumentDoneUpdateParameters1
from lilt.models.document_done_update_parameters2 import DocumentDoneUpdateParameters2
from lilt.models.document_parameters import DocumentParameters
from lilt.models.document_pretranslate_parameters import DocumentPretranslateParameters
from lilt.models.document_pretranslate_response import DocumentPretranslateResponse
from lilt.models.document_pretranslating import DocumentPretranslating
from lilt.models.document_pretranslating_status import DocumentPretranslatingStatus
from lilt.models.document_quote import DocumentQuote
from lilt.models.document_with_segments import DocumentWithSegments
from lilt.models.document_without_segments import DocumentWithoutSegments
from lilt.models.document_without_segments_status import DocumentWithoutSegmentsStatus
from lilt.models.document_workflow import DocumentWorkflow
from lilt.models.edit_filter_mapping_parameters import EditFilterMappingParameters
from lilt.models.error import Error
from lilt.models.file_delete_response import FileDeleteResponse
from lilt.models.inline_object import InlineObject
from lilt.models.inline_object1 import InlineObject1
from lilt.models.job import Job
from lilt.models.job_create_parameters import JobCreateParameters
from lilt.models.job_delete_response import JobDeleteResponse
from lilt.models.job_leverage_stats import JobLeverageStats
from lilt.models.job_project import JobProject
from lilt.models.job_stats import JobStats
from lilt.models.job_update_parameters import JobUpdateParameters
from lilt.models.language_pair import LanguagePair
from lilt.models.languages_response import LanguagesResponse
from lilt.models.lexicon_entry import LexiconEntry
from lilt.models.lexicon_entry_examples import LexiconEntryExamples
from lilt.models.lexicon_entry_source_span import LexiconEntrySourceSpan
from lilt.models.lexicon_entry_target_span import LexiconEntryTargetSpan
from lilt.models.lexicon_entry_translations import LexiconEntryTranslations
from lilt.models.lexicon_update_parameters import LexiconUpdateParameters
from lilt.models.lexicon_update_response import LexiconUpdateResponse
from lilt.models.match_band import MatchBand
from lilt.models.memory import Memory
from lilt.models.memory_create_parameters import MemoryCreateParameters
from lilt.models.memory_delete_response import MemoryDeleteResponse
from lilt.models.memory_import_response import MemoryImportResponse
from lilt.models.memory_insert_response import MemoryInsertResponse
from lilt.models.memory_update_parameters import MemoryUpdateParameters
from lilt.models.memory_update_response import MemoryUpdateResponse
from lilt.models.next_workflow_task import NextWorkflowTask
from lilt.models.project import Project
from lilt.models.project_create_parameters import ProjectCreateParameters
from lilt.models.project_delete_response import ProjectDeleteResponse
from lilt.models.project_quote import ProjectQuote
from lilt.models.project_stats import ProjectStats
from lilt.models.project_status import ProjectStatus
from lilt.models.project_update_response import ProjectUpdateResponse
from lilt.models.qa_rule_matches import QARuleMatches
from lilt.models.qa_rule_matches_context import QARuleMatchesContext
from lilt.models.qa_rule_matches_custom_rules import QARuleMatchesCustomRules
from lilt.models.qa_rule_matches_matches import QARuleMatchesMatches
from lilt.models.qa_rule_matches_replacements import QARuleMatchesReplacements
from lilt.models.qa_rule_matches_rule import QARuleMatchesRule
from lilt.models.qa_rule_matches_rule_category import QARuleMatchesRuleCategory
from lilt.models.qa_rule_matches_rule_urls import QARuleMatchesRuleUrls
from lilt.models.resource_status import ResourceStatus
from lilt.models.review_completion_type_error import ReviewCompletionTypeError
from lilt.models.segment import Segment
from lilt.models.segment_create_parameters import SegmentCreateParameters
from lilt.models.segment_delete_response import SegmentDeleteResponse
from lilt.models.segment_done_response import SegmentDoneResponse
from lilt.models.segment_update_parameters import SegmentUpdateParameters
from lilt.models.segment_with_comments import SegmentWithComments
from lilt.models.set_document_stage_request import SetDocumentStageRequest
from lilt.models.setting import Setting
from lilt.models.setting_upsert_body import SettingUpsertBody
from lilt.models.setting_upsert_response import SettingUpsertResponse
from lilt.models.source_file import SourceFile
from lilt.models.tagged_segment import TaggedSegment
from lilt.models.translate_completion_type_error import TranslateCompletionTypeError
from lilt.models.translate_register_response import TranslateRegisterResponse
from lilt.models.translate_segment_body import TranslateSegmentBody
from lilt.models.translate_segment_body1 import TranslateSegmentBody1
from lilt.models.translation import Translation
from lilt.models.translation_info import TranslationInfo
from lilt.models.translation_list import TranslationList
from lilt.models.translation_memory_entry import TranslationMemoryEntry
from lilt.models.workflow_stage import WorkflowStage
from lilt.models.workflow_stage_assignment import WorkflowStageAssignment
from lilt.models.workflow_stage_template import WorkflowStageTemplate
from lilt.models.workflow_task import WorkflowTask
from lilt.models.workflow_template import WorkflowTemplate

