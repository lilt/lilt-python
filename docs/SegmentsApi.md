# pylilt.SegmentsApi

All URIs are relative to *https://lilt.com/2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_segment**](SegmentsApi.md#create_segment) | **POST** /segments | Create a Segment
[**delete_segment**](SegmentsApi.md#delete_segment) | **DELETE** /segments | Delete a Segment
[**get_segment**](SegmentsApi.md#get_segment) | **GET** /segments | Retrieve a Segment
[**tag_segment**](SegmentsApi.md#tag_segment) | **GET** /segments/tag | Tag a Segment
[**update_segment**](SegmentsApi.md#update_segment) | **PUT** /segments | Update a Segment

# **create_segment**
> Segment create_segment(body)

Create a Segment

Create a Segment and add it to a Memory. A Segment is a source/target pair that is used to train the machine translation system and populate the translation memory. This is not intended to be used on documents and will throw an error.  The maximum source length is 5,000 characters.  

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
api_instance = pylilt.SegmentsApi(pylilt.ApiClient(configuration))
body = NULL # object | The Segment resource to create.

To add a Segment to a Memory, include the `memory_id` and `target` parameters.

To add a Segment to a Document, include the `document_id` and the `source` parameters.
The `target` parameter is optional.


try:
    # Create a Segment
    api_response = api_instance.create_segment(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentsApi->create_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| The Segment resource to create.

To add a Segment to a Memory, include the &#x60;memory_id&#x60; and &#x60;target&#x60; parameters.

To add a Segment to a Document, include the &#x60;document_id&#x60; and the &#x60;source&#x60; parameters.
The &#x60;target&#x60; parameter is optional.
 | 

### Return type

[**Segment**](Segment.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_segment**
> object delete_segment(id)

Delete a Segment

Delete a Segment from memory. This will not delete a segment from a document. 

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
api_instance = pylilt.SegmentsApi(pylilt.ApiClient(configuration))
id = 56 # int | A unique Segment identifier.

try:
    # Delete a Segment
    api_response = api_instance.delete_segment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentsApi->delete_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique Segment identifier. | 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_segment**
> Segment get_segment(id)

Retrieve a Segment

Retrieve a Segment.  

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
api_instance = pylilt.SegmentsApi(pylilt.ApiClient(configuration))
id = 56 # int | A unique Segment identifier.

try:
    # Retrieve a Segment
    api_response = api_instance.get_segment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentsApi->get_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique Segment identifier. | 

### Return type

[**Segment**](Segment.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tag_segment**
> TaggedSegment tag_segment(source_tagged, target, memory_id)

Tag a Segment

Project tags for a segment. The `source_tagged` string contains one or more SGML tags. The `target` string is untagged. This endpoint will automatically place the source tags in the target.  Usage charges apply to this endpoint for production REST API keys.  

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
api_instance = pylilt.SegmentsApi(pylilt.ApiClient(configuration))
source_tagged = 'source_tagged_example' # str | The tagged source string.
target = 'target_example' # str | The target string.
memory_id = 56 # int | A unique Memory identifier.

try:
    # Tag a Segment
    api_response = api_instance.tag_segment(source_tagged, target, memory_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentsApi->tag_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_tagged** | **str**| The tagged source string. | 
 **target** | **str**| The target string. | 
 **memory_id** | **int**| A unique Memory identifier. | 

### Return type

[**TaggedSegment**](TaggedSegment.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_segment**
> Segment update_segment(body)

Update a Segment

Update a Segment in memory. The Memory will be updated with the new target string.  

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
api_instance = pylilt.SegmentsApi(pylilt.ApiClient(configuration))
body = NULL # object | The Segment resource to update.

try:
    # Update a Segment
    api_response = api_instance.update_segment(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentsApi->update_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| The Segment resource to update. | 

### Return type

[**Segment**](Segment.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

