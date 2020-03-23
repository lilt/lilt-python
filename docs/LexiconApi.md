# pylilt.LexiconApi

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
api_instance = pylilt.LexiconApi(pylilt.ApiClient(configuration))
memory_id = 56 # int | A unique Memory identifier.
srclang = 'srclang_example' # str | An ISO 639-1 language code.
trglang = 'trglang_example' # str | An ISO 639-1 language code.
query = 'query_example' # str | The query term.
n = 56 # int | The maximum number of results to return. (optional)

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
 **n** | **int**| The maximum number of results to return. | [optional] 

### Return type

[**list[LexiconEntry]**](LexiconEntry.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_lexicon**
> object update_lexicon(body)

Update a Lexicon

Update the Lexicon (Termbase as displayed in the ui) with a new term. The maximum source length is 250 characters.  

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
api_instance = pylilt.LexiconApi(pylilt.ApiClient(configuration))
body = NULL # object | The lexicon entry.

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
 **body** | [**object**](object.md)| The lexicon entry. | 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

