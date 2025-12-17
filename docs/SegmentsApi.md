# lilt.SegmentsApi

All URIs are relative to *https://api.lilt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_segment**](SegmentsApi.md#create_segment) | **POST** /v2/segments | Create a Segment
[**delete_segment**](SegmentsApi.md#delete_segment) | **DELETE** /v2/segments | Delete a Segment
[**get_segment**](SegmentsApi.md#get_segment) | **GET** /v2/segments | Retrieve a Segment
[**tag_segment**](SegmentsApi.md#tag_segment) | **GET** /segments/tag | Tag a Segment
[**unlock_segments**](SegmentsApi.md#unlock_segments) | **POST** /segments/review/unlock | Unaccept and unlock segments
[**update_segment**](SegmentsApi.md#update_segment) | **PUT** /v2/segments | Update a Segment


# **create_segment**
> Segment create_segment(segment_create_parameters)

Create a Segment

Create a Segment and add it to a Memory or a Document. A Segment is a source/target
pair that is used to train the machine translation system and populate
the translation memory.

The maximum source length is 5,000 characters.



### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.segment import Segment
from lilt.models.segment_create_parameters import SegmentCreateParameters
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
    api_instance = lilt.SegmentsApi(api_client)
    segment_create_parameters = lilt.SegmentCreateParameters() # SegmentCreateParameters | The Segment resource to create.  To add a Segment to a Memory, include the `memory_id` and `target` parameters.  To add a Segment to a Document, include the `document_id` and the `source` parameters. The `target` parameter is optional. 

    try:
        # Create a Segment
        api_response = api_instance.create_segment(segment_create_parameters)
        print("The response of SegmentsApi->create_segment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentsApi->create_segment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_create_parameters** | [**SegmentCreateParameters**](SegmentCreateParameters.md)| The Segment resource to create.  To add a Segment to a Memory, include the &#x60;memory_id&#x60; and &#x60;target&#x60; parameters.  To add a Segment to a Document, include the &#x60;document_id&#x60; and the &#x60;source&#x60; parameters. The &#x60;target&#x60; parameter is optional.  | 

### Return type

[**Segment**](Segment.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Segment object. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_segment**
> SegmentDeleteResponse delete_segment(id)

Delete a Segment

Delete a Segment from memory. This will not delete a segment from a document.


### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.segment_delete_response import SegmentDeleteResponse
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
    api_instance = lilt.SegmentsApi(api_client)
    id = 56 # int | A unique Segment identifier.

    try:
        # Delete a Segment
        api_response = api_instance.delete_segment(id)
        print("The response of SegmentsApi->delete_segment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentsApi->delete_segment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique Segment identifier. | 

### Return type

[**SegmentDeleteResponse**](SegmentDeleteResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A status object. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_segment**
> Segment get_segment(id, include_comments=include_comments)

Retrieve a Segment

Retrieve a Segment.



### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.segment import Segment
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
    api_instance = lilt.SegmentsApi(api_client)
    id = 56 # int | A unique Segment identifier.
    include_comments = False # bool | Include comments in the response. (optional) (default to False)

    try:
        # Retrieve a Segment
        api_response = api_instance.get_segment(id, include_comments=include_comments)
        print("The response of SegmentsApi->get_segment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentsApi->get_segment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique Segment identifier. | 
 **include_comments** | **bool**| Include comments in the response. | [optional] [default to False]

### Return type

[**Segment**](Segment.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Segment object. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tag_segment**
> TaggedSegment tag_segment(source_tagged, target, memory_id)

Tag a Segment

Project tags for a segment. The `source_tagged` string contains one or more SGML
tags. The `target` string is untagged. This endpoint will automatically place the
source tags in the target.

Usage charges apply to this endpoint for production REST API keys.



### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.tagged_segment import TaggedSegment
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
    api_instance = lilt.SegmentsApi(api_client)
    source_tagged = 'source_tagged_example' # str | The tagged source string.
    target = 'target_example' # str | The target string.
    memory_id = 56 # int | A unique Memory identifier.

    try:
        # Tag a Segment
        api_response = api_instance.tag_segment(source_tagged, target, memory_id)
        print("The response of SegmentsApi->tag_segment:\n")
        pprint(api_response)
    except Exception as e:
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

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A TaggedSegment object. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlock_segments**
> List[float] unlock_segments(segment_done_response)

Unaccept and unlock segments

Unaccept and unlock segments.
Sets individual segments' "Review Done" to false. Confirmed segments will remain confirmed.

Example curl:
```
  curl --X --request POST 'https://lilt.com/2/segments/review/unlock?key=API_KEY' \
  --header 'Content-Type: application/json' \
  --data-raw '{
      "segmentIds": [23921, 23922]
  }'
```


### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.segment_done_response import SegmentDoneResponse
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
    api_instance = lilt.SegmentsApi(api_client)
    segment_done_response = lilt.SegmentDoneResponse() # SegmentDoneResponse | segment ids to update

    try:
        # Unaccept and unlock segments
        api_response = api_instance.unlock_segments(segment_done_response)
        print("The response of SegmentsApi->unlock_segments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentsApi->unlock_segments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_done_response** | [**SegmentDoneResponse**](SegmentDoneResponse.md)| segment ids to update | 

### Return type

**List[float]**

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | array of updated segments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_segment**
> Segment update_segment(segment_update_parameters)

Update a Segment

Update a Segment in memory. The Memory will be updated with the new target string.



### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.segment import Segment
from lilt.models.segment_update_parameters import SegmentUpdateParameters
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
    api_instance = lilt.SegmentsApi(api_client)
    segment_update_parameters = lilt.SegmentUpdateParameters() # SegmentUpdateParameters | The Segment resource to update.

    try:
        # Update a Segment
        api_response = api_instance.update_segment(segment_update_parameters)
        print("The response of SegmentsApi->update_segment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SegmentsApi->update_segment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_update_parameters** | [**SegmentUpdateParameters**](SegmentUpdateParameters.md)| The Segment resource to update. | 

### Return type

[**Segment**](Segment.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Segment object. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

