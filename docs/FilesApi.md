# lilt.FilesApi

All URIs are relative to *https://lilt.com/2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_file**](FilesApi.md#delete_file) | **DELETE** /files | Delete a File
[**get_files**](FilesApi.md#get_files) | **GET** /files | Retrieve a File
[**upload_file**](FilesApi.md#upload_file) | **POST** /files | Upload a File


# **delete_file**
> FileDeleteResponse delete_file(id)

Delete a File

Delete a File.  Example CURL command: ```   curl -X DELETE https://lilt.com/2/files?key=API_KEY&id=123 ```  

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
    api_instance = lilt.FilesApi(api_client)
    id = 56 # int | A unique File identifier.

    try:
        # Delete a File
        api_response = api_instance.delete_file(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->delete_file: %s\n" % e)
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
    api_instance = lilt.FilesApi(api_client)
    id = 56 # int | A unique File identifier.

    try:
        # Delete a File
        api_response = api_instance.delete_file(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->delete_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique File identifier. | 

### Return type

[**FileDeleteResponse**](FileDeleteResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | A status object. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_files**
> list[SourceFile] get_files(id=id)

Retrieve a File

Retrieves one or more files available to your user. Files are not associated with a project or a memory. They are unprocessed and can be used later in the project/document creation workflow step.  To retrieve a specific file, specify the <strong>id</strong> request parameter. To retrieve all files, omit the <strong>id</strong> request parameter.  Example CURL command: ```  curl -X GET https://lilt.com/2/files?key=API_KEY&id=274```

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
    api_instance = lilt.FilesApi(api_client)
    id = 56 # int | A unique File identifier. (optional)

    try:
        # Retrieve a File
        api_response = api_instance.get_files(id=id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->get_files: %s\n" % e)
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
    api_instance = lilt.FilesApi(api_client)
    id = 56 # int | A unique File identifier. (optional)

    try:
        # Retrieve a File
        api_response = api_instance.get_files(id=id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->get_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique File identifier. | [optional] 

### Return type

[**list[SourceFile]**](SourceFile.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of files. |  -  |
**403** | Unauthorized. |  -  |
**410** | File deleted. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> SourceFile upload_file(name, body, file_hash=file_hash, lang_id=lang_id, project_id=project_id, category=category, labels=labels)

Upload a File

Upload a File in any of the formats [documented in our knowledge base](https://support.lilt.com/hc/en-us/articles/360020816253-File-Formats). Request parameters should be passed in as query string parameters.  Example CURL command: ```   curl -X POST https://lilt.com/2/files?key=API_KEY&name=en_US.json \\   --header \"Content-Type: application/octet-stream\" \\   --data-binary @en_US.json ``` Calls to GET /files are used to monitor the language detection results. The API response will be augmented to include detected language and confidence score.  The language detection will complete asynchronously. Prior to completion, the `detected_lang` value will be `zxx`, the reserved ISO 639-2 code for \"No linguistic content/not applicable\".  If the language can not be determined, or the detection process fails, the `detected_lang` field will return `und`, the reserved ISO 639-2 code for undetermined language, and the `detected_lang_confidence` score will be `0`.  

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
    api_instance = lilt.FilesApi(api_client)
    name = 'name_example' # str | A file name.
body = '/path/to/file' # file | The file contents to be uploaded. The entire POST body will be treated as the file.
file_hash = 'file_hash_example' # str | A hash value to associate with the file. The MD5 hash of the body contents will be used by default if a value isn't provided. (optional)
lang_id = True # bool | Flag indicating whether to perform language detection on the uploaded file. Default is false. (optional)
project_id = 56 # int | The project to associate the uploaded file with. (optional)
category = 'category_example' # str | The category of the file. The options are `REFERENCE`, or `API`. The default is API. Files with the `REFERENCE` category will be displayed as reference material. (optional)
labels = 'labels_example' # str | Comma-separated list of labels to add to the uploaded document. (optional)

    try:
        # Upload a File
        api_response = api_instance.upload_file(name, body, file_hash=file_hash, lang_id=lang_id, project_id=project_id, category=category, labels=labels)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->upload_file: %s\n" % e)
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
    api_instance = lilt.FilesApi(api_client)
    name = 'name_example' # str | A file name.
body = '/path/to/file' # file | The file contents to be uploaded. The entire POST body will be treated as the file.
file_hash = 'file_hash_example' # str | A hash value to associate with the file. The MD5 hash of the body contents will be used by default if a value isn't provided. (optional)
lang_id = True # bool | Flag indicating whether to perform language detection on the uploaded file. Default is false. (optional)
project_id = 56 # int | The project to associate the uploaded file with. (optional)
category = 'category_example' # str | The category of the file. The options are `REFERENCE`, or `API`. The default is API. Files with the `REFERENCE` category will be displayed as reference material. (optional)
labels = 'labels_example' # str | Comma-separated list of labels to add to the uploaded document. (optional)

    try:
        # Upload a File
        api_response = api_instance.upload_file(name, body, file_hash=file_hash, lang_id=lang_id, project_id=project_id, category=category, labels=labels)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->upload_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| A file name. | 
 **body** | **file**| The file contents to be uploaded. The entire POST body will be treated as the file. | 
 **file_hash** | **str**| A hash value to associate with the file. The MD5 hash of the body contents will be used by default if a value isn&#39;t provided. | [optional] 
 **lang_id** | **bool**| Flag indicating whether to perform language detection on the uploaded file. Default is false. | [optional] 
 **project_id** | **int**| The project to associate the uploaded file with. | [optional] 
 **category** | **str**| The category of the file. The options are &#x60;REFERENCE&#x60;, or &#x60;API&#x60;. The default is API. Files with the &#x60;REFERENCE&#x60; category will be displayed as reference material. | [optional] 
 **labels** | **str**| Comma-separated list of labels to add to the uploaded document. | [optional] 

### Return type

[**SourceFile**](SourceFile.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A SourceFile object. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

