# lilt.ConverterConfigApi

All URIs are relative to *https://lilt.com/2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_converter_config**](ConverterConfigApi.md#add_converter_config) | **PUT** /configs/converter | Add Converter Config
[**delete_converter_config**](ConverterConfigApi.md#delete_converter_config) | **DELETE** /configs/converter/{configId} | Delete Converter Config
[**delete_filter_mapping**](ConverterConfigApi.md#delete_filter_mapping) | **DELETE** /configs/converter/{configId}/{fileExtension} | Delete Filter Mapping
[**edit_filter_mapping**](ConverterConfigApi.md#edit_filter_mapping) | **PUT** /configs/converter/{configId}/{fileExtension} | Add Filter Mapping
[**get_converter_config_by_id**](ConverterConfigApi.md#get_converter_config_by_id) | **GET** /configs/converter/{configId} | Fetch Converter Config by Id
[**get_converter_configs**](ConverterConfigApi.md#get_converter_configs) | **GET** /configs/converter | List Converter Configs


# **add_converter_config**
> ConverterConfigUpdateResponse add_converter_config(organization_id, body=body)

Add Converter Config

Add a file filter configuration for your Organization. 

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
    api_instance = lilt.ConverterConfigApi(api_client)
    organization_id = 56 # int | A unique Organization identifier.
body = lilt.CreateConverterConfigParameters() # CreateConverterConfigParameters |  (optional)

    try:
        # Add Converter Config
        api_response = api_instance.add_converter_config(organization_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConverterConfigApi->add_converter_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| A unique Organization identifier. | 
 **body** | [**CreateConverterConfigParameters**](CreateConverterConfigParameters.md)|  | [optional] 

### Return type

[**ConverterConfigUpdateResponse**](ConverterConfigUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The config id of the configuration created. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_converter_config**
> ConverterConfigUpdateResponse delete_converter_config(config_id)

Delete Converter Config

Delete a file filter configuration by id. 

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
    api_instance = lilt.ConverterConfigApi(api_client)
    config_id = 56 # int | A unique configuration identifier.

    try:
        # Delete Converter Config
        api_response = api_instance.delete_converter_config(config_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConverterConfigApi->delete_converter_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **int**| A unique configuration identifier. | 

### Return type

[**ConverterConfigUpdateResponse**](ConverterConfigUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The config id of the configuration deleted. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_filter_mapping**
> dict(str, str) delete_filter_mapping(config_id, file_extension)

Delete Filter Mapping

Delete a file filter mapping by id and file extension. 

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
    api_instance = lilt.ConverterConfigApi(api_client)
    config_id = 56 # int | A unique configuration identifier.
file_extension = 'file_extension_example' # str | A file extension to delete.

    try:
        # Delete Filter Mapping
        api_response = api_instance.delete_filter_mapping(config_id, file_extension)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConverterConfigApi->delete_filter_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **int**| A unique configuration identifier. | 
 **file_extension** | **str**| A file extension to delete. | 

### Return type

**dict(str, str)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A map of config id to string escaped config json. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_filter_mapping**
> dict(str, str) edit_filter_mapping(config_id, file_extension, body=body)

Add Filter Mapping

Add a specific filter mapping to your file filter configuration 

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
    api_instance = lilt.ConverterConfigApi(api_client)
    config_id = 56 # int | A unique configuration identifier.
file_extension = 'file_extension_example' # str | A file extension for the filter mapping.
body = lilt.EditFilterMappingParameters() # EditFilterMappingParameters |  (optional)

    try:
        # Add Filter Mapping
        api_response = api_instance.edit_filter_mapping(config_id, file_extension, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConverterConfigApi->edit_filter_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **int**| A unique configuration identifier. | 
 **file_extension** | **str**| A file extension for the filter mapping. | 
 **body** | [**EditFilterMappingParameters**](EditFilterMappingParameters.md)|  | [optional] 

### Return type

**dict(str, str)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A map of config id to string escaped config json. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_converter_config_by_id**
> dict(str, str) get_converter_config_by_id(config_id)

Fetch Converter Config by Id

Fetch a file filter configuration by id. 

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
    api_instance = lilt.ConverterConfigApi(api_client)
    config_id = 56 # int | A unique configuration identifier.

    try:
        # Fetch Converter Config by Id
        api_response = api_instance.get_converter_config_by_id(config_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConverterConfigApi->get_converter_config_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **int**| A unique configuration identifier. | 

### Return type

**dict(str, str)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A map of config id to string escaped config json. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_converter_configs**
> dict(str, str) get_converter_configs(organization_id)

List Converter Configs

List all file filter configurations for your Organization. 

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
    api_instance = lilt.ConverterConfigApi(api_client)
    organization_id = 56 # int | A unique Organization identifier.

    try:
        # List Converter Configs
        api_response = api_instance.get_converter_configs(organization_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConverterConfigApi->get_converter_configs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| A unique Organization identifier. | 

### Return type

**dict(str, str)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A map of config id to string escaped config json. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

