# lilt.FilesApi

All URIs are relative to *https://api.lilt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_label**](FilesApi.md#add_label) | **POST** /v2/files/labels | Add Label to File
[**delete_file**](FilesApi.md#delete_file) | **DELETE** /v2/files | Delete a File
[**download**](FilesApi.md#download) | **GET** /v2/files/download | Download file
[**get_files**](FilesApi.md#get_files) | **GET** /v2/files | Retrieve a File
[**remove_label**](FilesApi.md#remove_label) | **DELETE** /v2/files/labels | Remove Label from File
[**upload_file**](FilesApi.md#upload_file) | **POST** /v2/files | Upload a File


# **add_label**
> add_label(id, name)

Add Label to File

Add a label to a File.

Example CURL:
```bash
curl -X POST 'https://api.lilt.com/v2/files/labels?key=API_KEY&id=1'
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "label_name"
}'
```


### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.add_file_label_request import AddFileLabelRequest
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
    api_instance = lilt.FilesApi(api_client)
    id = 'id_example' # str | A File id.
    name = lilt.AddFileLabelRequest() # AddFileLabelRequest | A label name.

    try:
        # Add Label to File
        api_instance.add_label(id, name)
    except Exception as e:
        print("Exception when calling FilesApi->add_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A File id. | 
 **name** | [**AddFileLabelRequest**](AddFileLabelRequest.md)| A label name. | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream, text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | A success response. |  -  |
**401** | Unauthorized |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file**
> FileDeleteResponse delete_file(id)

Delete a File

Delete a File.

Example CURL command:
```bash
  curl -X DELETE https://api.lilt.com/v2/files?key=API_KEY&id=123 
```



### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.file_delete_response import FileDeleteResponse
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
    api_instance = lilt.FilesApi(api_client)
    id = 56 # int | A unique File identifier.

    try:
        # Delete a File
        api_response = api_instance.delete_file(id)
        print("The response of FilesApi->delete_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->delete_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique File identifier. | 

### Return type

[**FileDeleteResponse**](FileDeleteResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | A status object. |  -  |
**401** | Unauthorized |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download**
> bytearray download(id)

Download file

Download a File.

Example CURL:
```bash
curl -X GET 'https://api.lilt.com/v2/files/download?key=API_KEY&id=1'
```


### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
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
    api_instance = lilt.FilesApi(api_client)
    id = 'id_example' # str | A File id.

    try:
        # Download file
        api_response = api_instance.download(id)
        print("The response of FilesApi->download:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->download: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A File id. | 

### Return type

**bytearray**

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A file. |  -  |
**401** | Unauthorized |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_files**
> List[SourceFile] get_files(id=id, labels=labels)

Retrieve a File

Retrieves one or more files available to your user. Files are not associated with a project or a memory. They are unprocessed and can be used later in the project/document creation workflow step.

To retrieve a specific file, specify the <strong>id</strong> request parameter. To retrieve all files, omit the <strong>id</strong> request parameter.

Example CURL command:
```bash
 curl -X GET https://api.lilt.com/v2/files?key=API_KEY&id=274
```

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.source_file import SourceFile
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
    api_instance = lilt.FilesApi(api_client)
    id = 56 # int | A unique File identifier. (optional)
    labels = ['labels_example'] # List[str] | One or more labels. This will return the files which contain all of the given labels.  (optional)

    try:
        # Retrieve a File
        api_response = api_instance.get_files(id=id, labels=labels)
        print("The response of FilesApi->get_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique File identifier. | [optional] 
 **labels** | [**List[str]**](str.md)| One or more labels. This will return the files which contain all of the given labels.  | [optional] 

### Return type

[**List[SourceFile]**](SourceFile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of files. |  -  |
**401** | Unauthorized |  -  |
**403** | User does not have permission for provided file. |  -  |
**410** | File deleted. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_label**
> remove_label(id, name)

Remove Label from File

Remove a label from a File.

Example CURL:
```bash
curl -X DELETE 'https://api.lilt.com/v2/files/labels?key=API_KEY&id=1&name=label_name'
```


### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
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
    api_instance = lilt.FilesApi(api_client)
    id = 'id_example' # str | A File id.
    name = 'name_example' # str | A label name.

    try:
        # Remove Label from File
        api_instance.remove_label(id, name)
    except Exception as e:
        print("Exception when calling FilesApi->remove_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A File id. | 
 **name** | **str**| A label name. | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | A success response. |  -  |
**401** | Unauthorized |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> SourceFile upload_file(name, body, file_hash=file_hash, lang_id=lang_id, project_id=project_id, category=category, labels=labels, job_type=job_type)

Upload a File

Upload a File in any of the formats [documented in our knowledge
base](https://support.lilt.com/hc/en-us/articles/360020816253-File-Formats).
Request parameters should be passed in as query string parameters.

Example CURL command:
```bash
  curl -X POST https://api.lilt.com/v2/files?key=API_KEY&name=en_US.json \
  --header "Content-Type: application/octet-stream" \
  --data-binary @en_US.json
```
Calls to GET /files are used to monitor the language detection results. The API response will be augmented to include detected language and confidence score.

The language detection will complete asynchronously. Prior to completion, the `detected_lang` value will be `zxx`, the reserved ISO 639-2 code for "No linguistic content/not applicable".

If the language can not be determined, or the detection process fails, the `detected_lang` field will return `und`, the reserved ISO 639-2 code for undetermined language, and the `detected_lang_confidence` score will be `0`.



### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.source_file import SourceFile
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
    api_instance = lilt.FilesApi(api_client)
    name = 'name_example' # str | A file name.
    body = None # bytearray | The file contents to be uploaded. The entire POST body will be treated as the file.
    file_hash = 'file_hash_example' # str | A hash value to associate with the file. The MD5 hash of the body contents will be used by default if a value isn't provided. (optional)
    lang_id = True # bool | Flag indicating whether to perform language detection on the uploaded file. Default is false. (optional)
    project_id = 56 # int | The project to associate the uploaded file with. (optional)
    category = 'category_example' # str | The category of the file. The options are `REFERENCE`, or `API`. The default is API. Files with the `REFERENCE` category will be displayed as reference material. (optional)
    labels = 'labels_example' # str | Comma-separated list of labels to add to the uploaded document. (optional)
    job_type = 'job_type_example' # str | Specifies the job type when adding this file to a job. (optional)

    try:
        # Upload a File
        api_response = api_instance.upload_file(name, body, file_hash=file_hash, lang_id=lang_id, project_id=project_id, category=category, labels=labels, job_type=job_type)
        print("The response of FilesApi->upload_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->upload_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| A file name. | 
 **body** | **bytearray**| The file contents to be uploaded. The entire POST body will be treated as the file. | 
 **file_hash** | **str**| A hash value to associate with the file. The MD5 hash of the body contents will be used by default if a value isn&#39;t provided. | [optional] 
 **lang_id** | **bool**| Flag indicating whether to perform language detection on the uploaded file. Default is false. | [optional] 
 **project_id** | **int**| The project to associate the uploaded file with. | [optional] 
 **category** | **str**| The category of the file. The options are &#x60;REFERENCE&#x60;, or &#x60;API&#x60;. The default is API. Files with the &#x60;REFERENCE&#x60; category will be displayed as reference material. | [optional] 
 **labels** | **str**| Comma-separated list of labels to add to the uploaded document. | [optional] 
 **job_type** | **str**| Specifies the job type when adding this file to a job. | [optional] 

### Return type

[**SourceFile**](SourceFile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json, application/octet-stream, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A SourceFile object. |  -  |
**401** | Unauthorized |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

