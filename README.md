# lilt
The Lilt REST API enables programmatic access to the full-range of Lilt backend services including:
  * Training of and translating with interactive, adaptive machine translation
  * Large-scale translation memory
  * The Lexicon (a large-scale termbase)
  * Programmatic control of the Lilt CAT environment
  * Translation memory synchronization

Requests and responses are in JSON format. The REST API only responds to HTTPS / SSL requests.
## Authentication
Requests are authenticated via REST API key, which requires the Business plan.

Requests are authenticated using [HTTP Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication). Add your REST API key as both the `username` and `password`.

For development, you may also pass the REST API key via the `key` query parameter. This is less secure than HTTP Basic Auth, and is not recommended for production use.


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v2.0
- Package version: 0.6.3
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://lilt.com/docs/api](https://lilt.com/docs/api)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/lilt/lilt-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/lilt/lilt-python.git`)

Then import the package:
```python
import lilt
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import lilt
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
import lilt
from lilt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://lilt.com/2
# See configuration.py for a list of all supported configuration parameters.
configuration = lilt.Configuration(
    host = "https://lilt.com/2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration = lilt.Configuration(
    host = "https://lilt.com/2",
    api_key = {
        'key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = lilt.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)


# Enter a context with an instance of the API client
with lilt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lilt.CommentsApi(api_client)
    document_id = 56 # int | A unique document identifier.
segment_id = 56 # int | A unique segment identifier.
body = lilt.CommentBody() # CommentBody | The comment being created

    try:
        # Create a new comment
        api_response = api_instance.create_comment(document_id, segment_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommentsApi->create_comment: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *https://lilt.com/2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CommentsApi* | [**create_comment**](docs/CommentsApi.md#create_comment) | **POST** /comments | Create a new comment
*CommentsApi* | [**delete_comment**](docs/CommentsApi.md#delete_comment) | **DELETE** /comments | Delete a Comment
*CommentsApi* | [**get_document_comments**](docs/CommentsApi.md#get_document_comments) | **GET** /comments | Retrieve a document&#39;s comments by segment
*CommentsApi* | [**update_comment**](docs/CommentsApi.md#update_comment) | **PUT** /comments | Update an existing comment
*ConnectorsApi* | [**create_connector**](docs/ConnectorsApi.md#create_connector) | **POST** /connectors | Upload a Connector
*ConnectorsApi* | [**delete_connector**](docs/ConnectorsApi.md#delete_connector) | **DELETE** /connectors | Delete a Connector
*ConnectorsApi* | [**export_connector_job**](docs/ConnectorsApi.md#export_connector_job) | **POST** /connectors/jobs/deliver | Deliver a Connector Job
*ConnectorsApi* | [**get_connector_jobs**](docs/ConnectorsApi.md#get_connector_jobs) | **GET** /connectors/jobs | Retrieve a Connector Job
*ConnectorsApi* | [**get_connectors**](docs/ConnectorsApi.md#get_connectors) | **GET** /connectors | Retrieve a Connector
*ConnectorsApi* | [**sync_connector**](docs/ConnectorsApi.md#sync_connector) | **POST** /connectors/sync | Sync a Connector
*ConnectorsApi* | [**update_connector**](docs/ConnectorsApi.md#update_connector) | **PUT** /connectors | Upload a Connector
*DocumentsApi* | [**assign_document**](docs/DocumentsApi.md#assign_document) | **PUT** /documents/share | Assign a Document
*DocumentsApi* | [**create_document**](docs/DocumentsApi.md#create_document) | **POST** /documents | Create a Document
*DocumentsApi* | [**delete_document**](docs/DocumentsApi.md#delete_document) | **DELETE** /documents | Delete a Document
*DocumentsApi* | [**document_translation_done**](docs/DocumentsApi.md#document_translation_done) | **POST** /documents/done/translation | Mark translation done
*DocumentsApi* | [**document_unlock**](docs/DocumentsApi.md#document_unlock) | **POST** /documents/done/unlock | Unlock documents
*DocumentsApi* | [**documents_done_review_post**](docs/DocumentsApi.md#documents_done_review_post) | **POST** /documents/done/review | Mark review done
*DocumentsApi* | [**download_document**](docs/DocumentsApi.md#download_document) | **GET** /documents/files | Download a Document
*DocumentsApi* | [**get_document**](docs/DocumentsApi.md#get_document) | **GET** /documents | Retrieve a Document
*DocumentsApi* | [**pretranslate_documents**](docs/DocumentsApi.md#pretranslate_documents) | **POST** /documents/pretranslate | Pretranslate a Document
*DocumentsApi* | [**update_document**](docs/DocumentsApi.md#update_document) | **PUT** /documents | Update a Document
*DocumentsApi* | [**upload_document**](docs/DocumentsApi.md#upload_document) | **POST** /documents/files | Upload a File
*FilesApi* | [**delete_file**](docs/FilesApi.md#delete_file) | **DELETE** /files | Delete a File
*FilesApi* | [**get_files**](docs/FilesApi.md#get_files) | **GET** /files | Retrieve a File
*FilesApi* | [**upload_file**](docs/FilesApi.md#upload_file) | **POST** /files | Upload a File
*JobsApi* | [**archive_job**](docs/JobsApi.md#archive_job) | **POST** /jobs/{jobId}/archive | Archive a Job
*JobsApi* | [**create_job**](docs/JobsApi.md#create_job) | **POST** /jobs | Create a Job
*JobsApi* | [**delete_job**](docs/JobsApi.md#delete_job) | **DELETE** /jobs/{jobId} | Delete a Job
*JobsApi* | [**deliver_job**](docs/JobsApi.md#deliver_job) | **POST** /jobs/{jobId}/deliver | Deliver a Job
*JobsApi* | [**download_job**](docs/JobsApi.md#download_job) | **GET** /jobs/{jobId}/downlod | Download a Job
*JobsApi* | [**export_job**](docs/JobsApi.md#export_job) | **GET** /jobs/{jobId}/export | Export a Job
*JobsApi* | [**get_job**](docs/JobsApi.md#get_job) | **GET** /jobs/{jobId} | Retrieve a Job
*JobsApi* | [**get_job_leverage_stats**](docs/JobsApi.md#get_job_leverage_stats) | **POST** /jobs/{jobId}/stats | Retrieve Job Leverage Stats
*JobsApi* | [**reactivate_job**](docs/JobsApi.md#reactivate_job) | **POST** /jobs/{jobId}/reactivate | Reactivate a Job
*JobsApi* | [**retrieve_all_jobs**](docs/JobsApi.md#retrieve_all_jobs) | **GET** /jobs | Retrieve all Jobs
*JobsApi* | [**unarchive_job**](docs/JobsApi.md#unarchive_job) | **POST** /jobs/{jobId}/unarchive | Unarchive a Job
*JobsApi* | [**update_job**](docs/JobsApi.md#update_job) | **PUT** /jobs/{jobId} | Update a Job
*LanguagesApi* | [**get_languages**](docs/LanguagesApi.md#get_languages) | **GET** /languages | Retrieve supported languages
*LexiconApi* | [**query_lexicon**](docs/LexiconApi.md#query_lexicon) | **GET** /lexicon | Query a Lexicon
*LexiconApi* | [**update_lexicon**](docs/LexiconApi.md#update_lexicon) | **POST** /lexicon | Update a Lexicon
*MemoriesApi* | [**create_memory**](docs/MemoriesApi.md#create_memory) | **POST** /memories | Create a Memory
*MemoriesApi* | [**delete_memory**](docs/MemoriesApi.md#delete_memory) | **DELETE** /memories | Delete a Memory
*MemoriesApi* | [**get_memory**](docs/MemoriesApi.md#get_memory) | **GET** /memories | Retrieve a Memory
*MemoriesApi* | [**import_memory_file**](docs/MemoriesApi.md#import_memory_file) | **POST** /memories/import | File import for a Memory
*MemoriesApi* | [**query_memory**](docs/MemoriesApi.md#query_memory) | **GET** /memories/query | Query a Memory
*MemoriesApi* | [**sync_delete_memory**](docs/MemoriesApi.md#sync_delete_memory) | **DELETE** /memories/sync | Delete-sync for a Memory
*MemoriesApi* | [**sync_down_memory**](docs/MemoriesApi.md#sync_down_memory) | **GET** /memories/sync | Get-sync for a Memory
*MemoriesApi* | [**sync_insert_memory**](docs/MemoriesApi.md#sync_insert_memory) | **POST** /memories/sync | Insert-sync for a Memory
*MemoriesApi* | [**sync_update_memory**](docs/MemoriesApi.md#sync_update_memory) | **PUT** /memories/sync | Update-sync for a Memory
*MemoriesApi* | [**update_memory**](docs/MemoriesApi.md#update_memory) | **PUT** /memories | Update the name of a Memory
*ProjectsApi* | [**create_project**](docs/ProjectsApi.md#create_project) | **POST** /projects | Create a Project
*ProjectsApi* | [**delete_project**](docs/ProjectsApi.md#delete_project) | **DELETE** /projects | Delete a Project
*ProjectsApi* | [**get_project_report**](docs/ProjectsApi.md#get_project_report) | **GET** /projects/quote | Retrieve Project report
*ProjectsApi* | [**get_project_status**](docs/ProjectsApi.md#get_project_status) | **GET** /projects/status | Retrieve Project status
*ProjectsApi* | [**get_projects**](docs/ProjectsApi.md#get_projects) | **GET** /projects | Retrieve a Project
*ProjectsApi* | [**update_project**](docs/ProjectsApi.md#update_project) | **PUT** /projects | Update a Project
*QAApi* | [**qa_check**](docs/QAApi.md#qa_check) | **GET** /qa | Perform QA check
*RootApi* | [**root**](docs/RootApi.md#root) | **GET** / | Retrieve the REST API root
*SegmentsApi* | [**create_segment**](docs/SegmentsApi.md#create_segment) | **POST** /segments | Create a Segment
*SegmentsApi* | [**delete_segment**](docs/SegmentsApi.md#delete_segment) | **DELETE** /segments | Delete a Segment
*SegmentsApi* | [**get_segment**](docs/SegmentsApi.md#get_segment) | **GET** /segments | Retrieve a Segment
*SegmentsApi* | [**segments_review_unlock_post**](docs/SegmentsApi.md#segments_review_unlock_post) | **POST** /segments/review/unlock | Unaccept and unlock segments
*SegmentsApi* | [**tag_segment**](docs/SegmentsApi.md#tag_segment) | **GET** /segments/tag | Tag a Segment
*SegmentsApi* | [**update_segment**](docs/SegmentsApi.md#update_segment) | **PUT** /segments | Update a Segment
*SettingsApi* | [**get_organization_settings**](docs/SettingsApi.md#get_organization_settings) | **GET** /settings/organization | Update or create a setting
*SettingsApi* | [**get_project_settings**](docs/SettingsApi.md#get_project_settings) | **GET** /settings/project/{projectId} | Get settings for a project
*SettingsApi* | [**get_user_settings**](docs/SettingsApi.md#get_user_settings) | **GET** /settings/user | Get settings for a project
*SettingsApi* | [**upsert_setting**](docs/SettingsApi.md#upsert_setting) | **POST** /settings | Get organization-level settings
*TranslateApi* | [**batch_translate_file**](docs/TranslateApi.md#batch_translate_file) | **POST** /translate/file | Translate a File
*TranslateApi* | [**download_file**](docs/TranslateApi.md#download_file) | **GET** /translate/files | Download translated file
*TranslateApi* | [**monitor_file_translation**](docs/TranslateApi.md#monitor_file_translation) | **GET** /translate/file | Monitor file translation
*TranslateApi* | [**register_segment**](docs/TranslateApi.md#register_segment) | **GET** /translate/register | Register a segment
*TranslateApi* | [**translate_segment**](docs/TranslateApi.md#translate_segment) | **GET** /translate | Translate a segment


## Documentation For Models

 - [Annotation](docs/Annotation.md)
 - [ApiRoot](docs/ApiRoot.md)
 - [Comment](docs/Comment.md)
 - [CommentBody](docs/CommentBody.md)
 - [CommentDeleteResponse](docs/CommentDeleteResponse.md)
 - [Connector](docs/Connector.md)
 - [ConnectorArguments](docs/ConnectorArguments.md)
 - [ConnectorDeleteResponse](docs/ConnectorDeleteResponse.md)
 - [ConnectorJob](docs/ConnectorJob.md)
 - [DocumentAssignmentParameters](docs/DocumentAssignmentParameters.md)
 - [DocumentAssignmentResponse](docs/DocumentAssignmentResponse.md)
 - [DocumentComments](docs/DocumentComments.md)
 - [DocumentDeleteResponse](docs/DocumentDeleteResponse.md)
 - [DocumentDoneUpdateParameters](docs/DocumentDoneUpdateParameters.md)
 - [DocumentDoneUpdateParameters1](docs/DocumentDoneUpdateParameters1.md)
 - [DocumentDoneUpdateParameters2](docs/DocumentDoneUpdateParameters2.md)
 - [DocumentParameters](docs/DocumentParameters.md)
 - [DocumentPretranslateParameters](docs/DocumentPretranslateParameters.md)
 - [DocumentPretranslateResponse](docs/DocumentPretranslateResponse.md)
 - [DocumentPretranslating](docs/DocumentPretranslating.md)
 - [DocumentPretranslatingStatus](docs/DocumentPretranslatingStatus.md)
 - [DocumentQuote](docs/DocumentQuote.md)
 - [DocumentUpdateParameters](docs/DocumentUpdateParameters.md)
 - [DocumentWithSegments](docs/DocumentWithSegments.md)
 - [DocumentWithoutSegments](docs/DocumentWithoutSegments.md)
 - [DocumentWithoutSegmentsStatus](docs/DocumentWithoutSegmentsStatus.md)
 - [Error](docs/Error.md)
 - [FileDeleteResponse](docs/FileDeleteResponse.md)
 - [Job](docs/Job.md)
 - [JobCreateParameters](docs/JobCreateParameters.md)
 - [JobDeleteResponse](docs/JobDeleteResponse.md)
 - [JobLeverageStats](docs/JobLeverageStats.md)
 - [JobLeverageStatsProjects](docs/JobLeverageStatsProjects.md)
 - [JobProject](docs/JobProject.md)
 - [JobStats](docs/JobStats.md)
 - [JobUpdateParameters](docs/JobUpdateParameters.md)
 - [LanguagePair](docs/LanguagePair.md)
 - [LanguagesResponse](docs/LanguagesResponse.md)
 - [LexiconEntry](docs/LexiconEntry.md)
 - [LexiconEntryExamples](docs/LexiconEntryExamples.md)
 - [LexiconEntrySourceSpan](docs/LexiconEntrySourceSpan.md)
 - [LexiconEntryTargetSpan](docs/LexiconEntryTargetSpan.md)
 - [LexiconEntryTranslations](docs/LexiconEntryTranslations.md)
 - [LexiconUpdateParameters](docs/LexiconUpdateParameters.md)
 - [LexiconUpdateResponse](docs/LexiconUpdateResponse.md)
 - [MatchBand](docs/MatchBand.md)
 - [Memory](docs/Memory.md)
 - [MemoryCreateParameters](docs/MemoryCreateParameters.md)
 - [MemoryDeleteResponse](docs/MemoryDeleteResponse.md)
 - [MemoryImportResponse](docs/MemoryImportResponse.md)
 - [MemoryInsertResponse](docs/MemoryInsertResponse.md)
 - [MemoryUpdateParameters](docs/MemoryUpdateParameters.md)
 - [MemoryUpdateResponse](docs/MemoryUpdateResponse.md)
 - [Project](docs/Project.md)
 - [ProjectCreateParameters](docs/ProjectCreateParameters.md)
 - [ProjectDeleteResponse](docs/ProjectDeleteResponse.md)
 - [ProjectQuote](docs/ProjectQuote.md)
 - [ProjectStatus](docs/ProjectStatus.md)
 - [ProjectUpdateResponse](docs/ProjectUpdateResponse.md)
 - [QARuleMatches](docs/QARuleMatches.md)
 - [QARuleMatchesContext](docs/QARuleMatchesContext.md)
 - [QARuleMatchesMatches](docs/QARuleMatchesMatches.md)
 - [QARuleMatchesReplacements](docs/QARuleMatchesReplacements.md)
 - [QARuleMatchesRule](docs/QARuleMatchesRule.md)
 - [QARuleMatchesRuleCategory](docs/QARuleMatchesRuleCategory.md)
 - [QARuleMatchesRuleUrls](docs/QARuleMatchesRuleUrls.md)
 - [ResourceStatus](docs/ResourceStatus.md)
 - [Segment](docs/Segment.md)
 - [SegmentCreateParameters](docs/SegmentCreateParameters.md)
 - [SegmentDeleteResponse](docs/SegmentDeleteResponse.md)
 - [SegmentDoneResponse](docs/SegmentDoneResponse.md)
 - [SegmentUpdateParameters](docs/SegmentUpdateParameters.md)
 - [SegmentWithComments](docs/SegmentWithComments.md)
 - [Setting](docs/Setting.md)
 - [SettingDictionary](docs/SettingDictionary.md)
 - [SettingUpsertResponse](docs/SettingUpsertResponse.md)
 - [SourceFile](docs/SourceFile.md)
 - [TaggedSegment](docs/TaggedSegment.md)
 - [TranslateRegisterResponse](docs/TranslateRegisterResponse.md)
 - [Translation](docs/Translation.md)
 - [TranslationInfo](docs/TranslationInfo.md)
 - [TranslationList](docs/TranslationList.md)
 - [TranslationMemoryEntry](docs/TranslationMemoryEntry.md)


## Documentation For Authorization


## ApiKeyAuth

- **Type**: API key
- **API key parameter name**: key
- **Location**: URL query string


## BasicAuth

- **Type**: HTTP basic authentication


## Author

support@lilt.com


