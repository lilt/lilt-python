# lilt.DocumentsApi

All URIs are relative to *https://api.lilt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_document**](DocumentsApi.md#download_document) | **GET** /v2/documents/files | Download a Document
[**upload_document**](DocumentsApi.md#upload_document) | **POST** /v2/documents/files | Upload a File


# **download_document**
> str download_document(id, is_xliff=is_xliff)

Download a Document

Export a Document that has been translated in the Lilt web application. Any Document can be downloaded in XLIFF 1.2 format, or can be retrieved in its original uploaded format by setting `is_xliff=false`. This endpoint will fail if either (a) export or (b) pre-translation operations are in-progress. The status of those operations can be determined by retrieving the Document resource. Example CURL command: ```   curl -X GET https://api.lilt.com/v2/documents/files?key=API_KEY&id=274 -o from_lilt.xliff ```  

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
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

# Configure API key authorization: ApiKeyAuth
configuration = lilt.Configuration(
    host = "https://api.lilt.com",
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
    api_instance = lilt.DocumentsApi(api_client)
    id = 56 # int | An unique Document identifier.
is_xliff = True # bool | Download the document in XLIFF 1.2 format. (optional) (default to True)

    try:
        # Download a Document
        api_response = api_instance.download_document(id, is_xliff=is_xliff)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentsApi->download_document: %s\n" % e)
```

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
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

# Configure API key authorization: ApiKeyAuth
configuration = lilt.Configuration(
    host = "https://api.lilt.com",
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
    api_instance = lilt.DocumentsApi(api_client)
    id = 56 # int | An unique Document identifier.
is_xliff = True # bool | Download the document in XLIFF 1.2 format. (optional) (default to True)

    try:
        # Download a Document
        api_response = api_instance.download_document(id, is_xliff=is_xliff)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentsApi->download_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| An unique Document identifier. | 
 **is_xliff** | **bool**| Download the document in XLIFF 1.2 format. | [optional] [default to True]

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A file. |  -  |
**502** | File in pretranslation. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_document**
> DocumentWithSegments upload_document(name, project_id, body, pretranslate=pretranslate, auto_accept=auto_accept, case_sensitive=case_sensitive, match_attribution=match_attribution, config_id=config_id)

Upload a File

Create a Document from a file in any of the formats [documented in our knowledge base](https://support.lilt.com/hc/en-us/articles/360020816253-File-Formats). Request parameters should be passed as JSON object with the header field `LILT-API`.  File names in the header can only contain [US-ASCII characters](https://en.wikipedia.org/wiki/ASCII). File names with characters outside of US-ASCII should be [URI encoded](https://en.wikipedia.org/wiki/Percent-encoding) or transliterated to US-ASCII strings.  Example CURL command: ```   curl -X POST https://api.lilt.com/v2/documents/files?key=API_KEY \\   --header \"LILT-API: {\\\"name\\\": \\\"introduction.xliff\\\",\\\"pretranslate\\\": \\\"tm+mt\\\",\\\"project_id\\\": 9}\" \\   --header \"Content-Type: application/octet-stream\" \\   --data-binary @Introduction.xliff ```  

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
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

# Configure API key authorization: ApiKeyAuth
configuration = lilt.Configuration(
    host = "https://api.lilt.com",
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
    api_instance = lilt.DocumentsApi(api_client)
    name = 'name_example' # str | A file name.
project_id = 56 # int | A unique Project identifier.
body = '/path/to/file' # file | The file contents to be uploaded. The entire POST body will be treated as the file. 
pretranslate = 'pretranslate_example' # str | An optional parameter indicating if and how the document will be pretranslated upon being uploaded. The accepted values are `TM`, or `TM+MT`  (optional)
auto_accept = True # bool | An optional parameter to auto-accept segments with 100% translation memory matches when the `pretranslate` option is also set, or to auto-accept any target data that is present when the uploaded file is XLIFF. If omitted it will default to your organization settings for `Accept and lock exact matches`, if set to `false`, no segments will be auto-accepted.  (optional)
case_sensitive = True # bool | An optional parameter to use case sensitive translation memory matching when the `pretranslate` option is also enabled. Matches must have identical character-by-character case to qualify as matches. Default value matches your organization settings for `Use case sensitive translation memory matching` setting  (optional)
match_attribution = True # bool | An optional parameter to attribute translation authorship of exact matches to the author of the file when the `pretranslate` option is also enabled. Default value matches your organization settings for `Translation authorship` setting  (optional)
config_id = 56 # int | An optional pararameter to specify an import configuration to be applied when extracting translatable content from this file.  (optional)

    try:
        # Upload a File
        api_response = api_instance.upload_document(name, project_id, body, pretranslate=pretranslate, auto_accept=auto_accept, case_sensitive=case_sensitive, match_attribution=match_attribution, config_id=config_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentsApi->upload_document: %s\n" % e)
```

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
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

# Configure API key authorization: ApiKeyAuth
configuration = lilt.Configuration(
    host = "https://api.lilt.com",
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
    api_instance = lilt.DocumentsApi(api_client)
    name = 'name_example' # str | A file name.
project_id = 56 # int | A unique Project identifier.
body = '/path/to/file' # file | The file contents to be uploaded. The entire POST body will be treated as the file. 
pretranslate = 'pretranslate_example' # str | An optional parameter indicating if and how the document will be pretranslated upon being uploaded. The accepted values are `TM`, or `TM+MT`  (optional)
auto_accept = True # bool | An optional parameter to auto-accept segments with 100% translation memory matches when the `pretranslate` option is also set, or to auto-accept any target data that is present when the uploaded file is XLIFF. If omitted it will default to your organization settings for `Accept and lock exact matches`, if set to `false`, no segments will be auto-accepted.  (optional)
case_sensitive = True # bool | An optional parameter to use case sensitive translation memory matching when the `pretranslate` option is also enabled. Matches must have identical character-by-character case to qualify as matches. Default value matches your organization settings for `Use case sensitive translation memory matching` setting  (optional)
match_attribution = True # bool | An optional parameter to attribute translation authorship of exact matches to the author of the file when the `pretranslate` option is also enabled. Default value matches your organization settings for `Translation authorship` setting  (optional)
config_id = 56 # int | An optional pararameter to specify an import configuration to be applied when extracting translatable content from this file.  (optional)

    try:
        # Upload a File
        api_response = api_instance.upload_document(name, project_id, body, pretranslate=pretranslate, auto_accept=auto_accept, case_sensitive=case_sensitive, match_attribution=match_attribution, config_id=config_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentsApi->upload_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| A file name. | 
 **project_id** | **int**| A unique Project identifier. | 
 **body** | **file**| The file contents to be uploaded. The entire POST body will be treated as the file.  | 
 **pretranslate** | **str**| An optional parameter indicating if and how the document will be pretranslated upon being uploaded. The accepted values are &#x60;TM&#x60;, or &#x60;TM+MT&#x60;  | [optional] 
 **auto_accept** | **bool**| An optional parameter to auto-accept segments with 100% translation memory matches when the &#x60;pretranslate&#x60; option is also set, or to auto-accept any target data that is present when the uploaded file is XLIFF. If omitted it will default to your organization settings for &#x60;Accept and lock exact matches&#x60;, if set to &#x60;false&#x60;, no segments will be auto-accepted.  | [optional] 
 **case_sensitive** | **bool**| An optional parameter to use case sensitive translation memory matching when the &#x60;pretranslate&#x60; option is also enabled. Matches must have identical character-by-character case to qualify as matches. Default value matches your organization settings for &#x60;Use case sensitive translation memory matching&#x60; setting  | [optional] 
 **match_attribution** | **bool**| An optional parameter to attribute translation authorship of exact matches to the author of the file when the &#x60;pretranslate&#x60; option is also enabled. Default value matches your organization settings for &#x60;Translation authorship&#x60; setting  | [optional] 
 **config_id** | **int**| An optional pararameter to specify an import configuration to be applied when extracting translatable content from this file.  | [optional] 

### Return type

[**DocumentWithSegments**](DocumentWithSegments.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Document object. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

