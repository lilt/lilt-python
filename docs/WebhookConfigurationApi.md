# lilt.WebhookConfigurationApi

All URIs are relative to *https://api.lilt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**services_configuration_api_webhooks_delete**](WebhookConfigurationApi.md#services_configuration_api_webhooks_delete) | **DELETE** /v3/connectors/configuration/webhooks/{id} | Delete a specific Webhook Configuration by ID.
[**webhooks_create**](WebhookConfigurationApi.md#webhooks_create) | **POST** /v3/connectors/configuration/webhooks | Creates a new Webhook Configuration
[**webhooks_get**](WebhookConfigurationApi.md#webhooks_get) | **GET** /v3/connectors/configuration/webhooks/{id} | Retrieve a specific Webhook Configuration by ID.
[**webhooks_get_many**](WebhookConfigurationApi.md#webhooks_get_many) | **GET** /v3/connectors/configuration/webhooks | Retrieve a list of Webhook Configurations.
[**webhooks_update**](WebhookConfigurationApi.md#webhooks_update) | **PUT** /v3/connectors/configuration/webhooks/{id} | Update a specific Webhook Configuration by ID.


# **services_configuration_api_webhooks_delete**
> services_configuration_api_webhooks_delete(id)

Delete a specific Webhook Configuration by ID.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.lilt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = lilt.Configuration(
    host = "https://api.lilt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = lilt.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with lilt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lilt.WebhookConfigurationApi(api_client)
    id = 12345 # int | The Webhook Configuration ID.

    try:
        # Delete a specific Webhook Configuration by ID.
        api_instance.services_configuration_api_webhooks_delete(id)
    except Exception as e:
        print("Exception when calling WebhookConfigurationApi->services_configuration_api_webhooks_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Webhook Configuration ID. | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Upon success a response with an empty body is returned. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_create**
> WebhookResponse webhooks_create(create_webhook_options)

Creates a new Webhook Configuration

Creates a new webhook configuration for your LILT organization.


### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.create_webhook_options import CreateWebhookOptions
from lilt.models.webhook_response import WebhookResponse
from lilt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.lilt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = lilt.Configuration(
    host = "https://api.lilt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = lilt.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with lilt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lilt.WebhookConfigurationApi(api_client)
    create_webhook_options = lilt.CreateWebhookOptions() # CreateWebhookOptions | 

    try:
        # Creates a new Webhook Configuration
        api_response = api_instance.webhooks_create(create_webhook_options)
        print("The response of WebhookConfigurationApi->webhooks_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookConfigurationApi->webhooks_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_webhook_options** | [**CreateWebhookOptions**](CreateWebhookOptions.md)|  | 

### Return type

[**WebhookResponse**](WebhookResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the newly created webhook configuration. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_get**
> WebhookResponse webhooks_get(id)

Retrieve a specific Webhook Configuration by ID.

Retrieves a specific webhook configuration by its ID.
Deleted webhook configurations are not returned.


### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.webhook_response import WebhookResponse
from lilt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.lilt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = lilt.Configuration(
    host = "https://api.lilt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = lilt.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with lilt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lilt.WebhookConfigurationApi(api_client)
    id = 12345 # int | The Webhook Configuration ID.

    try:
        # Retrieve a specific Webhook Configuration by ID.
        api_response = api_instance.webhooks_get(id)
        print("The response of WebhookConfigurationApi->webhooks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookConfigurationApi->webhooks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Webhook Configuration ID. | 

### Return type

[**WebhookResponse**](WebhookResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the webhook configuration. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_get_many**
> List[WebhookResponse] webhooks_get_many()

Retrieve a list of Webhook Configurations.

Retrieves a list of webhook configurations available to your LILT organization.
Use this to manage your webhook configurations.


### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.webhook_response import WebhookResponse
from lilt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.lilt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = lilt.Configuration(
    host = "https://api.lilt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = lilt.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with lilt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lilt.WebhookConfigurationApi(api_client)

    try:
        # Retrieve a list of Webhook Configurations.
        api_response = api_instance.webhooks_get_many()
        print("The response of WebhookConfigurationApi->webhooks_get_many:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookConfigurationApi->webhooks_get_many: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[WebhookResponse]**](WebhookResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The webhook configurations response. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_update**
> WebhookResponse webhooks_update(id, webhooks_update_request)

Update a specific Webhook Configuration by ID.

Updates a specific webhook configuration by its ID.
Only the fields that are provided in the request body will be updated.


### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.webhook_response import WebhookResponse
from lilt.models.webhooks_update_request import WebhooksUpdateRequest
from lilt.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.lilt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = lilt.Configuration(
    host = "https://api.lilt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = lilt.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with lilt.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lilt.WebhookConfigurationApi(api_client)
    id = 12345 # int | The Webhook Configuration ID.
    webhooks_update_request = lilt.WebhooksUpdateRequest() # WebhooksUpdateRequest | 

    try:
        # Update a specific Webhook Configuration by ID.
        api_response = api_instance.webhooks_update(id, webhooks_update_request)
        print("The response of WebhookConfigurationApi->webhooks_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookConfigurationApi->webhooks_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Webhook Configuration ID. | 
 **webhooks_update_request** | [**WebhooksUpdateRequest**](WebhooksUpdateRequest.md)|  | 

### Return type

[**WebhookResponse**](WebhookResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the updated webhook configuration. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

