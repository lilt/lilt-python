# lilt.DocumentsApi

All URIs are relative to *https://lilt.com/2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_document**](DocumentsApi.md#assign_document) | **PUT** /documents/share | Assign a Document
[**create_document**](DocumentsApi.md#create_document) | **POST** /documents | Create a Document
[**delete_document**](DocumentsApi.md#delete_document) | **DELETE** /documents | Delete a Document
[**document_translation_done**](DocumentsApi.md#document_translation_done) | **POST** /documents/done/translation | Mark translation done
[**document_unlock**](DocumentsApi.md#document_unlock) | **POST** /documents/done/unlock | Unlock documents
[**documents_done_review_post**](DocumentsApi.md#documents_done_review_post) | **POST** /documents/done/review | Mark review done
[**download_document**](DocumentsApi.md#download_document) | **GET** /documents/files | Download a Document
[**get_document**](DocumentsApi.md#get_document) | **GET** /documents | Retrieve a Document
[**pretranslate_documents**](DocumentsApi.md#pretranslate_documents) | **POST** /documents/pretranslate | Pretranslate a Document
[**update_document**](DocumentsApi.md#update_document) | **PUT** /documents | Update a Document
[**upload_document**](DocumentsApi.md#upload_document) | **POST** /documents/files | Upload a File


# **assign_document**
> DocumentAssignmentResponse assign_document(body)

Assign a Document

Assign and unassign a Document for translation and/or review.  

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
    api_instance = lilt.DocumentsApi(api_client)
    body = lilt.DocumentAssignmentParameters() # DocumentAssignmentParameters | 

    try:
        # Assign a Document
        api_response = api_instance.assign_document(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentsApi->assign_document: %s\n" % e)
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
    api_instance = lilt.DocumentsApi(api_client)
    body = lilt.DocumentAssignmentParameters() # DocumentAssignmentParameters | 

    try:
        # Assign a Document
        api_response = api_instance.assign_document(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentsApi->assign_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentAssignmentParameters**](DocumentAssignmentParameters.md)|  | 

### Return type

[**DocumentAssignmentResponse**](DocumentAssignmentResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A status object. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_document**
> DocumentWithSegments create_document(body=body)

Create a Document

Create a new Document. A Document is a collection of one or more Segments. Documents are nested inside of Projects, and appear in the Project details view in the web app. Document-level relationships between Segments are considered by the machine translation system during adaptation. If there is no inherent document structure in your data, you still might consider grouping related Segments into Documents to improve translation quality. 

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
    api_instance = lilt.DocumentsApi(api_client)
    body = lilt.DocumentParameters() # DocumentParameters |  (optional)

    try:
        # Create a Document
        api_response = api_instance.create_document(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentsApi->create_document: %s\n" % e)
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
    api_instance = lilt.DocumentsApi(api_client)
    body = lilt.DocumentParameters() # DocumentParameters |  (optional)

    try:
        # Create a Document
        api_response = api_instance.create_document(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentsApi->create_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentParameters**](DocumentParameters.md)|  | [optional] 

### Return type

[**DocumentWithSegments**](DocumentWithSegments.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Document object. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document**
> DocumentDeleteResponse delete_document(id)

Delete a Document

Delete a Document. 

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
    api_instance = lilt.DocumentsApi(api_client)
    id = 56 # int | A unique Document identifier.

    try:
        # Delete a Document
        api_response = api_instance.delete_document(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentsApi->delete_document: %s\n" % e)
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
    api_instance = lilt.DocumentsApi(api_client)
    id = 56 # int | A unique Document identifier.

    try:
        # Delete a Document
        api_response = api_instance.delete_document(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentsApi->delete_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique Document identifier. | 

### Return type

[**DocumentDeleteResponse**](DocumentDeleteResponse.md)

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

# **document_translation_done**
> list[float] document_translation_done(body)

Mark translation done

Mark the translation of documents as done/undone in bulk.  When being marked positively as done:  - Documents must not already be marked as done and all segments must be confirmed. - This request will also trigger an email notification to a document's assigned reviewer that the document is ready for review.  When being marked as un-done: - Documents must not be marked as complete for review.  Example curl: ```   curl --X --request POST 'https://lilt.com/2/documents/done/translation?key=API_KEY' \\   --header 'Content-Type: application/json' \\   --data-raw '{       \"documentIds\": [23921, 23922],       \"isDone\": true   }' ``` 

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
    api_instance = lilt.DocumentsApi(api_client)
    body = lilt.DocumentDoneUpdateParameters1() # DocumentDoneUpdateParameters1 | 

    try:
        # Mark translation done
        api_response = api_instance.document_translation_done(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentsApi->document_translation_done: %s\n" % e)
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
    api_instance = lilt.DocumentsApi(api_client)
    body = lilt.DocumentDoneUpdateParameters1() # DocumentDoneUpdateParameters1 | 

    try:
        # Mark translation done
        api_response = api_instance.document_translation_done(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentsApi->document_translation_done: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentDoneUpdateParameters1**](DocumentDoneUpdateParameters1.md)|  | 

### Return type

**list[float]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | array of updated documents |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **document_unlock**
> list[float] document_unlock(body)

Unlock documents

Unlock documents for translation. Sets document \"Translation Done\" and \"Review Done\" to false.  Example curl: ```   curl --X --request POST 'https://lilt.com/2/documents/done/unlock?key=API_KEY' \\   --header 'Content-Type: application/json' \\   --data-raw '{       \"documentIds\": [23921, 23922]   }' ``` 

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
    api_instance = lilt.DocumentsApi(api_client)
    body = lilt.DocumentDoneUpdateParameters() # DocumentDoneUpdateParameters | 

    try:
        # Unlock documents
        api_response = api_instance.document_unlock(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentsApi->document_unlock: %s\n" % e)
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
    api_instance = lilt.DocumentsApi(api_client)
    body = lilt.DocumentDoneUpdateParameters() # DocumentDoneUpdateParameters | 

    try:
        # Unlock documents
        api_response = api_instance.document_unlock(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentsApi->document_unlock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentDoneUpdateParameters**](DocumentDoneUpdateParameters.md)|  | 

### Return type

**list[float]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | array of updated documents |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documents_done_review_post**
> list[float] documents_done_review_post(body)

Mark review done

Mark the review of documents as done/undone in bulk.  When being marked positively as done:  - Documents must not already be marked as done for review. - Documents must already be marked as done for translation. - This request will also trigger an email notification.  Example curl: ```   curl --X --request POST 'https://lilt.com/2/documents/done/review?key=API_KEY' \\   --header 'Content-Type: application/json' \\   --data-raw '{       \"documentIds\": [23921, 23922],       \"isDone\": true   }' ``` 

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
    api_instance = lilt.DocumentsApi(api_client)
    body = lilt.DocumentDoneUpdateParameters2() # DocumentDoneUpdateParameters2 | 

    try:
        # Mark review done
        api_response = api_instance.documents_done_review_post(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentsApi->documents_done_review_post: %s\n" % e)
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
    api_instance = lilt.DocumentsApi(api_client)
    body = lilt.DocumentDoneUpdateParameters2() # DocumentDoneUpdateParameters2 | 

    try:
        # Mark review done
        api_response = api_instance.documents_done_review_post(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentsApi->documents_done_review_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentDoneUpdateParameters2**](DocumentDoneUpdateParameters2.md)|  | 

### Return type

**list[float]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | array of updated documents |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_document**
> str download_document(id, is_xliff=is_xliff)

Download a Document

Export a Document that has been translated in the Lilt web application. Any Document can be downloaded in XLIFF 1.2 format, or can be retrieved in its original uploaded format by setting `is_xliff=false`. This endpoint will fail if either (a) export or (b) pre-translation operations are in-progress. The status of those operations can be determined by retrieving the Document resource. Example CURL command: ```   curl -X GET https://lilt.com/2/documents/files?key=API_KEY&id=274 -o from_lilt.xliff ```  

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
    api_instance = lilt.DocumentsApi(api_client)
    id = 56 # int | An unique Document identifier.
is_xliff = True # bool | Download the document in XLIFF 1.2 format. (optional) (default to True)

    try:
        # Download a Document
        api_response = api_instance.download_document(id, is_xliff=is_xliff)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentsApi->download_document: %s\n" % e)
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
    api_instance = lilt.DocumentsApi(api_client)
    id = 56 # int | An unique Document identifier.
is_xliff = True # bool | Download the document in XLIFF 1.2 format. (optional) (default to True)

    try:
        # Download a Document
        api_response = api_instance.download_document(id, is_xliff=is_xliff)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentsApi->download_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| An unique Document identifier. | 
 **is_xliff** | **bool**| Download the document in XLIFF 1.2 format. | [optional] [default to True]

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A file. |  -  |
**502** | File in pretranslation. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document**
> DocumentWithSegments get_document(id, with_segments=with_segments)

Retrieve a Document

List a Document.  The listing will include the pretranslation status for the document. When pretranslation is in progress for a document, the `GET /documents` endpoint's response will include `is_pretranslating = true` as well as a more detailed status property `status.pretranslation` one of `idle`, `pending`, or `running`.

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
    api_instance = lilt.DocumentsApi(api_client)
    id = 56 # int | A unique Document identifier.
with_segments = True # bool | Flag indicating whether full segment information should be returned. (optional)

    try:
        # Retrieve a Document
        api_response = api_instance.get_document(id, with_segments=with_segments)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentsApi->get_document: %s\n" % e)
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
    api_instance = lilt.DocumentsApi(api_client)
    id = 56 # int | A unique Document identifier.
with_segments = True # bool | Flag indicating whether full segment information should be returned. (optional)

    try:
        # Retrieve a Document
        api_response = api_instance.get_document(id, with_segments=with_segments)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentsApi->get_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique Document identifier. | 
 **with_segments** | **bool**| Flag indicating whether full segment information should be returned. | [optional] 

### Return type

[**DocumentWithSegments**](DocumentWithSegments.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Document object. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pretranslate_documents**
> DocumentPretranslateResponse pretranslate_documents(body, auto_accept=auto_accept, case_sensitive=case_sensitive, attribute_to_creator=attribute_to_creator, mode=mode)

Pretranslate a Document

Initiate pretranslation of a list of Documents. This request will mark document(s) as being pretranslated. Pretranslation in this context is: - Applying and confirming exact TM matches based on the Memory of the Project; - Translating all other segments via MT without confirming them.  Example CURL command: ``` curl -X POST https://lilt.com/2/documents/pretranslate?key=API_KEY -d {\"id\": [123]} -H \"Content-Type: application/json\" ```  Document translation is an asynchronous process that, in effect, is performed in the background.  To check the status of pretranslation for a document, use the `GET /documents` endpoint. When pretranslation is in progress for a document, the `GET /documents` endpoint's response will include `is_pretranslating = true` as well as a more detailed status property `status.pretranslation` one of `idle`, `pending`, or `running`.  Once pretranslation is finished, the document can be downloaded via `GET /documents/files`. 

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
    api_instance = lilt.DocumentsApi(api_client)
    body = lilt.DocumentPretranslateParameters() # DocumentPretranslateParameters | 
auto_accept = True # bool | Deprecated, use body param instead. Optional parameter for auto-accepting 100% TM hits. (optional)
case_sensitive = True # bool | Deprecated, use body param instead. Optional for using case matching against TM hits. (optional)
attribute_to_creator = True # bool | Deprecated, use body param instead. Optional parameter for attributing translation authorship of exact matches to document creator. (optional)
mode = 'mode_example' # str | Deprecated, use body param instead. An optional parameter indicating how the document will be pretranslated.  The accepted values are `tm`, or `tm+mt`. Default is `tm`.  (optional)

    try:
        # Pretranslate a Document
        api_response = api_instance.pretranslate_documents(body, auto_accept=auto_accept, case_sensitive=case_sensitive, attribute_to_creator=attribute_to_creator, mode=mode)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentsApi->pretranslate_documents: %s\n" % e)
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
    api_instance = lilt.DocumentsApi(api_client)
    body = lilt.DocumentPretranslateParameters() # DocumentPretranslateParameters | 
auto_accept = True # bool | Deprecated, use body param instead. Optional parameter for auto-accepting 100% TM hits. (optional)
case_sensitive = True # bool | Deprecated, use body param instead. Optional for using case matching against TM hits. (optional)
attribute_to_creator = True # bool | Deprecated, use body param instead. Optional parameter for attributing translation authorship of exact matches to document creator. (optional)
mode = 'mode_example' # str | Deprecated, use body param instead. An optional parameter indicating how the document will be pretranslated.  The accepted values are `tm`, or `tm+mt`. Default is `tm`.  (optional)

    try:
        # Pretranslate a Document
        api_response = api_instance.pretranslate_documents(body, auto_accept=auto_accept, case_sensitive=case_sensitive, attribute_to_creator=attribute_to_creator, mode=mode)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentsApi->pretranslate_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentPretranslateParameters**](DocumentPretranslateParameters.md)|  | 
 **auto_accept** | **bool**| Deprecated, use body param instead. Optional parameter for auto-accepting 100% TM hits. | [optional] 
 **case_sensitive** | **bool**| Deprecated, use body param instead. Optional for using case matching against TM hits. | [optional] 
 **attribute_to_creator** | **bool**| Deprecated, use body param instead. Optional parameter for attributing translation authorship of exact matches to document creator. | [optional] 
 **mode** | **str**| Deprecated, use body param instead. An optional parameter indicating how the document will be pretranslated.  The accepted values are &#x60;tm&#x60;, or &#x60;tm+mt&#x60;. Default is &#x60;tm&#x60;.  | [optional] 

### Return type

[**DocumentPretranslateResponse**](DocumentPretranslateResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | A status object. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_document**
> DocumentWithSegments update_document(body)

Update a Document

Update a Document. 

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
    api_instance = lilt.DocumentsApi(api_client)
    body = lilt.DocumentUpdateParameters() # DocumentUpdateParameters | 

    try:
        # Update a Document
        api_response = api_instance.update_document(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentsApi->update_document: %s\n" % e)
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
    api_instance = lilt.DocumentsApi(api_client)
    body = lilt.DocumentUpdateParameters() # DocumentUpdateParameters | 

    try:
        # Update a Document
        api_response = api_instance.update_document(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentsApi->update_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentUpdateParameters**](DocumentUpdateParameters.md)|  | 

### Return type

[**DocumentWithSegments**](DocumentWithSegments.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Document object. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_document**
> DocumentWithSegments upload_document(name, project_id, body, pretranslate=pretranslate, auto_accept=auto_accept, case_sensitive=case_sensitive, match_attribution=match_attribution, config_id=config_id)

Upload a File

Create a Document from a file in any of the formats [documented in our knowledge base](https://support.lilt.com/hc/en-us/articles/360020816253-File-Formats). Request parameters should be passed as JSON object with the header field `LILT-API`.  File names in the header can only contain [US-ASCII characters](https://en.wikipedia.org/wiki/ASCII). File names with characters outside of US-ASCII should be [URI encoded](https://en.wikipedia.org/wiki/Percent-encoding) or transliterated to US-ASCII strings.  Example CURL command: ```   curl -X POST https://lilt.com/2/documents/files?key=API_KEY \\   --header \"LILT-API: {\\\"name\\\": \\\"introduction.xliff\\\",\\\"pretranslate\\\": \\\"tm+mt\\\",\\\"project_id\\\": 9}\" \\   --header \"Content-Type: application/octet-stream\" \\   --data-binary @Introduction.xliff ```  

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
    api_instance = lilt.DocumentsApi(api_client)
    name = 'name_example' # str | A file name.
project_id = 56 # int | A unique Project identifier.
body = '/path/to/file' # file | The file contents to be uploaded. The entire POST body will be treated as the file. 
pretranslate = 'pretranslate_example' # str | An optional parameter indicating if and how the document will be pretranslated upon being uploaded. The accepted values are `TM`, or `TM+MT`  (optional)
auto_accept = True # bool | An optional parameter to auto-accept segments with 100% translation memory matches when the `pretranslate` option is also set, or to auto-accept any target data that is present when the uploaded file is XLIFF. If omitted or set to `false`, no segments will be auto-accepted.  (optional)
case_sensitive = True # bool | An optional parameter to use case sensitive translation memory matching when the `pretranslate` option is also enabled. Matches must have identical character-by-character case to qualify as matches. Default value is `false`  (optional)
match_attribution = True # bool | An optional parameter to attribute translation authorship of exact matches to the author of the file when the `pretranslate` option is also enabled. Default value is `false`  (optional)
config_id = 56 # int | An optional pararameter to specify an import configuration to be applied when extracting translatable content from this file.  (optional)

    try:
        # Upload a File
        api_response = api_instance.upload_document(name, project_id, body, pretranslate=pretranslate, auto_accept=auto_accept, case_sensitive=case_sensitive, match_attribution=match_attribution, config_id=config_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentsApi->upload_document: %s\n" % e)
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
    api_instance = lilt.DocumentsApi(api_client)
    name = 'name_example' # str | A file name.
project_id = 56 # int | A unique Project identifier.
body = '/path/to/file' # file | The file contents to be uploaded. The entire POST body will be treated as the file. 
pretranslate = 'pretranslate_example' # str | An optional parameter indicating if and how the document will be pretranslated upon being uploaded. The accepted values are `TM`, or `TM+MT`  (optional)
auto_accept = True # bool | An optional parameter to auto-accept segments with 100% translation memory matches when the `pretranslate` option is also set, or to auto-accept any target data that is present when the uploaded file is XLIFF. If omitted or set to `false`, no segments will be auto-accepted.  (optional)
case_sensitive = True # bool | An optional parameter to use case sensitive translation memory matching when the `pretranslate` option is also enabled. Matches must have identical character-by-character case to qualify as matches. Default value is `false`  (optional)
match_attribution = True # bool | An optional parameter to attribute translation authorship of exact matches to the author of the file when the `pretranslate` option is also enabled. Default value is `false`  (optional)
config_id = 56 # int | An optional pararameter to specify an import configuration to be applied when extracting translatable content from this file.  (optional)

    try:
        # Upload a File
        api_response = api_instance.upload_document(name, project_id, body, pretranslate=pretranslate, auto_accept=auto_accept, case_sensitive=case_sensitive, match_attribution=match_attribution, config_id=config_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentsApi->upload_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| A file name. | 
 **project_id** | **int**| A unique Project identifier. | 
 **body** | **file**| The file contents to be uploaded. The entire POST body will be treated as the file.  | 
 **pretranslate** | **str**| An optional parameter indicating if and how the document will be pretranslated upon being uploaded. The accepted values are &#x60;TM&#x60;, or &#x60;TM+MT&#x60;  | [optional] 
 **auto_accept** | **bool**| An optional parameter to auto-accept segments with 100% translation memory matches when the &#x60;pretranslate&#x60; option is also set, or to auto-accept any target data that is present when the uploaded file is XLIFF. If omitted or set to &#x60;false&#x60;, no segments will be auto-accepted.  | [optional] 
 **case_sensitive** | **bool**| An optional parameter to use case sensitive translation memory matching when the &#x60;pretranslate&#x60; option is also enabled. Matches must have identical character-by-character case to qualify as matches. Default value is &#x60;false&#x60;  | [optional] 
 **match_attribution** | **bool**| An optional parameter to attribute translation authorship of exact matches to the author of the file when the &#x60;pretranslate&#x60; option is also enabled. Default value is &#x60;false&#x60;  | [optional] 
 **config_id** | **int**| An optional pararameter to specify an import configuration to be applied when extracting translatable content from this file.  | [optional] 

### Return type

[**DocumentWithSegments**](DocumentWithSegments.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Document object. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

