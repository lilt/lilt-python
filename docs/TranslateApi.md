# lilt.TranslateApi

All URIs are relative to *https://lilt.com/2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**register_segment**](TranslateApi.md#register_segment) | **GET** /translate/register | Register a segment
[**translate_segment**](TranslateApi.md#translate_segment) | **GET** /translate | Translate a segment


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
configuration = lilt.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
configuration = lilt.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://lilt.com/2
configuration.host = "https://lilt.com/2"

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
configuration = lilt.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
configuration = lilt.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://lilt.com/2
configuration.host = "https://lilt.com/2"

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
> TranslationList translate_segment(memory_id, source=source, source_hash=source_hash, prefix=prefix, rich=rich, tm_matches=tm_matches, project_tags=project_tags)

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
configuration = lilt.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
configuration = lilt.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://lilt.com/2
configuration.host = "https://lilt.com/2"

# Enter a context with an instance of the API client
with lilt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lilt.TranslateApi(api_client)
    memory_id = 56 # int | A unique Memory identifier.
source = 'source_example' # str | The source text to be translated. (optional)
source_hash = 56 # int | A source hash code. (optional)
prefix = 'prefix_example' # str | A target prefix. (optional)
rich = False # bool | Returns rich translation information (e.g., with word alignments). (optional) (default to False)
tm_matches = True # bool | Include translation memory fuzzy matches. (optional) (default to True)
project_tags = False # bool | Project tags. Projects tags in source to target if set to true. (optional) (default to False)

    try:
        # Translate a segment
        api_response = api_instance.translate_segment(memory_id, source=source, source_hash=source_hash, prefix=prefix, rich=rich, tm_matches=tm_matches, project_tags=project_tags)
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
configuration = lilt.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
configuration = lilt.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://lilt.com/2
configuration.host = "https://lilt.com/2"

# Enter a context with an instance of the API client
with lilt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lilt.TranslateApi(api_client)
    memory_id = 56 # int | A unique Memory identifier.
source = 'source_example' # str | The source text to be translated. (optional)
source_hash = 56 # int | A source hash code. (optional)
prefix = 'prefix_example' # str | A target prefix. (optional)
rich = False # bool | Returns rich translation information (e.g., with word alignments). (optional) (default to False)
tm_matches = True # bool | Include translation memory fuzzy matches. (optional) (default to True)
project_tags = False # bool | Project tags. Projects tags in source to target if set to true. (optional) (default to False)

    try:
        # Translate a segment
        api_response = api_instance.translate_segment(memory_id, source=source, source_hash=source_hash, prefix=prefix, rich=rich, tm_matches=tm_matches, project_tags=project_tags)
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

