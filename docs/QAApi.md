# lilt.QAApi

All URIs are relative to *https://lilt.com/2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**qa_check**](QAApi.md#qa_check) | **GET** /qa | Perform QA check


# **qa_check**
> QARuleMatches qa_check(target, trglang, source=source, srclang=srclang, memory_id=memory_id)

Perform QA check

Perform QA checks on a target string. Optionally, you can specify a source string for additional bilingual checks, e.g. number consistency. 

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
    api_instance = lilt.QAApi(api_client)
    target = 'target_example' # str | A target string to be checked.
trglang = 'trglang_example' # str | An ISO 639-1 language code.
source = 'source_example' # str | An optional source string. (optional)
srclang = 'srclang_example' # str | An ISO 639-1 language code. (optional)
memory_id = 56 # int | Any custom rules defined for this Memory will also be applied as part of the QA check.  (optional)

    try:
        # Perform QA check
        api_response = api_instance.qa_check(target, trglang, source=source, srclang=srclang, memory_id=memory_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling QAApi->qa_check: %s\n" % e)
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
    api_instance = lilt.QAApi(api_client)
    target = 'target_example' # str | A target string to be checked.
trglang = 'trglang_example' # str | An ISO 639-1 language code.
source = 'source_example' # str | An optional source string. (optional)
srclang = 'srclang_example' # str | An ISO 639-1 language code. (optional)
memory_id = 56 # int | Any custom rules defined for this Memory will also be applied as part of the QA check.  (optional)

    try:
        # Perform QA check
        api_response = api_instance.qa_check(target, trglang, source=source, srclang=srclang, memory_id=memory_id)
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
 **memory_id** | **int**| Any custom rules defined for this Memory will also be applied as part of the QA check.  | [optional] 

### Return type

[**QARuleMatches**](QARuleMatches.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A QARuleMatches object. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

