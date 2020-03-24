# lilt.FilesApi

All URIs are relative to *https://lilt.com/2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_file**](FilesApi.md#delete_file) | **DELETE** /files | Delete a File
[**get_files**](FilesApi.md#get_files) | **GET** /files | Retrieve a File
[**upload_file**](FilesApi.md#upload_file) | **POST** /files | Upload a File

# **delete_file**
> object delete_file(id)

Delete a File

Delete a File.  Example CURL command: ```   curl -X DELETE https://lilt.com/2/files?key=API_KEY&id=123 ```  

### Example
```python
from __future__ import print_function
import time
import lilt
from lilt.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = lilt.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'# Configure HTTP basic authorization: BasicAuth
configuration = lilt.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = lilt.FilesApi(lilt.ApiClient(configuration))
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

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_files**
> File get_files(id=id)

Retrieve a File

Retrieves one or more files available to your user. Files are not associated with a project or a memory. They are unprocessed and can be used later in the project/document creation workflow step.  To retrieve a specific file, specify the <strong>id</strong> request parameter. To retrieve all files, omit the <strong>id</strong> request parameter.  Example cURL command: ```  curl -X GET https://lilt.com/2/files?key=API_KEY&id=274```

### Example
```python
from __future__ import print_function
import time
import lilt
from lilt.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = lilt.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'# Configure HTTP basic authorization: BasicAuth
configuration = lilt.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = lilt.FilesApi(lilt.ApiClient(configuration))
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

[**File**](File.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> File upload_file(body, name, export_uri=export_uri, file_hash=file_hash)

Upload a File

Upload a File in any of the formats [documented in our knowledge base](https://support.lilt.com/hc/en-us/articles/360020816253-File-Formats). Request parameters should be passed in as query string parameters.  When uploading a file, any parameters needed to issue a request to the specified export_uri can be encoded in the export_uri itself as query parameters. Typical examples of parameters that may be required are an access token to authorize requests to a third-party HTTP API and the unique identifier of a resource available via the third-party HTTP API that corresponds to the file. An example export_uri that encodes a target resource identifier (i.e., source_id) of an associated resource behind a third party HTTP API is given in the cURL command below.  Example cURL command: ```   curl -X POST https://lilt.com/2/files?key=API_KEY&name=en_US.json&export_uri=https://example.com/export?source_id=12345 \\   --header \"Content-Type: application/octet-stream\" \\   --data-binary @en_US.json ```  

### Example
```python
from __future__ import print_function
import time
import lilt
from lilt.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = lilt.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'# Configure HTTP basic authorization: BasicAuth
configuration = lilt.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = lilt.FilesApi(lilt.ApiClient(configuration))
body = 'body_example' # str | The file contents to be uploaded. The entire POST body will be treated as the file.
name = 'name_example' # str | A file name.
export_uri = 'export_uri_example' # str | A webhook endpoint that will export the translated document back to the source repository. (optional)
file_hash = 'file_hash_example' # str | A hash value to associate with the file. The MD5 hash of the body contents will be used by default if a value isn't provided. (optional)

try:
    # Upload a File
    api_response = api_instance.upload_file(body, name, export_uri=export_uri, file_hash=file_hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->upload_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| The file contents to be uploaded. The entire POST body will be treated as the file. | 
 **name** | **str**| A file name. | 
 **export_uri** | **str**| A webhook endpoint that will export the translated document back to the source repository. | [optional] 
 **file_hash** | **str**| A hash value to associate with the file. The MD5 hash of the body contents will be used by default if a value isn&#x27;t provided. | [optional] 

### Return type

[**File**](File.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

