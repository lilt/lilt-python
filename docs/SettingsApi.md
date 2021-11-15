# lilt.SettingsApi

All URIs are relative to *https://lilt.com/2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_organization_settings**](SettingsApi.md#get_organization_settings) | **GET** /settings/organization | Get organization-level settings
[**get_project_settings**](SettingsApi.md#get_project_settings) | **GET** /settings/project/{projectId} | Get settings for a project
[**get_user_settings**](SettingsApi.md#get_user_settings) | **GET** /settings/user | Get settings for the authenticated  user
[**upsert_setting**](SettingsApi.md#upsert_setting) | **POST** /settings | Update or create a setting


# **get_organization_settings**
> dict(str, Setting) get_organization_settings()

Get organization-level settings

Get the organization-level settings for the active users organization  Example CURL:  ``` curl --location --request GET 'https://lilt.com/2/settings/organization?key=<API_KEY>' \\ ```  

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
    api_instance = lilt.SettingsApi(api_client)
    
    try:
        # Get organization-level settings
        api_response = api_instance.get_organization_settings()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SettingsApi->get_organization_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**dict(str, Setting)**](Setting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Organization settings dictionary. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_settings**
> dict(str, Setting) get_project_settings(project_id)

Get settings for a project

Get the settings as applied to a specific project. Active settings will combine project-level settings, organization-level settings and fallback to setting default values.  Example CURL:  ``` curl --location --request GET 'https://lilt.com/2/settings/project/123?key=<API_KEY>' \\ ```  

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
    api_instance = lilt.SettingsApi(api_client)
    project_id = 56 # int | A project id.

    try:
        # Get settings for a project
        api_response = api_instance.get_project_settings(project_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SettingsApi->get_project_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| A project id. | 

### Return type

[**dict(str, Setting)**](Setting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project settings dictionary. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_settings**
> dict(str, Setting) get_user_settings()

Get settings for the authenticated  user

Get the active settings applied to the authenticated user.  Example CURL:  ``` curl --location --request GET 'https://lilt.com/2/settings/user?key=<API_KEY>' \\ ```  

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
    api_instance = lilt.SettingsApi(api_client)
    
    try:
        # Get settings for the authenticated  user
        api_response = api_instance.get_user_settings()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SettingsApi->get_user_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**dict(str, Setting)**](Setting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Settings dictionary. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_setting**
> SettingUpsertResponse upsert_setting(body=body)

Update or create a setting

Create or update the value for the given setting and setting scope.  Example CURL to set an organization-level setting:  ``` curl --location --request POST 'https://lilt.com/2/settings?key=<API_KEY>' \\ --header 'Content-Type: application/json' \\ --data-raw '{     \"settingName\": \"requireBatchQaTranslator\",     \"value\": false,     \"organizationId\": 285,     \"scope\": \"Organization\" }' ```  

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
    api_instance = lilt.SettingsApi(api_client)
    body = lilt.SettingUpsertBody() # SettingUpsertBody |  (optional)

    try:
        # Update or create a setting
        api_response = api_instance.upsert_setting(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SettingsApi->upsert_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SettingUpsertBody**](SettingUpsertBody.md)|  | [optional] 

### Return type

[**SettingUpsertResponse**](SettingUpsertResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated settings object and updated active settings. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

