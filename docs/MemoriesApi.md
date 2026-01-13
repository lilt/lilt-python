# lilt.MemoriesApi

All URIs are relative to *https://api.lilt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_memory**](MemoriesApi.md#create_memory) | **POST** /v2/memories | Create a Memory
[**delete_memory**](MemoriesApi.md#delete_memory) | **DELETE** /v2/memories | Delete a Memory
[**delete_segment_from_memory**](MemoriesApi.md#delete_segment_from_memory) | **DELETE** /v2/memories/segment | Delete a segment from a memory.
[**download_termbase**](MemoriesApi.md#download_termbase) | **GET** /v2/memories/termbase/download | Termbase download for a Memory
[**export_termbase**](MemoriesApi.md#export_termbase) | **POST** /v2/memories/termbase/export | Termbase export for a Memory
[**get_memory**](MemoriesApi.md#get_memory) | **GET** /v2/memories | Retrieve a Memory
[**import_memory_file**](MemoriesApi.md#import_memory_file) | **POST** /v2/memories/import | File import for a Memory
[**query_memory**](MemoriesApi.md#query_memory) | **GET** /v2/memories/query | Query a Memory
[**update_memory**](MemoriesApi.md#update_memory) | **PUT** /v2/memories | Update the name of a Memory


# **create_memory**
> Memory create_memory(body)

Create a Memory

Create a new Memory. A Memory is a container that collects source/target
sentences for a specific language pair (e.g., English>French). The data
in the Memory is used to train the MT system, populate the TM, and
update the lexicon. Memories are private to your account - the data is
not shared across users - unless you explicitly share a Memory with your
team (via web app only).

<a href="/kb/introduction-to-lilt-translation" target=_blank>Refer
to our KB</a> for a more detailed description.



### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.memory import Memory
from lilt.models.memory_create_parameters import MemoryCreateParameters
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
    api_instance = lilt.MemoriesApi(api_client)
    body = lilt.MemoryCreateParameters() # MemoryCreateParameters | The Memory resource to create.

    try:
        # Create a Memory
        api_response = api_instance.create_memory(body)
        print("The response of MemoriesApi->create_memory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoriesApi->create_memory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MemoryCreateParameters**](MemoryCreateParameters.md)| The Memory resource to create. | 

### Return type

[**Memory**](Memory.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/octet-stream, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Memory object. |  -  |
**401** | Unauthorized |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_memory**
> MemoryDeleteResponse delete_memory(id)

Delete a Memory

Delete a Memory.


### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.memory_delete_response import MemoryDeleteResponse
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
    api_instance = lilt.MemoriesApi(api_client)
    id = 56 # int | A unique Memory identifier.

    try:
        # Delete a Memory
        api_response = api_instance.delete_memory(id)
        print("The response of MemoriesApi->delete_memory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoriesApi->delete_memory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique Memory identifier. | 

### Return type

[**MemoryDeleteResponse**](MemoryDeleteResponse.md)

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

# **delete_segment_from_memory**
> DeleteSegmentFromMemoryResponse delete_segment_from_memory(id, segment_id)

Delete a segment from a memory.

Delete a segment from a memory.

```bash
  curl -X DELETE https://api.lilt.com/v2/memories/segment?key=API_KEY&id=ID&segment_id=$SEGMENT_ID
```


### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.delete_segment_from_memory_response import DeleteSegmentFromMemoryResponse
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
    api_instance = lilt.MemoriesApi(api_client)
    id = 56 # int | A unique Memory identifier.
    segment_id = 56 # int | A unique Segment identifier.

    try:
        # Delete a segment from a memory.
        api_response = api_instance.delete_segment_from_memory(id, segment_id)
        print("The response of MemoriesApi->delete_segment_from_memory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoriesApi->delete_segment_from_memory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique Memory identifier. | 
 **segment_id** | **int**| A unique Segment identifier. | 

### Return type

[**DeleteSegmentFromMemoryResponse**](DeleteSegmentFromMemoryResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A success resposne. |  -  |
**401** | Unauthorized |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_termbase**
> bytearray download_termbase(id)

Termbase download for a Memory

Downloads the termbase export for the given memory as a CSV file.

Ensure you first call the `/2/memories/termbase/export` endpoint to
start the export process before you try to download it.

```bash
  curl -X GET https://api.lilt.com/v2/memories/termbase/download?key=API_KEY&id=ID
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
    api_instance = lilt.MemoriesApi(api_client)
    id = 56 # int | A unique Memory identifier.

    try:
        # Termbase download for a Memory
        api_response = api_instance.download_termbase(id)
        print("The response of MemoriesApi->download_termbase:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoriesApi->download_termbase: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique Memory identifier. | 

### Return type

**bytearray**

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A file. |  -  |
**401** | Unauthorized |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_termbase**
> TermbaseExportResponse export_termbase(id)

Termbase export for a Memory

Exports the termbase entries for the given memory into a CSV file.

Calling this endpoint will begin the export process in the background.
Check that the processing is complete by polling the `GET /2/memories`
endpoint. When the `is_processing` value is 0 then call the
`POST /2/memories/termbase/download` endpoint.

```bash
  curl -X POST https://api.lilt.com/v2/memories/termbase/export?key=API_KEY&id=ID
```


### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.termbase_export_response import TermbaseExportResponse
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
    api_instance = lilt.MemoriesApi(api_client)
    id = 56 # int | A unique Memory identifier.

    try:
        # Termbase export for a Memory
        api_response = api_instance.export_termbase(id)
        print("The response of MemoriesApi->export_termbase:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoriesApi->export_termbase: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique Memory identifier. | 

### Return type

[**TermbaseExportResponse**](TermbaseExportResponse.md)

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

# **get_memory**
> List[Memory] get_memory(id=id)

Retrieve a Memory

Retrieve a Memory. If you cannot access the Memory (401 error) please check permissions (e.g. in case you created the Memory via the web app with a different account you may have to explicitly share that Memory).



### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.memory import Memory
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
    api_instance = lilt.MemoriesApi(api_client)
    id = 56 # int | An optional Memory identifier. (optional)

    try:
        # Retrieve a Memory
        api_response = api_instance.get_memory(id=id)
        print("The response of MemoriesApi->get_memory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoriesApi->get_memory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| An optional Memory identifier. | [optional] 

### Return type

[**List[Memory]**](Memory.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Memory objects. |  -  |
**401** | Unauthorized |  -  |
**404** | Memory not found. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_memory_file**
> MemoryImportResponse import_memory_file(memory_id, name, body, sdlxliff_filters=sdlxliff_filters, has_header_row=has_header_row, skip_duplicates=skip_duplicates)

File import for a Memory

Imports common translation memory or termbase file formats to a specific LILT memory. Currently supported file formats are `*.tmx`, `*.sdltm`, `*.sdlxliff`(With custom Filters), '*.xliff', and `*.tmq` for TM data; `*.csv` and `*.tbx` for termbase data. Request parameters should be passed as JSON object with the header field `LILT-API`.

Example CURL command to upload a translation memory file named `my_memory.sdltm` in the current working directory:
```bash
  curl -X POST https://api.lilt.com/v2/memories/import?key=API_KEY \
    --header "LILT-API: {\"name\": \"my_memory.sdltm\",\"memory_id\": 42}" \
    --header "Content-Type: application/octet-stream" \
    --data-binary @my_memory.sdltm
```

Example CURL command to upload a translation memory file named `my_memory.sdlxliff` in the current working directory, with Custom Filters based on SDLXLIFF fields, conf_name which maps to, percentage, and whether we should ignore unlocked segments.
```bash
  curl -X POST https://api.lilt.com/v2/memories/import?key=API_KEY \
    --header "LILT-API: {\"name\": \"my_memory.sdlxliff\",\"memory_id\": 12,\"sdlxliff_filters\":[{\"conf_name\": \"Translated\", \"percentage\": 100, \"allow_unlocked\": false}]"}" \
    --header "Content-Type: application/octet-stream" \
    --data-binary @my_memory.sdlxliff
```



### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.memory_import_response import MemoryImportResponse
from lilt.models.sdlxliff_filter import SDLXLIFFFilter
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
    api_instance = lilt.MemoriesApi(api_client)
    memory_id = 56 # int | A unique Memory identifier.
    name = 'name_example' # str | Name of the TM or termbase file.
    body = None # bytearray | The file contents to be uploaded. The entire POST body will be treated as the file.
    sdlxliff_filters = [lilt.SDLXLIFFFilter()] # List[SDLXLIFFFilter] | Contains Filter information Unique to SDLXLIFF (optional)
    has_header_row = True # bool | A flag indicating whether an imported Termbase CSV has a header row or not (the default value is `false`). (optional)
    skip_duplicates = True # bool | A flag indicating whether or not to skip the import of segments which already exist in the memory. (the default value is `false`).  (optional)

    try:
        # File import for a Memory
        api_response = api_instance.import_memory_file(memory_id, name, body, sdlxliff_filters=sdlxliff_filters, has_header_row=has_header_row, skip_duplicates=skip_duplicates)
        print("The response of MemoriesApi->import_memory_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoriesApi->import_memory_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **memory_id** | **int**| A unique Memory identifier. | 
 **name** | **str**| Name of the TM or termbase file. | 
 **body** | **bytearray**| The file contents to be uploaded. The entire POST body will be treated as the file. | 
 **sdlxliff_filters** | [**List[SDLXLIFFFilter]**](SDLXLIFFFilter.md)| Contains Filter information Unique to SDLXLIFF | [optional] 
 **has_header_row** | **bool**| A flag indicating whether an imported Termbase CSV has a header row or not (the default value is &#x60;false&#x60;). | [optional] 
 **skip_duplicates** | **bool**| A flag indicating whether or not to skip the import of segments which already exist in the memory. (the default value is &#x60;false&#x60;).  | [optional] 

### Return type

[**MemoryImportResponse**](MemoryImportResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json, application/octet-stream, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A status object. |  -  |
**401** | Unauthorized |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_memory**
> List[TranslationMemoryEntry] query_memory(id, query, n=n)

Query a Memory

Perform a translation memory query.


### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.translation_memory_entry import TranslationMemoryEntry
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
    api_instance = lilt.MemoriesApi(api_client)
    id = 56 # int | A unique Memory identifier.
    query = 'query_example' # str | A source query.
    n = 10 # int | Maximum number of results to return. (optional) (default to 10)

    try:
        # Query a Memory
        api_response = api_instance.query_memory(id, query, n=n)
        print("The response of MemoriesApi->query_memory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoriesApi->query_memory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique Memory identifier. | 
 **query** | **str**| A source query. | 
 **n** | **int**| Maximum number of results to return. | [optional] [default to 10]

### Return type

[**List[TranslationMemoryEntry]**](TranslationMemoryEntry.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of TranslationMemoryEntry objects. |  -  |
**401** | Unauthorized |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_memory**
> Memory update_memory(body)

Update the name of a Memory

Update a Memory.


### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.memory import Memory
from lilt.models.memory_update_parameters import MemoryUpdateParameters
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
    api_instance = lilt.MemoriesApi(api_client)
    body = lilt.MemoryUpdateParameters() # MemoryUpdateParameters | The Memory resource to update.

    try:
        # Update the name of a Memory
        api_response = api_instance.update_memory(body)
        print("The response of MemoriesApi->update_memory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoriesApi->update_memory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MemoryUpdateParameters**](MemoryUpdateParameters.md)| The Memory resource to update. | 

### Return type

[**Memory**](Memory.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/octet-stream, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Memory object. |  -  |
**401** | Unauthorized |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

