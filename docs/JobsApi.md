# lilt.JobsApi

All URIs are relative to *https://lilt.com/2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_job**](JobsApi.md#archive_job) | **POST** /jobs/{jobId}/archive | Archive a Job
[**create_job**](JobsApi.md#create_job) | **POST** /jobs | Create a Job
[**delete_job**](JobsApi.md#delete_job) | **DELETE** /jobs/{jobId} | Delete a Job
[**deliver_job**](JobsApi.md#deliver_job) | **POST** /jobs/{jobId}/deliver | Deliver a Job
[**download_job**](JobsApi.md#download_job) | **GET** /jobs/{jobId}/downlod | Download a Job
[**export_job**](JobsApi.md#export_job) | **GET** /jobs/{jobId}/export | Export a Job
[**get_job**](JobsApi.md#get_job) | **GET** /jobs/{jobId} | Retrieve a Job
[**get_job_leverage_stats**](JobsApi.md#get_job_leverage_stats) | **POST** /jobs/{jobId}/stats | Retrieve Job Leverage Stats
[**reactivate_job**](JobsApi.md#reactivate_job) | **POST** /jobs/{jobId}/reactivate | Reactivate a Job
[**retrieve_all_jobs**](JobsApi.md#retrieve_all_jobs) | **GET** /jobs | Retrieve all Jobs
[**unarchive_job**](JobsApi.md#unarchive_job) | **POST** /jobs/{jobId}/unarchive | Unarchive a Job
[**update_job**](JobsApi.md#update_job) | **PUT** /jobs/{jobId} | Update a Job


# **archive_job**
> Job archive_job(job_id)

Archive a Job

Set job to archived, unassign all linguists and archive all projects and documents inside the job.  It will return the archived job.  Example CURL command:  ``` curl -X POST 'https://lilt.com/2/jobs/{id}/archive?key=API_KEY' ```

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
    api_instance = lilt.JobsApi(api_client)
    job_id = 56 # int | A job id.

    try:
        # Archive a Job
        api_response = api_instance.archive_job(job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->archive_job: %s\n" % e)
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
    api_instance = lilt.JobsApi(api_client)
    job_id = 56 # int | A job id.

    try:
        # Archive a Job
        api_response = api_instance.archive_job(job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->archive_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| A job id. | 

### Return type

[**Job**](Job.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A job object. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_job**
> Job create_job(body)

Create a Job

Create a Job. A Job is a collection of Projects. A Job will contain multiple projects, based on the language pair. A Project is associated with exactly one Memory.  Jobs appear in the Jobs dashboard of the web app.  Example CURL command:  ``` curl -X POST 'https://lilt.com/2/jobs?key=API_KEY' \\ --header 'Content-Type: application/json' \\ --data-raw '{   \"name\": \"test job\",   \"fileIds\": [5009, 5010, 5011],   \"due\": \"2022-05-05T10:56:44.985Z\",   \"srcLang\": \"en\",   \"srcLocale\": \"US\",   \"languagePairs\": [       { \"memoryId\": 3121, \"trgLang\": \"de\" },       { \"memoryId\": 2508, \"trgLang\": \"fr\" },       { \"memoryId\": 3037, \"trgLang\": \"zh\" }     ] }' ```  

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
    api_instance = lilt.JobsApi(api_client)
    body = lilt.JobCreateParameters() # JobCreateParameters | 

    try:
        # Create a Job
        api_response = api_instance.create_job(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->create_job: %s\n" % e)
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
    api_instance = lilt.JobsApi(api_client)
    body = lilt.JobCreateParameters() # JobCreateParameters | 

    try:
        # Create a Job
        api_response = api_instance.create_job(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->create_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JobCreateParameters**](JobCreateParameters.md)|  | 

### Return type

[**Job**](Job.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Job object. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job**
> JobDeleteResponse delete_job(job_id)

Delete a Job

Delete a job, deletes all projects and documents in the job, deletes all the segments from all the job's translation memories.  Example CURL command:  ``` curl -X DELETE 'https://lilt.com/2/jobs/{id}?key=API_KEY' ```

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
    api_instance = lilt.JobsApi(api_client)
    job_id = 56 # int | A job id.

    try:
        # Delete a Job
        api_response = api_instance.delete_job(job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->delete_job: %s\n" % e)
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
    api_instance = lilt.JobsApi(api_client)
    job_id = 56 # int | A job id.

    try:
        # Delete a Job
        api_response = api_instance.delete_job(job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->delete_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| A job id. | 

### Return type

[**JobDeleteResponse**](JobDeleteResponse.md)

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

# **deliver_job**
> Job deliver_job(job_id)

Deliver a Job

Set the job state to delivered and set all the projects in the job to done  It will return the delivered job.  Example CURL command:  ``` curl -X POST 'https://lilt.com/2/jobs/{id}/deliver?key=API_KEY' ```

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
    api_instance = lilt.JobsApi(api_client)
    job_id = 56 # int | A job id.

    try:
        # Deliver a Job
        api_response = api_instance.deliver_job(job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->deliver_job: %s\n" % e)
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
    api_instance = lilt.JobsApi(api_client)
    job_id = 56 # int | A job id.

    try:
        # Deliver a Job
        api_response = api_instance.deliver_job(job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->deliver_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| A job id. | 

### Return type

[**Job**](Job.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A job object. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_job**
> download_job(job_id)

Download a Job

Make sure you have exported a job with the same id before using this api.  Downloading files requires the exported job `id` in the param.  Example CURL command:  ``` curl -X GET 'https://lilt.com/2/jobs/{id}/download?key=API_KEY' ```

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
    api_instance = lilt.JobsApi(api_client)
    job_id = 56 # int | A job id.

    try:
        # Download a Job
        api_instance.download_job(job_id)
    except ApiException as e:
        print("Exception when calling JobsApi->download_job: %s\n" % e)
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
    api_instance = lilt.JobsApi(api_client)
    job_id = 56 # int | A job id.

    try:
        # Download a Job
        api_instance.download_job(job_id)
    except ApiException as e:
        print("Exception when calling JobsApi->download_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| A job id. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | zipped file |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_job**
> export_job(job_id, type)

Export a Job

Prepare job files for download. To export translated documents from the job use the query parameter `type=files`:  Example CURL command:  ``` curl -X GET 'https://lilt.com/2/jobs/{id}/export?key=API_KEY&type=files' ```  To export job memories use the query parameter `type=memory`.  The status of the export can be checked by requesting the job `GET /jobs/:jobId`, `job.isProcessing` will be `1` while in progress, `0` when idle and `-2` when the export failed.

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
    api_instance = lilt.JobsApi(api_client)
    job_id = 56 # int | A job id.
type = 'type_example' # str | category for files and memory.

    try:
        # Export a Job
        api_instance.export_job(job_id, type)
    except ApiException as e:
        print("Exception when calling JobsApi->export_job: %s\n" % e)
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
    api_instance = lilt.JobsApi(api_client)
    job_id = 56 # int | A job id.
type = 'type_example' # str | category for files and memory.

    try:
        # Export a Job
        api_instance.export_job(job_id, type)
    except ApiException as e:
        print("Exception when calling JobsApi->export_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| A job id. | 
 **type** | **str**| category for files and memory. | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 status. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job**
> Job get_job(job_id)

Retrieve a Job

Retrieves a job data along with stats. To retrieve a specific job, you will need the job `id` in the url path.  Example CURL command:  ``` curl -X GET 'https://lilt.com/2/jobs/{id}?key=API_KEY' ```

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
    api_instance = lilt.JobsApi(api_client)
    job_id = 56 # int | A job id.

    try:
        # Retrieve a Job
        api_response = api_instance.get_job(job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->get_job: %s\n" % e)
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
    api_instance = lilt.JobsApi(api_client)
    job_id = 56 # int | A job id.

    try:
        # Retrieve a Job
        api_response = api_instance.get_job(job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->get_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| A job id. | 

### Return type

[**Job**](Job.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A job object. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_leverage_stats**
> JobLeverageStats get_job_leverage_stats(job_id)

Retrieve Job Leverage Stats

Get the TM leverage stats for the job (new/exact/fuzzy matches).  Example CURL command:  ``` curl -X POST 'https://lilt.com/2/jobs/{id}/stats?key=API_KEY' ```

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
    api_instance = lilt.JobsApi(api_client)
    job_id = 56 # int | A job id.

    try:
        # Retrieve Job Leverage Stats
        api_response = api_instance.get_job_leverage_stats(job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->get_job_leverage_stats: %s\n" % e)
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
    api_instance = lilt.JobsApi(api_client)
    job_id = 56 # int | A job id.

    try:
        # Retrieve Job Leverage Stats
        api_response = api_instance.get_job_leverage_stats(job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->get_job_leverage_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| A job id. | 

### Return type

[**JobLeverageStats**](JobLeverageStats.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A job leverage stats object. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reactivate_job**
> Job reactivate_job(job_id)

Reactivate a Job

Set the job state to active. Does not change the state of projects associated with the given job.  It will return the reactivated job.  Example CURL command:  ``` curl -X POST 'https://lilt.com/2/jobs/{id}/reactivate?key=API_KEY' ```

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
    api_instance = lilt.JobsApi(api_client)
    job_id = 56 # int | A job id.

    try:
        # Reactivate a Job
        api_response = api_instance.reactivate_job(job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->reactivate_job: %s\n" % e)
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
    api_instance = lilt.JobsApi(api_client)
    job_id = 56 # int | A job id.

    try:
        # Reactivate a Job
        api_response = api_instance.reactivate_job(job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->reactivate_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| A job id. | 

### Return type

[**Job**](Job.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A job object. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all_jobs**
> list[Job] retrieve_all_jobs(is_archived=is_archived, is_delivered=is_delivered, offset=offset, limit=limit)

Retrieve all Jobs

Get all Jobs within a given offset and limit. You can retrieve jobs from your account using the above API.  Example CURL command:  ``` curl -X GET 'https://lilt.com/2/jobs?key=API_KEY&isArchived=false' ```

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
    api_instance = lilt.JobsApi(api_client)
    is_archived = True # bool | Retrieves all jobs that are archived. (optional)
is_delivered = True # bool | Retrieves all jobs that are delivered. (optional)
offset = 56 # int | Return jobs starting at the offset row. If not given the default offset will be 0. (optional)
limit = 56 # int | The maximum number of jobs to be returned. If not given the default limit will be 25. (optional)

    try:
        # Retrieve all Jobs
        api_response = api_instance.retrieve_all_jobs(is_archived=is_archived, is_delivered=is_delivered, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->retrieve_all_jobs: %s\n" % e)
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
    api_instance = lilt.JobsApi(api_client)
    is_archived = True # bool | Retrieves all jobs that are archived. (optional)
is_delivered = True # bool | Retrieves all jobs that are delivered. (optional)
offset = 56 # int | Return jobs starting at the offset row. If not given the default offset will be 0. (optional)
limit = 56 # int | The maximum number of jobs to be returned. If not given the default limit will be 25. (optional)

    try:
        # Retrieve all Jobs
        api_response = api_instance.retrieve_all_jobs(is_archived=is_archived, is_delivered=is_delivered, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->retrieve_all_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_archived** | **bool**| Retrieves all jobs that are archived. | [optional] 
 **is_delivered** | **bool**| Retrieves all jobs that are delivered. | [optional] 
 **offset** | **int**| Return jobs starting at the offset row. If not given the default offset will be 0. | [optional] 
 **limit** | **int**| The maximum number of jobs to be returned. If not given the default limit will be 25. | [optional] 

### Return type

[**list[Job]**](Job.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Job objects. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unarchive_job**
> Job unarchive_job(job_id)

Unarchive a Job

Set job to unarchived, the job will move to active status.  Example CURL command:  ``` curl -X POST 'https://lilt.com/2/jobs/{id}/unarchive?key=API_KEY' ```

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
    api_instance = lilt.JobsApi(api_client)
    job_id = 56 # int | A job id.

    try:
        # Unarchive a Job
        api_response = api_instance.unarchive_job(job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->unarchive_job: %s\n" % e)
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
    api_instance = lilt.JobsApi(api_client)
    job_id = 56 # int | A job id.

    try:
        # Unarchive a Job
        api_response = api_instance.unarchive_job(job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->unarchive_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| A job id. | 

### Return type

[**Job**](Job.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A job object. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_job**
> Job update_job(job_id, body=body)

Update a Job

Updates a job with the new job properties. To update a specific job, you will need the job `id` in the url path.  You can update job's name and due date by passing the property and new value in the body.  Example CURL command:  ``` curl -X PUT 'https://lilt.com/2/jobs/{id}?key=API_KEY' \\ --header 'Content-Type: application/json' \\ --data-raw '{   \"name\": \"test job\",   \"due\": \"2022-05-05T10:56:44.985Z\" }' ```

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
    api_instance = lilt.JobsApi(api_client)
    job_id = 56 # int | A job id.
body = lilt.JobUpdateParameters() # JobUpdateParameters |  (optional)

    try:
        # Update a Job
        api_response = api_instance.update_job(job_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->update_job: %s\n" % e)
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
    api_instance = lilt.JobsApi(api_client)
    job_id = 56 # int | A job id.
body = lilt.JobUpdateParameters() # JobUpdateParameters |  (optional)

    try:
        # Update a Job
        api_response = api_instance.update_job(job_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->update_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| A job id. | 
 **body** | [**JobUpdateParameters**](JobUpdateParameters.md)|  | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A job object. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

