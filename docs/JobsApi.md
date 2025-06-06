# lilt.JobsApi

All URIs are relative to *https://api.lilt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_job**](JobsApi.md#archive_job) | **POST** /v2/jobs/{jobId}/archive | Archive a Job
[**create_job**](JobsApi.md#create_job) | **POST** /v2/jobs | Create a Job
[**delete_job**](JobsApi.md#delete_job) | **DELETE** /v2/jobs/{jobId} | Delete a Job
[**deliver_job**](JobsApi.md#deliver_job) | **POST** /v2/jobs/{jobId}/deliver | Deliver a Job
[**download_job**](JobsApi.md#download_job) | **GET** /v2/jobs/{jobId}/download | Download a Job
[**export_job**](JobsApi.md#export_job) | **GET** /v2/jobs/{jobId}/export | Export a Job
[**get_job**](JobsApi.md#get_job) | **GET** /v2/jobs/{jobId} | Retrieve a Job
[**get_job_leverage_stats**](JobsApi.md#get_job_leverage_stats) | **POST** /v2/jobs/{jobId}/stats | Retrieve Job Leverage Stats
[**reactivate_job**](JobsApi.md#reactivate_job) | **POST** /v2/jobs/{jobId}/reactivate | Reactivate a Job
[**retrieve_all_jobs**](JobsApi.md#retrieve_all_jobs) | **GET** /v2/jobs | Retrieve all Jobs
[**unarchive_job**](JobsApi.md#unarchive_job) | **POST** /v2/jobs/{jobId}/unarchive | Unarchive a Job
[**update_job**](JobsApi.md#update_job) | **PUT** /v2/jobs/{jobId} | Update a Job


# **archive_job**
> Job archive_job(job_id)

Archive a Job

Set job to archived, unassign all linguists and archive all projects and documents inside the job.

It will return the archived job.

Example CURL command:

```bash
curl -X POST 'https://api.lilt.com/v2/jobs/{id}/archive?key=API_KEY'
```

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.job import Job
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
    api_instance = lilt.JobsApi(api_client)
    job_id = 56 # int | A job id.

    try:
        # Archive a Job
        api_response = api_instance.archive_job(job_id)
        print("The response of JobsApi->archive_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->archive_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| A job id. | 

### Return type

[**Job**](Job.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A job object. |  -  |
**401** | Unauthorized |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_job**
> Job create_job(body)

Create a Job

Create a Job. A Job is a collection of Projects.
A Job will contain multiple projects, based on the language pair.
A Project is associated with exactly one Memory.

Jobs appear in the Jobs dashboard of the web app.

Example CURL command:

```bash
curl -X POST 'https://api.lilt.com/v2/jobs?key=API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "name": "test job",
  "fileIds": [5009, 5010, 5011],
  "due": "2022-05-05T10:56:44.985Z",
  "srcLang": "en",
  "srcLocale": "US",
  "languagePairs": [
      { "memoryId": 3121, "trgLang": "de" },
      { "memoryId": 2508, "trgLang": "fr" },
      { "memoryId": 3037, "trgLang": "zh" }
    ]
}'
```



### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.job import Job
from lilt.models.job_create_parameters import JobCreateParameters
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
    api_instance = lilt.JobsApi(api_client)
    body = lilt.JobCreateParameters() # JobCreateParameters | The Job resource to create.

    try:
        # Create a Job
        api_response = api_instance.create_job(body)
        print("The response of JobsApi->create_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->create_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JobCreateParameters**](JobCreateParameters.md)| The Job resource to create. | 

### Return type

[**Job**](Job.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/octet-stream, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Job object. |  -  |
**401** | Unauthorized |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job**
> JobDeleteResponse delete_job(job_id)

Delete a Job

Delete a job, deletes all projects and documents in the job, deletes all the segments from all the job's translation memories.

Example CURL command:

```bash
curl -X DELETE 'https://api.lilt.com/v2/jobs/{id}?key=API_KEY'
```

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.job_delete_response import JobDeleteResponse
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
    api_instance = lilt.JobsApi(api_client)
    job_id = 56 # int | A job id.

    try:
        # Delete a Job
        api_response = api_instance.delete_job(job_id)
        print("The response of JobsApi->delete_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->delete_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| A job id. | 

### Return type

[**JobDeleteResponse**](JobDeleteResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A status object. |  -  |
**401** | Unauthorized |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deliver_job**
> Job deliver_job(job_id)

Deliver a Job

Set the job state to delivered and set all the projects in the job to done

It will return the delivered job.

Example CURL command:

```bash
curl -X POST 'https://api.lilt.com/v2/jobs/{id}/deliver?key=API_KEY'
```

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.job import Job
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
    api_instance = lilt.JobsApi(api_client)
    job_id = 56 # int | A job id.

    try:
        # Deliver a Job
        api_response = api_instance.deliver_job(job_id)
        print("The response of JobsApi->deliver_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->deliver_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| A job id. | 

### Return type

[**Job**](Job.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A job object. |  -  |
**401** | Unauthorized |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_job**
> bytearray download_job(job_id)

Download a Job

Make sure you have exported a job with the same id before using this api.

Downloading files requires the exported job `id` in the param.

Example CURL command:

```bash
curl -X GET 'https://api.lilt.com/v2/jobs/{id}/download?key=API_KEY'
```

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
    api_instance = lilt.JobsApi(api_client)
    job_id = 56 # int | A job id.

    try:
        # Download a Job
        api_response = api_instance.download_job(job_id)
        print("The response of JobsApi->download_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->download_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| A job id. | 

### Return type

**bytearray**

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | zipped file |  -  |
**401** | Unauthorized |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_job**
> export_job(job_id, type)

Export a Job

Prepare job files for download.
To export translated documents from the job use the query parameter `type=files`:

Example CURL command:

```bash
curl -X GET 'https://api.lilt.com/v2/jobs/{id}/export?key=API_KEY&type=files'
```

To export job memories use the query parameter `type=memory`.

The status of the export can be checked by requesting the job `GET /jobs/:jobId`, `job.isProcessing` will be `1` while in progress,
`0` when idle and `-2` when the export failed.

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
    api_instance = lilt.JobsApi(api_client)
    job_id = 56 # int | A job id.
    type = 'type_example' # str | category for files and memory.

    try:
        # Export a Job
        api_instance.export_job(job_id, type)
    except Exception as e:
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

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 status. |  -  |
**401** | Unauthorized |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job**
> Job get_job(job_id)

Retrieve a Job

Retrieves a job data along with stats. To retrieve a specific job, you will need the job `id` in the url path.

Example CURL command:

```bash
curl -X GET 'https://api.lilt.com/v2/jobs/{id}?key=API_KEY'
```

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.job import Job
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
    api_instance = lilt.JobsApi(api_client)
    job_id = 56 # int | A job id.

    try:
        # Retrieve a Job
        api_response = api_instance.get_job(job_id)
        print("The response of JobsApi->get_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| A job id. | 

### Return type

[**Job**](Job.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A job object. |  -  |
**401** | Unauthorized |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_leverage_stats**
> JobLeverageStats get_job_leverage_stats(job_id)

Retrieve Job Leverage Stats

Get the TM leverage stats for the job (new/exact/fuzzy matches).

Example CURL command:

```bash
curl -X POST 'https://api.lilt.com/v2/jobs/{id}/stats?key=API_KEY'
```

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.job_leverage_stats import JobLeverageStats
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
    api_instance = lilt.JobsApi(api_client)
    job_id = 56 # int | A job id.

    try:
        # Retrieve Job Leverage Stats
        api_response = api_instance.get_job_leverage_stats(job_id)
        print("The response of JobsApi->get_job_leverage_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_job_leverage_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| A job id. | 

### Return type

[**JobLeverageStats**](JobLeverageStats.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A job leverage stats object. |  -  |
**401** | Unauthorized |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reactivate_job**
> Job reactivate_job(job_id)

Reactivate a Job

Set the job state to active. Does not change the state of projects associated with the given job.

It will return the reactivated job.

Example CURL command:

```bash
curl -X POST 'https://api.lilt.com/v2/jobs/{id}/reactivate?key=API_KEY'
```

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.job import Job
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
    api_instance = lilt.JobsApi(api_client)
    job_id = 56 # int | A job id.

    try:
        # Reactivate a Job
        api_response = api_instance.reactivate_job(job_id)
        print("The response of JobsApi->reactivate_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->reactivate_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| A job id. | 

### Return type

[**Job**](Job.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A job object. |  -  |
**401** | Unauthorized |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all_jobs**
> List[Job] retrieve_all_jobs(is_archived=is_archived, is_delivered=is_delivered, offset=offset, limit=limit)

Retrieve all Jobs

Get all Jobs within a given offset and limit. You can retrieve jobs from your account using the above API.

Example CURL command:

```bash
curl -X GET 'https://api.lilt.com/v2/jobs?key=API_KEY&isArchived=false'
```

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.job import Job
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
    api_instance = lilt.JobsApi(api_client)
    is_archived = True # bool | Retrieves all jobs that are archived. (optional)
    is_delivered = True # bool | Retrieves all jobs that are delivered. (optional)
    offset = 56 # int | Return jobs starting at the offset row. If not given the default offset will be 0. (optional)
    limit = 56 # int | The maximum number of jobs to be returned. If not given the default limit will be 25. (optional)

    try:
        # Retrieve all Jobs
        api_response = api_instance.retrieve_all_jobs(is_archived=is_archived, is_delivered=is_delivered, offset=offset, limit=limit)
        print("The response of JobsApi->retrieve_all_jobs:\n")
        pprint(api_response)
    except Exception as e:
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

[**List[Job]**](Job.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Job objects. |  -  |
**401** | Unauthorized |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unarchive_job**
> Job unarchive_job(job_id)

Unarchive a Job

Set job to unarchived, the job will move to active status.

Example CURL command:

```bash
curl -X POST 'https://api.lilt.com/v2/jobs/{id}/unarchive?key=API_KEY'
```

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.job import Job
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
    api_instance = lilt.JobsApi(api_client)
    job_id = 56 # int | A job id.

    try:
        # Unarchive a Job
        api_response = api_instance.unarchive_job(job_id)
        print("The response of JobsApi->unarchive_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->unarchive_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| A job id. | 

### Return type

[**Job**](Job.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A job object. |  -  |
**401** | Unauthorized |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_job**
> Job update_job(job_id, body=body)

Update a Job

Updates a job with the new job properties. To update a specific job, you will need the job `id` in the url path.

You can update job's name and due date by passing the property and new value in the body.

Example CURL command:

```bash
curl -X PUT 'https://api.lilt.com/v2/jobs/{id}?key=API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "name": "test job",
  "due": "2022-05-05T10:56:44.985Z"
}'
```

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.job import Job
from lilt.models.job_update_parameters import JobUpdateParameters
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
    api_instance = lilt.JobsApi(api_client)
    job_id = 56 # int | A job id.
    body = lilt.JobUpdateParameters() # JobUpdateParameters | The Job resource to update. (optional)

    try:
        # Update a Job
        api_response = api_instance.update_job(job_id, body=body)
        print("The response of JobsApi->update_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->update_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **int**| A job id. | 
 **body** | [**JobUpdateParameters**](JobUpdateParameters.md)| The Job resource to update. | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/octet-stream, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A job object. |  -  |
**401** | Unauthorized |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

