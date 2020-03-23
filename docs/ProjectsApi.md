# pylilt.ProjectsApi

All URIs are relative to *https://lilt.com/2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](ProjectsApi.md#create_project) | **POST** /projects | Create a Project
[**delete_project**](ProjectsApi.md#delete_project) | **DELETE** /projects | Delete a Project
[**get_project**](ProjectsApi.md#get_project) | **GET** /projects | Retrieve a Project
[**get_project_report**](ProjectsApi.md#get_project_report) | **GET** /projects/quote | Retrieve Project report
[**get_project_status**](ProjectsApi.md#get_project_status) | **GET** /projects/status | Retrieve Project status
[**update_project**](ProjectsApi.md#update_project) | **PUT** /projects | Update a Project

# **create_project**
> Project create_project(body)

Create a Project

Create a Project. A Project is a collection of Documents.  A Project is associated with exactly one Memory.  Projects appear in the dashboard of the web app.  

### Example
```python
from __future__ import print_function
import time
import pylilt
from pylilt.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = pylilt.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'# Configure HTTP basic authorization: BasicAuth
configuration = pylilt.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pylilt.ProjectsApi(pylilt.ApiClient(configuration))
body = NULL # object | The Project resource to create.

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
 **body** | [**object**](object.md)| The Project resource to create. | 

### Return type

[**Project**](Project.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> object delete_project(id=id)

Delete a Project

Delete a Project. 

### Example
```python
from __future__ import print_function
import time
import pylilt
from pylilt.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = pylilt.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'# Configure HTTP basic authorization: BasicAuth
configuration = pylilt.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pylilt.ProjectsApi(pylilt.ApiClient(configuration))
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

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> list[Project] get_project(id=id, srclang=srclang, trglang=trglang, from_time=from_time, to_time=to_time, state=state, archived=archived)

Retrieve a Project

Retrieves one or more projects, including the documents associated with each project. Retrieving a project is the most efficient way to retrieve a single project or a list of all available projects.  To retrieve a specific project, specify the `id` request parameter. To retrieve all projects, omit the `id` request parameter. To limit the retrieved projects to those with a particular source language or target language, specify the corresponding ISO 639-1 language codes in the `srclang` and `trglang` request parameters, respectively.

### Example
```python
from __future__ import print_function
import time
import pylilt
from pylilt.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = pylilt.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'# Configure HTTP basic authorization: BasicAuth
configuration = pylilt.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pylilt.ProjectsApi(pylilt.ApiClient(configuration))
id = 56 # int | A unique Project identifier. (optional)
srclang = 'srclang_example' # str | An ISO 639-1 language code. (optional)
trglang = 'trglang_example' # str | An ISO 639-1 language code. (optional)
from_time = 56 # int | Unix time stamp (epoch, in seconds) of Projects with `created_at` greater than or equal to the value. (optional)
to_time = 56 # int | Unix time stamp (epoch, in seconds) of Projects with `created_at` less than the value. (optional)
state = 'state_example' # str | A project state (backlog, inProgress, inReview, inQA, done). (optional)
archived = true # bool | A flag that toggles whether to include archived projects in the response (the default is `true`). (optional)

try:
    # Retrieve a Project
    api_response = api_instance.get_project(id=id, srclang=srclang, trglang=trglang, from_time=from_time, to_time=to_time, state=state, archived=archived)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_project: %s\n" % e)
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

### Return type

[**list[Project]**](Project.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_report**
> ProjectQuote get_project_report(id)

Retrieve Project report

Get information about a project that can be used for quoting. This includes: * A translation memory leverage report * Word count * Segment count  

### Example
```python
from __future__ import print_function
import time
import pylilt
from pylilt.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = pylilt.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'# Configure HTTP basic authorization: BasicAuth
configuration = pylilt.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pylilt.ProjectsApi(pylilt.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_status**
> ProjectStatus get_project_status(id)

Retrieve Project status

Retrieve the status of a Project.  

### Example
```python
from __future__ import print_function
import time
import pylilt
from pylilt.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = pylilt.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'# Configure HTTP basic authorization: BasicAuth
configuration = pylilt.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pylilt.ProjectsApi(pylilt.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> Project update_project(body)

Update a Project

Update a Project. 

### Example
```python
from __future__ import print_function
import time
import pylilt
from pylilt.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = pylilt.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'# Configure HTTP basic authorization: BasicAuth
configuration = pylilt.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pylilt.ProjectsApi(pylilt.ApiClient(configuration))
body = NULL # object | The Project resource to update.

try:
    # Update a Project
    api_response = api_instance.update_project(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| The Project resource to update. | 

### Return type

[**Project**](Project.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

