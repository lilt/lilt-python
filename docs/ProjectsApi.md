# lilt.ProjectsApi

All URIs are relative to *https://lilt.com/2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](ProjectsApi.md#create_project) | **POST** /projects | Create a Project
[**delete_project**](ProjectsApi.md#delete_project) | **DELETE** /projects | Delete a Project
[**deliver_projects_bulk**](ProjectsApi.md#deliver_projects_bulk) | **POST** /projects/bulk-deliver | Deliver multiple projects apart from their jobs.
[**get_project_report**](ProjectsApi.md#get_project_report) | **GET** /projects/quote | Retrieve Project report
[**get_project_revision_report**](ProjectsApi.md#get_project_revision_report) | **GET** /projects/{id}/revision | Retrieve Project revision report
[**get_project_status**](ProjectsApi.md#get_project_status) | **GET** /projects/status | Retrieve Project status
[**get_projects**](ProjectsApi.md#get_projects) | **GET** /projects | Retrieve a Project
[**trigger_auto_assignment**](ProjectsApi.md#trigger_auto_assignment) | **POST** /autoAssignment | Auto Assignment
[**update_projects_bulk**](ProjectsApi.md#update_projects_bulk) | **PUT** /projects/bulk-update | Update multiple Projects with a single payload


# **create_project**
> Project create_project(body)

Create a Project

Create a Project. A Project is a collection of Documents.  A Project is associated with exactly one Memory.  Projects appear in the dashboard of the web app.  

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
    api_instance = lilt.ProjectsApi(api_client)
    body = lilt.ProjectCreateParameters() # ProjectCreateParameters | 

    try:
        # Create a Project
        api_response = api_instance.create_project(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->create_project: %s\n" % e)
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
    api_instance = lilt.ProjectsApi(api_client)
    body = lilt.ProjectCreateParameters() # ProjectCreateParameters | 

    try:
        # Create a Project
        api_response = api_instance.create_project(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectCreateParameters**](ProjectCreateParameters.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Project object. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> ProjectDeleteResponse delete_project(id=id)

Delete a Project

Delete a Project. 

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
    api_instance = lilt.ProjectsApi(api_client)
    id = 56 # int | A unique Project identifier. (optional)

    try:
        # Delete a Project
        api_response = api_instance.delete_project(id=id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->delete_project: %s\n" % e)
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
    api_instance = lilt.ProjectsApi(api_client)
    id = 56 # int | A unique Project identifier. (optional)

    try:
        # Delete a Project
        api_response = api_instance.delete_project(id=id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique Project identifier. | [optional] 

### Return type

[**ProjectDeleteResponse**](ProjectDeleteResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A status object. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deliver_projects_bulk**
> deliver_projects_bulk(body, workflow_enabled=workflow_enabled)

Deliver multiple projects apart from their jobs.

Deliver mulitple projects apart from their jobs. 

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
    api_instance = lilt.ProjectsApi(api_client)
    body = lilt.InlineObject1() # InlineObject1 | 
workflow_enabled = True # bool | Whether the project has or not workflows enabled. (not used) (optional)

    try:
        # Deliver multiple projects apart from their jobs.
        api_instance.deliver_projects_bulk(body, workflow_enabled=workflow_enabled)
    except ApiException as e:
        print("Exception when calling ProjectsApi->deliver_projects_bulk: %s\n" % e)
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
    api_instance = lilt.ProjectsApi(api_client)
    body = lilt.InlineObject1() # InlineObject1 | 
workflow_enabled = True # bool | Whether the project has or not workflows enabled. (not used) (optional)

    try:
        # Deliver multiple projects apart from their jobs.
        api_instance.deliver_projects_bulk(body, workflow_enabled=workflow_enabled)
    except ApiException as e:
        print("Exception when calling ProjectsApi->deliver_projects_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InlineObject1**](InlineObject1.md)|  | 
 **workflow_enabled** | **bool**| Whether the project has or not workflows enabled. (not used) | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Empty response if succeed. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_report**
> ProjectQuote get_project_report(id)

Retrieve Project report

Get information about a project that can be used for quoting. This includes: * A translation memory leverage report * Word count * Segment count  

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
    api_instance = lilt.ProjectsApi(api_client)
    id = 56 # int | A unique Project identifier.

    try:
        # Retrieve Project report
        api_response = api_instance.get_project_report(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->get_project_report: %s\n" % e)
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
    api_instance = lilt.ProjectsApi(api_client)
    id = 56 # int | A unique Project identifier.

    try:
        # Retrieve Project report
        api_response = api_instance.get_project_report(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->get_project_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique Project identifier. | 

### Return type

[**ProjectQuote**](ProjectQuote.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object that represents a Project quote. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_revision_report**
> get_project_revision_report(id)

Retrieve Project revision report

Get information about a project's revision report. This includes: * Stats on accepted segments * reviewer details * Error rate  

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
    api_instance = lilt.ProjectsApi(api_client)
    id = 56 # int | A unique Project identifier.

    try:
        # Retrieve Project revision report
        api_instance.get_project_revision_report(id)
    except ApiException as e:
        print("Exception when calling ProjectsApi->get_project_revision_report: %s\n" % e)
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
    api_instance = lilt.ProjectsApi(api_client)
    id = 56 # int | A unique Project identifier.

    try:
        # Retrieve Project revision report
        api_instance.get_project_revision_report(id)
    except ApiException as e:
        print("Exception when calling ProjectsApi->get_project_revision_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique Project identifier. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A csv file containing revision report. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_status**
> ProjectStatus get_project_status(id)

Retrieve Project status

Retrieve the status of a Project.  

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
    api_instance = lilt.ProjectsApi(api_client)
    id = 56 # int | A unique Project identifier.

    try:
        # Retrieve Project status
        api_response = api_instance.get_project_status(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->get_project_status: %s\n" % e)
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
    api_instance = lilt.ProjectsApi(api_client)
    id = 56 # int | A unique Project identifier.

    try:
        # Retrieve Project status
        api_response = api_instance.get_project_status(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->get_project_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique Project identifier. | 

### Return type

[**ProjectStatus**](ProjectStatus.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object that represents a Project status report. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects**
> list[Project] get_projects(id=id, srclang=srclang, trglang=trglang, from_time=from_time, to_time=to_time, state=state, archived=archived, connector_id=connector_id)

Retrieve a Project

Retrieves one or more projects, including the documents associated with each project. Retrieving a project is the most efficient way to retrieve a single project or a list of all available projects.  To retrieve a specific project, specify the `id` request parameter. To retrieve all projects, omit the `id` request parameter. To limit the retrieved projects to those with a particular source language or target language, specify the corresponding ISO 639-1 language codes in the `srclang` and `trglang` request parameters, respectively.

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
    api_instance = lilt.ProjectsApi(api_client)
    id = 56 # int | A unique Project identifier. (optional)
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
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->get_projects: %s\n" % e)
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
    api_instance = lilt.ProjectsApi(api_client)
    id = 56 # int | A unique Project identifier. (optional)
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
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->get_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique Project identifier. | [optional] 
 **srclang** | **str**| An ISO 639-1 language code. | [optional] 
 **trglang** | **str**| An ISO 639-1 language code. | [optional] 
 **from_time** | **int**| Unix time stamp (epoch, in seconds) of Projects with &#x60;created_at&#x60; greater than or equal to the value. | [optional] 
 **to_time** | **int**| Unix time stamp (epoch, in seconds) of Projects with &#x60;created_at&#x60; less than the value. | [optional] 
 **state** | **str**| A project state (backlog, inProgress, inReview, inQA, done). | [optional] 
 **archived** | **bool**| A flag that toggles whether to include archived projects in the response (the default is &#x60;true&#x60;). | [optional] 
 **connector_id** | **int**| A unique Connector identifier. | [optional] 

### Return type

[**list[Project]**](Project.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Project objects. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_auto_assignment**
> list[AutoAssignmentResponse] trigger_auto_assignment(project_ids, body=body)

Auto Assignment

Trigger automatic assignment of linguists.  Requires auto-assignment to be enabled as a setting on the origanization level. 

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
    api_instance = lilt.ProjectsApi(api_client)
    project_ids = 'project_ids_example' # str | The comma separated list of project ids to auto-assign. Can be sent in the body as an alternative but if both are specified the query has precedence. 
body = lilt.AutoAssignmentParameters() # AutoAssignmentParameters |  (optional)

    try:
        # Auto Assignment
        api_response = api_instance.trigger_auto_assignment(project_ids, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->trigger_auto_assignment: %s\n" % e)
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
    api_instance = lilt.ProjectsApi(api_client)
    project_ids = 'project_ids_example' # str | The comma separated list of project ids to auto-assign. Can be sent in the body as an alternative but if both are specified the query has precedence. 
body = lilt.AutoAssignmentParameters() # AutoAssignmentParameters |  (optional)

    try:
        # Auto Assignment
        api_response = api_instance.trigger_auto_assignment(project_ids, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->trigger_auto_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_ids** | **str**| The comma separated list of project ids to auto-assign. Can be sent in the body as an alternative but if both are specified the query has precedence.  | 
 **body** | [**AutoAssignmentParameters**](AutoAssignmentParameters.md)|  | [optional] 

### Return type

[**list[AutoAssignmentResponse]**](AutoAssignmentResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An auto assignment response. |  -  |
**400** | Bad request. Possible causes include no permission to the projects and the auto-assignment setting not being enabled. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_projects_bulk**
> list[Project] update_projects_bulk(body)

Update multiple Projects with a single payload

Update multiple Projects with a single payload. 

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
    api_instance = lilt.ProjectsApi(api_client)
    body = lilt.InlineObject() # InlineObject | 

    try:
        # Update multiple Projects with a single payload
        api_response = api_instance.update_projects_bulk(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->update_projects_bulk: %s\n" % e)
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
    api_instance = lilt.ProjectsApi(api_client)
    body = lilt.InlineObject() # InlineObject | 

    try:
        # Update multiple Projects with a single payload
        api_response = api_instance.update_projects_bulk(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectsApi->update_projects_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InlineObject**](InlineObject.md)|  | 

### Return type

[**list[Project]**](Project.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Project objects. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

