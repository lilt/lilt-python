# lilt.LanguagesApi

All URIs are relative to *https://lilt.com/2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_languages**](LanguagesApi.md#get_languages) | **GET** /languages | Retrieve supported languages


# **get_languages**
> LanguagesResponse get_languages()

Retrieve supported languages

Get a list of supported languages.  

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
    api_instance = lilt.LanguagesApi(api_client)
    
    try:
        # Retrieve supported languages
        api_response = api_instance.get_languages()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LanguagesApi->get_languages: %s\n" % e)
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
    api_instance = lilt.LanguagesApi(api_client)
    
    try:
        # Retrieve supported languages
        api_response = api_instance.get_languages()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LanguagesApi->get_languages: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LanguagesResponse**](LanguagesResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object listing supported languages and their corresponding locales. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

