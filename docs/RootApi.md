# lilt.RootApi

All URIs are relative to *https://lilt.com/2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**root**](RootApi.md#root) | **GET** / | Retrieve the REST API root


# **root**
> ApiRoot root()

Retrieve the REST API root

This resource does not have any attributes. It lists the name of the REST API.  This endpoint can be used to verify REST API keys and to check the availability of the REST API.  

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
    api_instance = lilt.RootApi(api_client)
    
    try:
        # Retrieve the REST API root
        api_response = api_instance.root()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RootApi->root: %s\n" % e)
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
    api_instance = lilt.RootApi(api_client)
    
    try:
        # Retrieve the REST API root
        api_response = api_instance.root()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RootApi->root: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiRoot**](ApiRoot.md)

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

