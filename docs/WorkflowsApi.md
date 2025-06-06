# lilt.WorkflowsApi

All URIs are relative to *https://api.lilt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_workflow_templates**](WorkflowsApi.md#get_workflow_templates) | **GET** /v2/workflows/templates | Retrieve workflow templates


# **get_workflow_templates**
> List[WorkflowTemplate] get_workflow_templates()

Retrieve workflow templates

Get all of the possible Workflow Templates owned by the team. Useful for retrieving the ids corresponding to each workflow tables, and passing them to subsequent requests, for example, creating a new Job with a specific Workflow.
Example CURL:
```bash curl -X GET 'https://api.lilt.com/v2/workflows/templates?key=API_KEY' ```


### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.workflow_template import WorkflowTemplate
from lilt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.lilt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = lilt.Configuration(
    host = "https://api.lilt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = lilt.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with lilt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lilt.WorkflowsApi(api_client)

    try:
        # Retrieve workflow templates
        api_response = api_instance.get_workflow_templates()
        print("The response of WorkflowsApi->get_workflow_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->get_workflow_templates: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[WorkflowTemplate]**](WorkflowTemplate.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array with a team&#39;s available WorkflowTemplates. |  -  |
**401** | Unauthorized |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

