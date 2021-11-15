# lilt.CommentsApi

All URIs are relative to *https://lilt.com/2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_comment**](CommentsApi.md#create_comment) | **POST** /comments | Create a new comment
[**delete_comment**](CommentsApi.md#delete_comment) | **DELETE** /comments | Delete a Comment
[**get_document_comments**](CommentsApi.md#get_document_comments) | **GET** /comments | Retrieve a document&#39;s comments by segment
[**update_comment**](CommentsApi.md#update_comment) | **PUT** /comments | Update an existing comment


# **create_comment**
> Comment create_comment(document_id, segment_id, body)

Create a new comment

Create a new comment for the specified Segment ID.

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
    api_instance = lilt.CommentsApi(api_client)
    document_id = 56 # int | A unique document identifier.
segment_id = 56 # int | A unique segment identifier.
body = lilt.CommentBody() # CommentBody | The comment being created

    try:
        # Create a new comment
        api_response = api_instance.create_comment(document_id, segment_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommentsApi->create_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **int**| A unique document identifier. | 
 **segment_id** | **int**| A unique segment identifier. | 
 **body** | [**CommentBody**](CommentBody.md)| The comment being created | 

### Return type

[**Comment**](Comment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A Comment object. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comment**
> CommentDeleteResponse delete_comment(comment_id)

Delete a Comment

Delete a Comment.  Example CURL command: ```   curl -X DELETE https://lilt.com/2/comments?key=API_KEY&comment_id=123 ``` 

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
    api_instance = lilt.CommentsApi(api_client)
    comment_id = 56 # int | A unique Comment identifier.

    try:
        # Delete a Comment
        api_response = api_instance.delete_comment(comment_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommentsApi->delete_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **int**| A unique Comment identifier. | 

### Return type

[**CommentDeleteResponse**](CommentDeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | A status object. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_comments**
> DocumentComments get_document_comments(document_id)

Retrieve a document's comments by segment

Retrieves all comments associated with a specified document, grouped by their Segment's ID.  To retrieve a document's comments, specify the <strong>document_id</strong> request parameter.  Example CURL command: ```   curl -X GET https://lilt.com/2/comments?key=API_KEY&document_id=123 ``` 

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
    api_instance = lilt.CommentsApi(api_client)
    document_id = 56 # int | A unique document identifier.

    try:
        # Retrieve a document's comments by segment
        api_response = api_instance.get_document_comments(document_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommentsApi->get_document_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **int**| A unique document identifier. | 

### Return type

[**DocumentComments**](DocumentComments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object containing lists of comments identified by the id of the segment to which they belong. |  -  |
**403** | Unauthorized. |  -  |
**410** | Comment deleted. |  -  |
**0** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comment**
> Comment update_comment(comment_id, document_id, body)

Update an existing comment

Update an existing comment.

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
    api_instance = lilt.CommentsApi(api_client)
    comment_id = 56 # int | A unique comment identifier.
document_id = 56 # int | A unique document identifier.
body = lilt.CommentBody() # CommentBody | The comment being updated.

    try:
        # Update an existing comment
        api_response = api_instance.update_comment(comment_id, document_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommentsApi->update_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **int**| A unique comment identifier. | 
 **document_id** | **int**| A unique document identifier. | 
 **body** | [**CommentBody**](CommentBody.md)| The comment being updated. | 

### Return type

[**Comment**](Comment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A Comment object. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

