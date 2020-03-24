# lilt.LanguagesApi

All URIs are relative to *https://lilt.com/2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_languages**](LanguagesApi.md#get_languages) | **GET** /languages | Retrieve supported languages

# **get_languages**
> object get_languages()

Retrieve supported languages

Get a list of supported languages.  

### Example
```python
from __future__ import print_function
import time
import lilt
from lilt.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = lilt.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'# Configure HTTP basic authorization: BasicAuth
configuration = lilt.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = lilt.LanguagesApi(lilt.ApiClient(configuration))

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

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

