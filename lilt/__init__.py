# coding: utf-8

# flake8: noqa

"""
    Lilt REST API

    The Lilt REST API enables programmatic access to the full-range of Lilt backend services including:   * Training of and translating with interactive, adaptive machine translation   * Large-scale translation memory   * The Lexicon (a large-scale termbase)   * Programmatic control of the Lilt CAT environment   * Translation memory synchronization  Requests and responses are in JSON format. The REST API only responds to HTTPS / SSL requests. ## Authentication Requests are authenticated via REST API key, which requires the Business plan.  Requests are authenticated using [HTTP Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication). Add your REST API key as both the `username` and `password`.  For development, you may also pass the REST API key via the `key` query parameter. This is less secure than HTTP Basic Auth, and is not recommended for production use.   # noqa: E501

    The version of the OpenAPI document: v2.0
    Contact: support@lilt.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "0.5.2"

# import apis into sdk package
from lilt.api.connectors_api import ConnectorsApi
from lilt.api.documents_api import DocumentsApi
from lilt.api.files_api import FilesApi
from lilt.api.languages_api import LanguagesApi
from lilt.api.lexicon_api import LexiconApi
from lilt.api.memories_api import MemoriesApi
from lilt.api.projects_api import ProjectsApi
from lilt.api.qa_api import QAApi
from lilt.api.root_api import RootApi
from lilt.api.segments_api import SegmentsApi
from lilt.api.translate_api import TranslateApi

# import ApiClient
from lilt.api_client import ApiClient
from lilt.configuration import Configuration
from lilt.exceptions import OpenApiException
from lilt.exceptions import ApiTypeError
from lilt.exceptions import ApiValueError
from lilt.exceptions import ApiKeyError
from lilt.exceptions import ApiException
# import models into sdk package
from lilt.models.annotation import Annotation
from lilt.models.api_root import ApiRoot
from lilt.models.comment import Comment
from lilt.models.connector import Connector
from lilt.models.connector_arguments import ConnectorArguments
from lilt.models.connector_delete_response import ConnectorDeleteResponse
from lilt.models.connector_job import ConnectorJob
from lilt.models.document_assignment_parameters import DocumentAssignmentParameters
from lilt.models.document_assignment_response import DocumentAssignmentResponse
from lilt.models.document_delete_response import DocumentDeleteResponse
from lilt.models.document_done_update_parameters import DocumentDoneUpdateParameters
from lilt.models.document_parameters import DocumentParameters
from lilt.models.document_pretranslate_parameters import DocumentPretranslateParameters
from lilt.models.document_pretranslate_response import DocumentPretranslateResponse
from lilt.models.document_pretranslating import DocumentPretranslating
from lilt.models.document_pretranslating_status import DocumentPretranslatingStatus
from lilt.models.document_quote import DocumentQuote
from lilt.models.document_update_parameters import DocumentUpdateParameters
from lilt.models.document_with_segments import DocumentWithSegments
from lilt.models.document_without_segments import DocumentWithoutSegments
from lilt.models.document_without_segments_status import DocumentWithoutSegmentsStatus
from lilt.models.error import Error
from lilt.models.file import File
from lilt.models.file_delete_response import FileDeleteResponse
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
from lilt.models.project import Project
from lilt.models.project_create_parameters import ProjectCreateParameters
from lilt.models.project_delete_response import ProjectDeleteResponse
from lilt.models.project_quote import ProjectQuote
from lilt.models.project_status import ProjectStatus
from lilt.models.project_update_response import ProjectUpdateResponse
from lilt.models.qa_rule_matches import QARuleMatches
from lilt.models.qa_rule_matches_context import QARuleMatchesContext
from lilt.models.qa_rule_matches_matches import QARuleMatchesMatches
from lilt.models.qa_rule_matches_replacements import QARuleMatchesReplacements
from lilt.models.qa_rule_matches_rule import QARuleMatchesRule
from lilt.models.qa_rule_matches_rule_category import QARuleMatchesRuleCategory
from lilt.models.qa_rule_matches_rule_urls import QARuleMatchesRuleUrls
from lilt.models.resource_status import ResourceStatus
from lilt.models.segment import Segment
from lilt.models.segment_create_parameters import SegmentCreateParameters
from lilt.models.segment_delete_response import SegmentDeleteResponse
from lilt.models.segment_update_parameters import SegmentUpdateParameters
from lilt.models.segment_with_comments import SegmentWithComments
from lilt.models.tagged_segment import TaggedSegment
from lilt.models.translate_register_response import TranslateRegisterResponse
from lilt.models.translation import Translation
from lilt.models.translation_list import TranslationList
from lilt.models.translation_memory_entry import TranslationMemoryEntry

