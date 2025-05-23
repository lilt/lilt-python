# lilt.TranslateApi

All URIs are relative to *https://api.lilt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_translate_file**](TranslateApi.md#batch_translate_file) | **POST** /v2/translate/file | Translate a File
[**download_file**](TranslateApi.md#download_file) | **GET** /v2/translate/files | Download translated file
[**monitor_file_translation**](TranslateApi.md#monitor_file_translation) | **GET** /v2/translate/file | Monitor file translation
[**translate_segment_post**](TranslateApi.md#translate_segment_post) | **POST** /v2/translate | Translate a segment


# **batch_translate_file**
> List[TranslationInfo] batch_translate_file(file_id, memory_id, config_id=config_id, with_tm=with_tm)

Translate a File

Start machine translation of one or more Files that have previously been uploaded.  The response will include an `id` parameter that can be used to monitor and download the translations in subsequent calls.

Example CURL:
```bash
curl -X POST 'https://api.lilt.com/v2/translate/file?key=API_KEY&fileId=583&memoryId=2495&configId=123&withTM=true'
```



### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.translation_info import TranslationInfo
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
    api_instance = lilt.TranslateApi(api_client)
    file_id = 'file_id_example' # str | List of File ids to be translated, comma separated.
    memory_id = 'memory_id_example' # str | Id of Memory to use in translation.
    config_id = 3.4 # float | An optional pararameter to specify an import configuration to be applied when extracting translatable content from this file. (optional)
    with_tm = True # bool | An optional boolean parameter to toggle the use of Translation Memory in the translation of the file. (optional)

    try:
        # Translate a File
        api_response = api_instance.batch_translate_file(file_id, memory_id, config_id=config_id, with_tm=with_tm)
        print("The response of TranslateApi->batch_translate_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslateApi->batch_translate_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| List of File ids to be translated, comma separated. | 
 **memory_id** | **str**| Id of Memory to use in translation. | 
 **config_id** | **float**| An optional pararameter to specify an import configuration to be applied when extracting translatable content from this file. | [optional] 
 **with_tm** | **bool**| An optional boolean parameter to toggle the use of Translation Memory in the translation of the file. | [optional] 

### Return type

[**List[TranslationInfo]**](TranslationInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Translation Info |  -  |
**401** | Unauthorized |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file**
> bytearray download_file(id)

Download translated file

Download a translated File.

Example CURL:
```bash
curl -X GET 'https://api.lilt.com/v2/translate/files?key=API_KEY&id=1'
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
    api_instance = lilt.TranslateApi(api_client)
    id = 'id_example' # str | A translation id.

    try:
        # Download translated file
        api_response = api_instance.download_file(id)
        print("The response of TranslateApi->download_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslateApi->download_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A translation id. | 

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

# **monitor_file_translation**
> List[TranslationInfo] monitor_file_translation(translation_ids=translation_ids, status=status, from_time=from_time, to_time=to_time)

Monitor file translation

Get information about the one or more Files that are being translated with machine translation. Query filters are optional but at least one must be provided.

Example CURL:
```bash
curl -X GET 'https://api.lilt.com/v2/translate/file?key=API_KEY&translationIds=1,2&fromTime=1607966744&toTime=1707966744&status=InProgress'
```



### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.translation_info import TranslationInfo
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
    api_instance = lilt.TranslateApi(api_client)
    translation_ids = 'translation_ids_example' # str | List of translation ids, comma separated (optional)
    status = 'status_example' # str | One of the translation statuses - `InProgress`, `Completed`, `Failed`, `ReadyForDownload` (optional)
    from_time = 3.4 # float | Results after this time (inclusive) will be returned, specified as seconds since the Unix epoch. (optional)
    to_time = 3.4 # float | Results before this time (exclusive) will be returned, specified as seconds since the Unix epoch. (optional)

    try:
        # Monitor file translation
        api_response = api_instance.monitor_file_translation(translation_ids=translation_ids, status=status, from_time=from_time, to_time=to_time)
        print("The response of TranslateApi->monitor_file_translation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslateApi->monitor_file_translation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **translation_ids** | **str**| List of translation ids, comma separated | [optional] 
 **status** | **str**| One of the translation statuses - &#x60;InProgress&#x60;, &#x60;Completed&#x60;, &#x60;Failed&#x60;, &#x60;ReadyForDownload&#x60; | [optional] 
 **from_time** | **float**| Results after this time (inclusive) will be returned, specified as seconds since the Unix epoch. | [optional] 
 **to_time** | **float**| Results before this time (exclusive) will be returned, specified as seconds since the Unix epoch. | [optional] 

### Return type

[**List[TranslationInfo]**](TranslationInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Translation Info |  -  |
**401** | Unauthorized |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **translate_segment_post**
> TranslationList translate_segment_post(body=body)

Translate a segment

Translate a source string.

Setting the `rich` parameter to `true` will change the response format
to include additional information about each translation including a
model score, word alignments,  and formatting information. The rich
format can be seen in the example response on this page.

By default, this endpoint also returns translation memory (TM) fuzzy matches, along
with associated scores. Fuzzy matches always appear ahead of machine translation
output in the response.

The maximum source length is 5,000 characters.

Usage charges apply to this endpoint for production REST API keys.



### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.translate_segment_body import TranslateSegmentBody
from lilt.models.translation_list import TranslationList
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
    api_instance = lilt.TranslateApi(api_client)
    body = lilt.TranslateSegmentBody() # TranslateSegmentBody |  (optional)

    try:
        # Translate a segment
        api_response = api_instance.translate_segment_post(body=body)
        print("The response of TranslateApi->translate_segment_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslateApi->translate_segment_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TranslateSegmentBody**](TranslateSegmentBody.md)|  | [optional] 

### Return type

[**TranslationList**](TranslationList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/octet-stream, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A TranslationList object. |  -  |
**401** | Unauthorized |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

