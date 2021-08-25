# lilt.TranslateApi

All URIs are relative to *https://lilt.com/2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_translate_file**](TranslateApi.md#batch_translate_file) | **POST** /translate/file | Translate a File
[**download_file**](TranslateApi.md#download_file) | **GET** /translate/files | Download translated file
[**monitor_file_translation**](TranslateApi.md#monitor_file_translation) | **GET** /translate/file | Monitor file translation
[**register_segment**](TranslateApi.md#register_segment) | **GET** /translate/register | Register a segment
[**translate_segment**](TranslateApi.md#translate_segment) | **GET** /translate | Translate a segment


# **batch_translate_file**
> list[TranslationInfo] batch_translate_file(file_id, memory_id, config_id=config_id)

Translate a File

Start machine translation of one or more Files that have previously been uploaded.  The response will include an `id` parameter that can be used to monitor and download the translations in subsequent calls.  Example CURL: ``` curl --X --request POST 'https://lilt.com/2/translate/file?key=API_KEY&fileId=583&memoryId=2495&configId=123' ```  

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
    api_instance = lilt.TranslateApi(api_client)
    file_id = 'file_id_example' # str | List of File ids to be translated, comma separated.
memory_id = 'memory_id_example' # str | Id of Memory to use in translation.
config_id = 3.4 # float | An optional pararameter to specify an import configuration to be applied when extracting translatable content from this file. (optional)

    try:
        # Translate a File
        api_response = api_instance.batch_translate_file(file_id, memory_id, config_id=config_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TranslateApi->batch_translate_file: %s\n" % e)
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
    api_instance = lilt.TranslateApi(api_client)
    file_id = 'file_id_example' # str | List of File ids to be translated, comma separated.
memory_id = 'memory_id_example' # str | Id of Memory to use in translation.
config_id = 3.4 # float | An optional pararameter to specify an import configuration to be applied when extracting translatable content from this file. (optional)

    try:
        # Translate a File
        api_response = api_instance.batch_translate_file(file_id, memory_id, config_id=config_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TranslateApi->batch_translate_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| List of File ids to be translated, comma separated. | 
 **memory_id** | **str**| Id of Memory to use in translation. | 
 **config_id** | **float**| An optional pararameter to specify an import configuration to be applied when extracting translatable content from this file. | [optional] 

### Return type

[**list[TranslationInfo]**](TranslationInfo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Translation info |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file**
> str download_file(id)

Download translated file

Download a translated File.  Example CURL: ``` curl --X --request GET 'https://lilt.com/2/translate/files?key=API_KEY&id=1' ```  

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
    api_instance = lilt.TranslateApi(api_client)
    id = 'id_example' # str | A translation id.

    try:
        # Download translated file
        api_response = api_instance.download_file(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TranslateApi->download_file: %s\n" % e)
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
    api_instance = lilt.TranslateApi(api_client)
    id = 'id_example' # str | A translation id.

    try:
        # Download translated file
        api_response = api_instance.download_file(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TranslateApi->download_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A translation id. | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **monitor_file_translation**
> TranslationInfo monitor_file_translation(translation_ids=translation_ids, status=status, from_time=from_time, to_time=to_time)

Monitor file translation

Get information about the one or more Files that are being translated with machine translation. Query filters are optional but at least one must be provided.  Example CURL: ``` curl --X --request GET 'https://lilt.com/2/translate/file?key=API_KEY&translationIds=1,2&fromTime=1607966744&toTime=1707966744&status=InProgress' ```  

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
    api_instance = lilt.TranslateApi(api_client)
    translation_ids = 'translation_ids_example' # str | List of translation ids, comma separated (optional)
status = 'status_example' # str | One of the translation statuses - `InProgress`, `Completed`, `Failed`, `ReadyForDownload` (optional)
from_time = 3.4 # float | Results after this time (inclusive) will be returned, specified as seconds since the Unix epoch. (optional)
to_time = 3.4 # float | Results before this time (exclusive) will be returned, specified as seconds since the Unix epoch. (optional)

    try:
        # Monitor file translation
        api_response = api_instance.monitor_file_translation(translation_ids=translation_ids, status=status, from_time=from_time, to_time=to_time)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TranslateApi->monitor_file_translation: %s\n" % e)
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
    api_instance = lilt.TranslateApi(api_client)
    translation_ids = 'translation_ids_example' # str | List of translation ids, comma separated (optional)
status = 'status_example' # str | One of the translation statuses - `InProgress`, `Completed`, `Failed`, `ReadyForDownload` (optional)
from_time = 3.4 # float | Results after this time (inclusive) will be returned, specified as seconds since the Unix epoch. (optional)
to_time = 3.4 # float | Results before this time (exclusive) will be returned, specified as seconds since the Unix epoch. (optional)

    try:
        # Monitor file translation
        api_response = api_instance.monitor_file_translation(translation_ids=translation_ids, status=status, from_time=from_time, to_time=to_time)
        pprint(api_response)
    except ApiException as e:
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

[**TranslationInfo**](TranslationInfo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Translation info |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_segment**
> TranslateRegisterResponse register_segment(source, srclang, trglang)

Register a segment

Register a source string for interactive translation. The `source_hash` value that is returned by this request is required by the `prefix` parameter for the translation endpoint. The maximum source length is 5,000 characters. Usage charges apply to this endpoint for production REST API keys.  

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
    api_instance = lilt.TranslateApi(api_client)
    source = 'source_example' # str | A source string to be registered.
srclang = 'srclang_example' # str | An ISO 639-1 language code.
trglang = 'trglang_example' # str | An ISO 639-1 language code.

    try:
        # Register a segment
        api_response = api_instance.register_segment(source, srclang, trglang)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TranslateApi->register_segment: %s\n" % e)
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
    api_instance = lilt.TranslateApi(api_client)
    source = 'source_example' # str | A source string to be registered.
srclang = 'srclang_example' # str | An ISO 639-1 language code.
trglang = 'trglang_example' # str | An ISO 639-1 language code.

    try:
        # Register a segment
        api_response = api_instance.register_segment(source, srclang, trglang)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TranslateApi->register_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| A source string to be registered. | 
 **srclang** | **str**| An ISO 639-1 language code. | 
 **trglang** | **str**| An ISO 639-1 language code. | 

### Return type

[**TranslateRegisterResponse**](TranslateRegisterResponse.md)

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

# **translate_segment**
> TranslationList translate_segment(memory_id, source=source, source_hash=source_hash, prefix=prefix, n=n, rich=rich, tm_matches=tm_matches, project_tags=project_tags)

Translate a segment

Translate a source string.  Setting the `rich` parameter to `true` will change the response format to include additional information about each translation including a model score, word alignments,  and formatting information. The rich format can be seen in the example response on this page.  By default, this endpoint also returns translation memory (TM) fuzzy matches, along with associated scores. Fuzzy matches always appear ahead of machine translation output in the response.  The maximum source length is 5,000 characters.  Usage charges apply to this endpoint for production REST API keys.  

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
    api_instance = lilt.TranslateApi(api_client)
    memory_id = 56 # int | A unique Memory identifier.
source = 'source_example' # str | The source text to be translated. (optional)
source_hash = 56 # int | A source hash code. (optional)
prefix = 'prefix_example' # str | A target prefix. (optional)
n = 1 # int | Return top n translations (deprecated). (optional) (default to 1)
rich = False # bool | Returns rich translation information (e.g., with word alignments). (optional) (default to False)
tm_matches = True # bool | Include translation memory fuzzy matches. (optional) (default to True)
project_tags = False # bool | Project tags. Projects tags in source to target if set to true. (optional) (default to False)

    try:
        # Translate a segment
        api_response = api_instance.translate_segment(memory_id, source=source, source_hash=source_hash, prefix=prefix, n=n, rich=rich, tm_matches=tm_matches, project_tags=project_tags)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TranslateApi->translate_segment: %s\n" % e)
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
    api_instance = lilt.TranslateApi(api_client)
    memory_id = 56 # int | A unique Memory identifier.
source = 'source_example' # str | The source text to be translated. (optional)
source_hash = 56 # int | A source hash code. (optional)
prefix = 'prefix_example' # str | A target prefix. (optional)
n = 1 # int | Return top n translations (deprecated). (optional) (default to 1)
rich = False # bool | Returns rich translation information (e.g., with word alignments). (optional) (default to False)
tm_matches = True # bool | Include translation memory fuzzy matches. (optional) (default to True)
project_tags = False # bool | Project tags. Projects tags in source to target if set to true. (optional) (default to False)

    try:
        # Translate a segment
        api_response = api_instance.translate_segment(memory_id, source=source, source_hash=source_hash, prefix=prefix, n=n, rich=rich, tm_matches=tm_matches, project_tags=project_tags)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TranslateApi->translate_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **memory_id** | **int**| A unique Memory identifier. | 
 **source** | **str**| The source text to be translated. | [optional] 
 **source_hash** | **int**| A source hash code. | [optional] 
 **prefix** | **str**| A target prefix. | [optional] 
 **n** | **int**| Return top n translations (deprecated). | [optional] [default to 1]
 **rich** | **bool**| Returns rich translation information (e.g., with word alignments). | [optional] [default to False]
 **tm_matches** | **bool**| Include translation memory fuzzy matches. | [optional] [default to True]
 **project_tags** | **bool**| Project tags. Projects tags in source to target if set to true. | [optional] [default to False]

### Return type

[**TranslationList**](TranslationList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A TranslationList object. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

