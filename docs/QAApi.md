# pylilt.QAApi

All URIs are relative to *https://lilt.com/2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**qa_check**](QAApi.md#qa_check) | **GET** /qa | Perform QA check

# **qa_check**
> QARuleMatches qa_check(target, trglang, source=source, srclang=srclang)

Perform QA check

Perform QA checks on a target string. Optionally, you can specify a source string for additional bilingual checks, e.g. number consistency. 

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
api_instance = pylilt.QAApi(pylilt.ApiClient(configuration))
target = 'target_example' # str | A target string to be checked.
trglang = 'trglang_example' # str | An ISO 639-1 language code.
source = 'source_example' # str | An optional source string. (optional)
srclang = 'srclang_example' # str | An ISO 639-1 language code. (optional)

try:
    # Perform QA check
    api_response = api_instance.qa_check(target, trglang, source=source, srclang=srclang)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QAApi->qa_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target** | **str**| A target string to be checked. | 
 **trglang** | **str**| An ISO 639-1 language code. | 
 **source** | **str**| An optional source string. | [optional] 
 **srclang** | **str**| An ISO 639-1 language code. | [optional] 

### Return type

[**QARuleMatches**](QARuleMatches.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

