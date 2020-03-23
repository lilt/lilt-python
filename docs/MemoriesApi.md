# pylilt.MemoriesApi

All URIs are relative to *https://lilt.com/2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_memory**](MemoriesApi.md#create_memory) | **POST** /memories | Create a Memory
[**delete_memory**](MemoriesApi.md#delete_memory) | **DELETE** /memories | Delete a Memory
[**get_memory**](MemoriesApi.md#get_memory) | **GET** /memories | Retrieve a Memory
[**import_memory_file**](MemoriesApi.md#import_memory_file) | **POST** /memories/import | File import for a Memory
[**query_memory**](MemoriesApi.md#query_memory) | **GET** /memories/query | Query a Memory
[**sync_delete_memory**](MemoriesApi.md#sync_delete_memory) | **DELETE** /memories/sync | Delete-sync for a Memory
[**sync_down_memory**](MemoriesApi.md#sync_down_memory) | **GET** /memories/sync | Get-sync for a Memory
[**sync_insert_memory**](MemoriesApi.md#sync_insert_memory) | **POST** /memories/sync | Insert-sync for a Memory
[**sync_update_memory**](MemoriesApi.md#sync_update_memory) | **PUT** /memories/sync | Update-sync for a Memory
[**update_memory**](MemoriesApi.md#update_memory) | **PUT** /memories | Update the name of a Memory

# **create_memory**
> Memory create_memory(body)

Create a Memory

Create a new Memory. A Memory is a container that collects source/target sentences for a specific language pair (e.g., English>French). The data in the Memory is used to train the MT system, populate the TM, and update the lexicon. Memories are private to your account - the data is not shared across users - unless you explicitly share a Memory with your team (via web app only).  <a href=\"https://lilt.com/kb/memory/memories\" target=_blank>Refer to our KB</a> for a more detailed description.  

### Example
```python
from __future__ import print_function
import time
import pylilt
from pylilt.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = pylilt.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'# Configure HTTP basic authorization: BasicAuth
configuration = pylilt.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pylilt.MemoriesApi(pylilt.ApiClient(configuration))
body = NULL # object | The Memory resource to create.

try:
    # Create a Memory
    api_response = api_instance.create_memory(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MemoriesApi->create_memory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| The Memory resource to create. | 

### Return type

[**Memory**](Memory.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_memory**
> object delete_memory(id)

Delete a Memory

Delete a Memory. 

### Example
```python
from __future__ import print_function
import time
import pylilt
from pylilt.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = pylilt.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'# Configure HTTP basic authorization: BasicAuth
configuration = pylilt.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pylilt.MemoriesApi(pylilt.ApiClient(configuration))
id = 56 # int | A unique Memory identifier.

try:
    # Delete a Memory
    api_response = api_instance.delete_memory(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MemoriesApi->delete_memory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique Memory identifier. | 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_memory**
> list[Memory] get_memory(id=id)

Retrieve a Memory

Retrieve a Memory. If you cannot access the Memory (401 error) please check permissions (e.g. in case you created the Memory via the web app with a different account you may have to explicitly share that Memory).  

### Example
```python
from __future__ import print_function
import time
import pylilt
from pylilt.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = pylilt.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'# Configure HTTP basic authorization: BasicAuth
configuration = pylilt.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pylilt.MemoriesApi(pylilt.ApiClient(configuration))
id = 56 # int | An optional Memory identifier. (optional)

try:
    # Retrieve a Memory
    api_response = api_instance.get_memory(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MemoriesApi->get_memory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| An optional Memory identifier. | [optional] 

### Return type

[**list[Memory]**](Memory.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_memory_file**
> object import_memory_file(body, id, name)

File import for a Memory

Imports common translation memory or termbase file formats to a specific Lilt memory. Currently supported file formats are `*.tmx`, `*.sdltm` and `*.tmq` for TM data; `*.csv` and `*.tbx` for termbase data. Request parameters should be passed as JSON object with the header field `LILT-API`.  Example cURL command to upload a translation memory file named `my_memory.sdltm` in the current working directory: ```   curl -X POST https://lilt.com/2/memories/import?key=API_KEY \\     --header \"LILT-API: {\\\"name\\\": \\\"my_memory.sdltm\\\",\\\"memory_id\\\": 42}\" \\     --header \"Content-Type: application/octet-stream\" \\     --data-binary @my_memory.sdltm ```  

### Example
```python
from __future__ import print_function
import time
import pylilt
from pylilt.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = pylilt.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'# Configure HTTP basic authorization: BasicAuth
configuration = pylilt.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pylilt.MemoriesApi(pylilt.ApiClient(configuration))
body = 'body_example' # str | The file contents to be uploaded. The entire POST body will be treated as the file.
id = 56 # int | A unique Memory identifier.
name = 'name_example' # str | Name of the TM or termbase file.

try:
    # File import for a Memory
    api_response = api_instance.import_memory_file(body, id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MemoriesApi->import_memory_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| The file contents to be uploaded. The entire POST body will be treated as the file. | 
 **id** | **int**| A unique Memory identifier. | 
 **name** | **str**| Name of the TM or termbase file. | 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_memory**
> list[TranslationMemoryEntry] query_memory(id, query, n=n)

Query a Memory

Perform a translation memory query.  

### Example
```python
from __future__ import print_function
import time
import pylilt
from pylilt.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = pylilt.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'# Configure HTTP basic authorization: BasicAuth
configuration = pylilt.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pylilt.MemoriesApi(pylilt.ApiClient(configuration))
id = 56 # int | A unique Memory identifier.
query = 'query_example' # str | A source query.
n = 56 # int | Maximum number of results to return. (optional)

try:
    # Query a Memory
    api_response = api_instance.query_memory(id, query, n=n)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MemoriesApi->query_memory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique Memory identifier. | 
 **query** | **str**| A source query. | 
 **n** | **int**| Maximum number of results to return. | [optional] 

### Return type

[**list[TranslationMemoryEntry]**](TranslationMemoryEntry.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_delete_memory**
> object sync_delete_memory(id, from_time=from_time, to_time=to_time, when=when)

Delete-sync for a Memory

Deletes segments in the Memory matching the `from_time`, `to_time` and `when` parameters.  Example CURL command: ```   curl -X DELETE https://lilt.com/2/memories/sync?key=API_KEY&id=42&from_time=1491048000&to_time=1491049800&when=created ```  

### Example
```python
from __future__ import print_function
import time
import pylilt
from pylilt.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = pylilt.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'# Configure HTTP basic authorization: BasicAuth
configuration = pylilt.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pylilt.MemoriesApi(pylilt.ApiClient(configuration))
id = 56 # int | A unique Memory identifier.
from_time = 56 # int | Unix time stamp (epoch, in seconds) of the start of the Memory section. (optional)
to_time = 56 # int | Unix time stamp (epoch, in seconds) of the end of the Memory section. (optional)
when = 'when_example' # str | The date field on which retrieved segments match from/to time stamps: `created`, `updated`, `deleted`. (optional)

try:
    # Delete-sync for a Memory
    api_response = api_instance.sync_delete_memory(id, from_time=from_time, to_time=to_time, when=when)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MemoriesApi->sync_delete_memory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique Memory identifier. | 
 **from_time** | **int**| Unix time stamp (epoch, in seconds) of the start of the Memory section. | [optional] 
 **to_time** | **int**| Unix time stamp (epoch, in seconds) of the end of the Memory section. | [optional] 
 **when** | **str**| The date field on which retrieved segments match from/to time stamps: &#x60;created&#x60;, &#x60;updated&#x60;, &#x60;deleted&#x60;. | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_down_memory**
> str sync_down_memory(id, from_time=from_time, to_time=to_time, when=when)

Get-sync for a Memory

Get all or part of a memory in TMX 1.4b format. If the `from_time` and/or `to_time` are omitted, then all segments are returned. The parameter `when` specifies on which date field `from_time` and `to_time` are matched. Possible values are `created` (when the segment was originally created in the memory), `updated` (when the segment was lastly updated), and `deleted` (when the segment was deleted).  Example CURL command: ```   curl -X GET https://lilt.com/2/memories/sync?key=API_KEY&id=42 -o from_lilt.tmx ```  

### Example
```python
from __future__ import print_function
import time
import pylilt
from pylilt.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = pylilt.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'# Configure HTTP basic authorization: BasicAuth
configuration = pylilt.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pylilt.MemoriesApi(pylilt.ApiClient(configuration))
id = 56 # int | A unique Memory identifier.
from_time = 56 # int | Unix time stamp (epoch, in seconds) of the start of the Memory section. (optional)
to_time = 56 # int | Unix time stamp (epoch, in seconds) of the end of the Memory section. (optional)
when = 'when_example' # str | The date field on which retrieved segments match from/to time stamps: `created`, `updated`, `deleted`. If this parameter is omitted, then the whole Memory is returned. (optional)

try:
    # Get-sync for a Memory
    api_response = api_instance.sync_down_memory(id, from_time=from_time, to_time=to_time, when=when)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MemoriesApi->sync_down_memory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique Memory identifier. | 
 **from_time** | **int**| Unix time stamp (epoch, in seconds) of the start of the Memory section. | [optional] 
 **to_time** | **int**| Unix time stamp (epoch, in seconds) of the end of the Memory section. | [optional] 
 **when** | **str**| The date field on which retrieved segments match from/to time stamps: &#x60;created&#x60;, &#x60;updated&#x60;, &#x60;deleted&#x60;. If this parameter is omitted, then the whole Memory is returned. | [optional] 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-tmx

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_insert_memory**
> object sync_insert_memory(body, id, name=name)

Insert-sync for a Memory

Inserts a TM in TMX 1.4b format into the Memory. Request parameters should be passed as JSON object with the header field `LILT-API`.  Example CURL command: ```   curl -X POST https://lilt.com/2/memories/sync?key=API_KEY \\     --header \"LILT-API: {\\\"name\\\": \\\"my_memory.tmx\\\",\\\"id\\\": 42}\" \\     --header \"Content-Type: application/octet-stream\" \\     --data-binary @my_memory.tmx ```  

### Example
```python
from __future__ import print_function
import time
import pylilt
from pylilt.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = pylilt.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'# Configure HTTP basic authorization: BasicAuth
configuration = pylilt.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pylilt.MemoriesApi(pylilt.ApiClient(configuration))
body = 'body_example' # str | The file contents to be uploaded. The entire POST body will be treated as the file.
id = 56 # int | A unique Memory identifier.
name = 'name_example' # str | Name of the TMX file. (optional)

try:
    # Insert-sync for a Memory
    api_response = api_instance.sync_insert_memory(body, id, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MemoriesApi->sync_insert_memory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| The file contents to be uploaded. The entire POST body will be treated as the file. | 
 **id** | **int**| A unique Memory identifier. | 
 **name** | **str**| Name of the TMX file. | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_update_memory**
> object sync_update_memory(body, id, from_time=from_time, to_time=to_time, when=when)

Update-sync for a Memory

Updates the Memory with given TMX file. Request parameters should be passed as JSON object with the header field `LILT-API`. The number of segments returned by the `from_time`, `to_time`, `when` parameters and the number of segments in the TMX file need to be identical.  Example CURL command: ```   curl -X PUT https://lilt.com/2/memories/sync?key=API_KEY \\     --header \"LILT-API: {\\\"name\\\": \\\"my_memory.tmx\\\", \\\"id\\\": 42, \\\"from_time\\\": 1491048000, \\\"to_time\\\": 1491049800, \"when\": \"Updated\"}\" \\     --header \"Content-Type: application/octet-stream\" \\     --data-binary @my_memory.tmx ```  

### Example
```python
from __future__ import print_function
import time
import pylilt
from pylilt.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = pylilt.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'# Configure HTTP basic authorization: BasicAuth
configuration = pylilt.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pylilt.MemoriesApi(pylilt.ApiClient(configuration))
body = 'body_example' # str | The file contents to be uploaded. The entire PUT body will be treated as the file.
id = 56 # int | A unique Memory identifier.
from_time = 56 # int | Unix time stamp (epoch, in seconds) of the start of the Memory section. (optional)
to_time = 56 # int | Unix time stamp (epoch, in seconds) of the end of the Memory section. (optional)
when = 'when_example' # str | The date field on which retrieved segments match from/to time stamps: `created`, `updated`, `deleted`. (optional)

try:
    # Update-sync for a Memory
    api_response = api_instance.sync_update_memory(body, id, from_time=from_time, to_time=to_time, when=when)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MemoriesApi->sync_update_memory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| The file contents to be uploaded. The entire PUT body will be treated as the file. | 
 **id** | **int**| A unique Memory identifier. | 
 **from_time** | **int**| Unix time stamp (epoch, in seconds) of the start of the Memory section. | [optional] 
 **to_time** | **int**| Unix time stamp (epoch, in seconds) of the end of the Memory section. | [optional] 
 **when** | **str**| The date field on which retrieved segments match from/to time stamps: &#x60;created&#x60;, &#x60;updated&#x60;, &#x60;deleted&#x60;. | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_memory**
> Memory update_memory(body)

Update the name of a Memory

Update a Memory. 

### Example
```python
from __future__ import print_function
import time
import pylilt
from pylilt.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = pylilt.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'# Configure HTTP basic authorization: BasicAuth
configuration = pylilt.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pylilt.MemoriesApi(pylilt.ApiClient(configuration))
body = NULL # object | The Memory resource to update.

try:
    # Update the name of a Memory
    api_response = api_instance.update_memory(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MemoriesApi->update_memory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| The Memory resource to update. | 

### Return type

[**Memory**](Memory.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

