# lilt.LexiconApi

All URIs are relative to *https://lilt.com/2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_lexicon**](LexiconApi.md#query_lexicon) | **GET** /lexicon | Query a Lexicon
[**update_lexicon**](LexiconApi.md#update_lexicon) | **POST** /lexicon | Update a Lexicon


# **query_lexicon**
> list[LexiconEntry] query_lexicon(memory_id, srclang, trglang, query, n=n)

Query a Lexicon

Query the Lexicon. The Lexicon is an editable termbase / concordance that is integrated with the Memory.  

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
    api_instance = lilt.LexiconApi(api_client)
    memory_id = 56 # int | A unique Memory identifier.
srclang = 'srclang_example' # str | An ISO 639-1 language code.
trglang = 'trglang_example' # str | An ISO 639-1 language code.
query = 'query_example' # str | The query term.
n = 1 # int | The maximum number of results to return. (optional) (default to 1)

    try:
        # Query a Lexicon
        api_response = api_instance.query_lexicon(memory_id, srclang, trglang, query, n=n)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LexiconApi->query_lexicon: %s\n" % e)
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
    api_instance = lilt.LexiconApi(api_client)
    memory_id = 56 # int | A unique Memory identifier.
srclang = 'srclang_example' # str | An ISO 639-1 language code.
trglang = 'trglang_example' # str | An ISO 639-1 language code.
query = 'query_example' # str | The query term.
n = 1 # int | The maximum number of results to return. (optional) (default to 1)

    try:
        # Query a Lexicon
        api_response = api_instance.query_lexicon(memory_id, srclang, trglang, query, n=n)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LexiconApi->query_lexicon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **memory_id** | **int**| A unique Memory identifier. | 
 **srclang** | **str**| An ISO 639-1 language code. | 
 **trglang** | **str**| An ISO 639-1 language code. | 
 **query** | **str**| The query term. | 
 **n** | **int**| The maximum number of results to return. | [optional] [default to 1]

### Return type

[**list[LexiconEntry]**](LexiconEntry.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of LexiconEntry objects. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_lexicon**
> LexiconUpdateResponse update_lexicon(body)

Update a Lexicon

Update the Lexicon (Termbase as displayed in the ui) with a new term. The maximum source length is 250 characters.  

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
    api_instance = lilt.LexiconApi(api_client)
    body = lilt.LexiconUpdateParameters() # LexiconUpdateParameters | 

    try:
        # Update a Lexicon
        api_response = api_instance.update_lexicon(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LexiconApi->update_lexicon: %s\n" % e)
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
    api_instance = lilt.LexiconApi(api_client)
    body = lilt.LexiconUpdateParameters() # LexiconUpdateParameters | 

    try:
        # Update a Lexicon
        api_response = api_instance.update_lexicon(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LexiconApi->update_lexicon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LexiconUpdateParameters**](LexiconUpdateParameters.md)|  | 

### Return type

[**LexiconUpdateResponse**](LexiconUpdateResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A status object. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

