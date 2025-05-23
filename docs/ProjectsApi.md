# lilt.ProjectsApi

All URIs are relative to *https://api.lilt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](ProjectsApi.md#create_project) | **POST** /v2/projects | Create a Project
[**delete_project**](ProjectsApi.md#delete_project) | **DELETE** /v2/projects | Delete a Project
[**get_projects**](ProjectsApi.md#get_projects) | **GET** /v2/projects | Retrieve a Project


# **create_project**
> Project create_project(body)

Create a Project

Create a Project. A Project is a collection of Documents.

A Project is associated with exactly one Memory.

Projects appear in the dashboard of the web app.



### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.project import Project
from lilt.models.project_create_parameters import ProjectCreateParameters
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
    api_instance = lilt.ProjectsApi(api_client)
    body = lilt.ProjectCreateParameters() # ProjectCreateParameters | The Project resource to create.

    try:
        # Create a Project
        api_response = api_instance.create_project(body)
        print("The response of ProjectsApi->create_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->create_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectCreateParameters**](ProjectCreateParameters.md)| The Project resource to create. | 

### Return type

[**Project**](Project.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/octet-stream, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Project object. |  -  |
**401** | Unauthorized |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> ProjectDeleteResponse delete_project(id=id)

Delete a Project

Delete a Project.


### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.project_delete_response import ProjectDeleteResponse
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
    api_instance = lilt.ProjectsApi(api_client)
    id = 56 # int | A unique Project identifier. (optional)

    try:
        # Delete a Project
        api_response = api_instance.delete_project(id=id)
        print("The response of ProjectsApi->delete_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->delete_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique Project identifier. | [optional] 

### Return type

[**ProjectDeleteResponse**](ProjectDeleteResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A status object. |  -  |
**401** | Unauthorized |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects**
> List[Project] get_projects(id=id, srclang=srclang, trglang=trglang, from_time=from_time, to_time=to_time, state=state, archived=archived, connector_id=connector_id)

Retrieve a Project

Retrieves one or more projects, including the documents associated with each project. Retrieving a project is the most efficient way to retrieve a single project, multiple projects or a list of all available projects.

To retrieve a specific project, specify the `id` request parameter or you can retrieve multiple projects by adding comma (,) between ids eg. `?id=1234,5678`. To retrieve all projects, omit the `id` request parameter. To limit the retrieved projects to those with a particular source language or target language, specify the corresponding ISO 639-1 language codes in the `srclang` and `trglang` request parameters, respectively.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.project import Project
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
    api_instance = lilt.ProjectsApi(api_client)
    id = 56 # int | A unique Project identifier. It can be a single id or multiple ids separated by a comma (optional)
    srclang = 'srclang_example' # str | An ISO 639-1 language code. (optional)
    trglang = 'trglang_example' # str | An ISO 639-1 language code. (optional)
    from_time = 56 # int | Unix time stamp (epoch, in seconds) of Projects with `created_at` greater than or equal to the value. (optional)
    to_time = 56 # int | Unix time stamp (epoch, in seconds) of Projects with `created_at` less than the value. (optional)
    state = 'state_example' # str | A project state (backlog, inProgress, inReview, inQA, done). (optional)
    archived = True # bool | A flag that toggles whether to include archived projects in the response (the default is `true`). (optional)
    connector_id = 56 # int | A unique Connector identifier. (optional)

    try:
        # Retrieve a Project
        api_response = api_instance.get_projects(id=id, srclang=srclang, trglang=trglang, from_time=from_time, to_time=to_time, state=state, archived=archived, connector_id=connector_id)
        print("The response of ProjectsApi->get_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_projects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique Project identifier. It can be a single id or multiple ids separated by a comma | [optional] 
 **srclang** | **str**| An ISO 639-1 language code. | [optional] 
 **trglang** | **str**| An ISO 639-1 language code. | [optional] 
 **from_time** | **int**| Unix time stamp (epoch, in seconds) of Projects with &#x60;created_at&#x60; greater than or equal to the value. | [optional] 
 **to_time** | **int**| Unix time stamp (epoch, in seconds) of Projects with &#x60;created_at&#x60; less than the value. | [optional] 
 **state** | **str**| A project state (backlog, inProgress, inReview, inQA, done). | [optional] 
 **archived** | **bool**| A flag that toggles whether to include archived projects in the response (the default is &#x60;true&#x60;). | [optional] 
 **connector_id** | **int**| A unique Connector identifier. | [optional] 

### Return type

[**List[Project]**](Project.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Project objects. |  -  |
**401** | Unauthorized |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

