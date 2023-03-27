# lilt.WorkflowsApi

All URIs are relative to *https://lilt.com/2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**advance_workflow_stage**](WorkflowsApi.md#advance_workflow_stage) | **POST** /document/{documentId}/task/{taskId}/advance | Advance workflow to the next stage
[**get_document_workflow**](WorkflowsApi.md#get_document_workflow) | **GET** /workflows/document/{documentId} | Retrieve document Workflow metadata
[**get_workflow_templates**](WorkflowsApi.md#get_workflow_templates) | **GET** /workflows/templates | Retrieve workflow templates
[**reject_workflow_stage**](WorkflowsApi.md#reject_workflow_stage) | **POST** /document/{documentId}/task/{taskId}/reject | Move workflow to the previous stage
[**set_document_stage**](WorkflowsApi.md#set_document_stage) | **PUT** /workflows/{documentId}/stage | Set Workflow stage for a document


# **advance_workflow_stage**
> NextWorkflowTask advance_workflow_stage(document_id, task_id)

Advance workflow to the next stage

Advance a workflow to the next stage and mark current workflow task as complete.  Example CURL: ``` curl --X --request POST 'https://lilt.com/2/workflows/document/{documentId}/task/{taskId}/advance?key=API_KEY' ```  

### Example

* Api Key Authentication (ApiKeyAuth):
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
    api_instance = lilt.WorkflowsApi(api_client)
    document_id = 56 # int | A document id.
task_id = 56 # int | The task id of the current workflow stage.

    try:
        # Advance workflow to the next stage
        api_response = api_instance.advance_workflow_stage(document_id, task_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowsApi->advance_workflow_stage: %s\n" % e)
```

* Basic Authentication (BasicAuth):
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
    api_instance = lilt.WorkflowsApi(api_client)
    document_id = 56 # int | A document id.
task_id = 56 # int | The task id of the current workflow stage.

    try:
        # Advance workflow to the next stage
        api_response = api_instance.advance_workflow_stage(document_id, task_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowsApi->advance_workflow_stage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **int**| A document id. | 
 **task_id** | **int**| The task id of the current workflow stage. | 

### Return type

[**NextWorkflowTask**](NextWorkflowTask.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object with a documents next task Workflow metadata. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_workflow**
> DocumentWorkflow get_document_workflow(document_id)

Retrieve document Workflow metadata

Get Workflow metadata related to a document. This is useful for gathering information about the current Workflow stage of a document.  Example CURL: ``` curl --X --request GET 'https://lilt.com/2/workflows/document/{documentId}?key=API_KEY' ```  

### Example

* Api Key Authentication (ApiKeyAuth):
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
    api_instance = lilt.WorkflowsApi(api_client)
    document_id = 56 # int | A document id.

    try:
        # Retrieve document Workflow metadata
        api_response = api_instance.get_document_workflow(document_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowsApi->get_document_workflow: %s\n" % e)
```

* Basic Authentication (BasicAuth):
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
    api_instance = lilt.WorkflowsApi(api_client)
    document_id = 56 # int | A document id.

    try:
        # Retrieve document Workflow metadata
        api_response = api_instance.get_document_workflow(document_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowsApi->get_document_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **int**| A document id. | 

### Return type

[**DocumentWorkflow**](DocumentWorkflow.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object with document Workflow metadata. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_templates**
> list[WorkflowTemplate] get_workflow_templates()

Retrieve workflow templates

Get all the possible Workflow Templates owned by the team. Useful for retrieving the ids corresponding to each workflow tables, and passing them to subsequent requests, for example, creating a new Job with a specific Workflow.  Example CURL: ``` curl --X --request GET 'https://lilt.com/2/workflows/templates?key=API_KEY' ```  

### Example

* Api Key Authentication (ApiKeyAuth):
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
    api_instance = lilt.WorkflowsApi(api_client)
    
    try:
        # Retrieve workflow templates
        api_response = api_instance.get_workflow_templates()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowsApi->get_workflow_templates: %s\n" % e)
```

* Basic Authentication (BasicAuth):
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
    api_instance = lilt.WorkflowsApi(api_client)
    
    try:
        # Retrieve workflow templates
        api_response = api_instance.get_workflow_templates()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowsApi->get_workflow_templates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[WorkflowTemplate]**](WorkflowTemplate.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array with a team&#39;s available WorkflowTemplates. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reject_workflow_stage**
> NextWorkflowTask reject_workflow_stage(document_id, task_id)

Move workflow to the previous stage

Move a workflow to the previous stage and mark current workflow task as rejected.  Example CURL: ``` curl --X --request POST 'https://lilt.com/2/workflows/document/{documentId}/task/{taskId}/reject?key=API_KEY' ```  

### Example

* Api Key Authentication (ApiKeyAuth):
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
    api_instance = lilt.WorkflowsApi(api_client)
    document_id = 56 # int | A document id.
task_id = 56 # int | The task id of the current workflow stage.

    try:
        # Move workflow to the previous stage
        api_response = api_instance.reject_workflow_stage(document_id, task_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowsApi->reject_workflow_stage: %s\n" % e)
```

* Basic Authentication (BasicAuth):
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
    api_instance = lilt.WorkflowsApi(api_client)
    document_id = 56 # int | A document id.
task_id = 56 # int | The task id of the current workflow stage.

    try:
        # Move workflow to the previous stage
        api_response = api_instance.reject_workflow_stage(document_id, task_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowsApi->reject_workflow_stage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **int**| A document id. | 
 **task_id** | **int**| The task id of the current workflow stage. | 

### Return type

[**NextWorkflowTask**](NextWorkflowTask.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object with a documents next task Workflow metadata. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_document_stage**
> NextWorkflowTask set_document_stage(document_id, workflow_stage_id=workflow_stage_id)

Set Workflow stage for a document

Set the Workflow stage for a document. You can find the stage information required for this request from the \"Retrieve document Workflow metadata\" endpoint.  Example CURL: ``` curl --X --request PUT 'https://lilt.com/2/workflows/document/{documentId}/stage?key=API_KEY' \\ --header 'Content-Type: application/json' \\ --data-raw '{   \"workflowStageId\": {workflowStageId} }' ```  

### Example

* Api Key Authentication (ApiKeyAuth):
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
    api_instance = lilt.WorkflowsApi(api_client)
    document_id = 56 # int | A document id.
workflow_stage_id = lilt.SetDocumentStageRequest() # SetDocumentStageRequest |  (optional)

    try:
        # Set Workflow stage for a document
        api_response = api_instance.set_document_stage(document_id, workflow_stage_id=workflow_stage_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowsApi->set_document_stage: %s\n" % e)
```

* Basic Authentication (BasicAuth):
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
    api_instance = lilt.WorkflowsApi(api_client)
    document_id = 56 # int | A document id.
workflow_stage_id = lilt.SetDocumentStageRequest() # SetDocumentStageRequest |  (optional)

    try:
        # Set Workflow stage for a document
        api_response = api_instance.set_document_stage(document_id, workflow_stage_id=workflow_stage_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowsApi->set_document_stage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **int**| A document id. | 
 **workflow_stage_id** | [**SetDocumentStageRequest**](SetDocumentStageRequest.md)|  | [optional] 

### Return type

[**NextWorkflowTask**](NextWorkflowTask.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object with a documents next task Workflow metadata. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

