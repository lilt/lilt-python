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


# Enter a context with an instance of the API client
with lilt.ApiClient() as api_client:
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object listing supported languages and their corresponding locales. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

