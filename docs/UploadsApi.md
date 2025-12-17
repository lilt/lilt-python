# lilt.UploadsApi

All URIs are relative to *https://api.lilt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_multipart_upload**](UploadsApi.md#cancel_multipart_upload) | **DELETE** /v2/upload/s3/multipart/{uploadId} | Cancel Multipart Upload
[**complete_multipart_upload**](UploadsApi.md#complete_multipart_upload) | **POST** /v2/upload/s3/multipart/{uploadId}/complete | Complete Multipart Upload
[**get_pending_uploads**](UploadsApi.md#get_pending_uploads) | **GET** /v2/upload | Get All Pending Uploads or specific list of uploads by ids or statuses
[**get_s3_upload_params**](UploadsApi.md#get_s3_upload_params) | **GET** /v2/upload/s3/params | Get S3 Upload Parameters
[**get_upload_by_id**](UploadsApi.md#get_upload_by_id) | **GET** /v2/upload/{uploadId} | Get Upload by ID
[**initiate_multipart_upload**](UploadsApi.md#initiate_multipart_upload) | **POST** /v2/upload/s3/multipart | Initiate Multipart Upload
[**initiate_s3_upload**](UploadsApi.md#initiate_s3_upload) | **POST** /v2/upload/s3/params | Initiate File Upload to Cloud Storage
[**sign_upload_part**](UploadsApi.md#sign_upload_part) | **GET** /v2/upload/s3/multipart/{uploadId}/partNumber | Sign Upload Part


# **cancel_multipart_upload**
> CancelMultipartUpload200Response cancel_multipart_upload(upload_id, s3_key)

Cancel Multipart Upload

Cancel/abort a multipart upload and clean up any uploaded parts.

Example CURL command:
```
  curl -X DELETE "https://lilt.com/v2/upload/s3/multipart/abc123def456?key=API_KEY&key=uploads/user123/file456.zip"
```


### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.cancel_multipart_upload200_response import CancelMultipartUpload200Response
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
    api_instance = lilt.UploadsApi(api_client)
    upload_id = 'upload_id_example' # str | Multipart upload ID to cancel
    s3_key = 's3_key_example' # str | Upload key from initiate response

    try:
        # Cancel Multipart Upload
        api_response = api_instance.cancel_multipart_upload(upload_id, s3_key)
        print("The response of UploadsApi->cancel_multipart_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadsApi->cancel_multipart_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **str**| Multipart upload ID to cancel | 
 **s3_key** | **str**| Upload key from initiate response | 

### Return type

[**CancelMultipartUpload200Response**](CancelMultipartUpload200Response.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Upload cancellation confirmation. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete_multipart_upload**
> CompleteMultipartUpload200Response complete_multipart_upload(upload_id, s3_key, complete_multipart_upload_body)

Complete Multipart Upload

Complete a multipart upload by providing all uploaded parts information.

Example CURL command:
```
  curl -X POST "https://lilt.com/v2/upload/s3/multipart/abc123def456/complete?key=API_KEY&key=uploads/user123/file456.zip" \
  --header "Content-Type: application/json" \
  --data-raw '{
    "parts": [
      {"ETag": "etag1", "PartNumber": 1},
      {"ETag": "etag2", "PartNumber": 2}
    ]
  }'
```


### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.complete_multipart_upload200_response import CompleteMultipartUpload200Response
from lilt.models.complete_multipart_upload_body import CompleteMultipartUploadBody
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
    api_instance = lilt.UploadsApi(api_client)
    upload_id = 'upload_id_example' # str | Multipart upload ID from initiate response
    s3_key = 's3_key_example' # str | Upload key from initiate response
    complete_multipart_upload_body = lilt.CompleteMultipartUploadBody() # CompleteMultipartUploadBody | Information about uploaded parts.

    try:
        # Complete Multipart Upload
        api_response = api_instance.complete_multipart_upload(upload_id, s3_key, complete_multipart_upload_body)
        print("The response of UploadsApi->complete_multipart_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadsApi->complete_multipart_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **str**| Multipart upload ID from initiate response | 
 **s3_key** | **str**| Upload key from initiate response | 
 **complete_multipart_upload_body** | [**CompleteMultipartUploadBody**](CompleteMultipartUploadBody.md)| Information about uploaded parts. | 

### Return type

[**CompleteMultipartUpload200Response**](CompleteMultipartUpload200Response.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Upload completion confirmation. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pending_uploads**
> List[GetPendingUploads200ResponseInner] get_pending_uploads(ids=ids, statuses=statuses)

Get All Pending Uploads or specific list of uploads by ids or statuses

Retrieve all pending uploads for the current user and organization.

Example CURL command:
```
  curl -X GET https://lilt.com/2/upload?key=API_KEY
```


### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.get_pending_uploads200_response_inner import GetPendingUploads200ResponseInner
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
    api_instance = lilt.UploadsApi(api_client)
    ids = 'ids_example' # str | Comma-separated list of upload IDs to filter by. (optional)
    statuses = 'statuses_example' # str | Comma-separated list of upload statuses to filter by. (optional)

    try:
        # Get All Pending Uploads or specific list of uploads by ids or statuses
        api_response = api_instance.get_pending_uploads(ids=ids, statuses=statuses)
        print("The response of UploadsApi->get_pending_uploads:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadsApi->get_pending_uploads: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| Comma-separated list of upload IDs to filter by. | [optional] 
 **statuses** | **str**| Comma-separated list of upload statuses to filter by. | [optional] 

### Return type

[**List[GetPendingUploads200ResponseInner]**](GetPendingUploads200ResponseInner.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of pending uploads. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_s3_upload_params**
> GetS3UploadParams200Response get_s3_upload_params(filename, type, metadata_size=metadata_size, metadata_category=metadata_category, metadata_uuid=metadata_uuid, metadata_labels=metadata_labels)

Get S3 Upload Parameters

Get S3 upload parameters via query string. This endpoint provides the necessary information
to complete the file upload process using GET parameters.

Example CURL command:
```
  curl -X GET "https://lilt.com/v2/upload/s3/params?key=API_KEY&filename=example.json&type=application/json&metadata.size=1024&metadata.labels=important,review-needed"
```


### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.get_s3_upload_params200_response import GetS3UploadParams200Response
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
    api_instance = lilt.UploadsApi(api_client)
    filename = 'document.xliff' # str | A file name including file extension.
    type = 'video/mp4' # str | The content-type or mime-type of the file to upload.
    metadata_size = 1024 # int | The size of the file to upload in bytes. (optional)
    metadata_category = 'documents' # str | File category metadata. (optional)
    metadata_uuid = '123e4567-e89b-12d3-a456-426614174000' # str | File UUID metadata. (optional)
    metadata_labels = 'important,review-needed' # str | Comma-separated list of label names to be added to the file after upload completes. (optional)

    try:
        # Get S3 Upload Parameters
        api_response = api_instance.get_s3_upload_params(filename, type, metadata_size=metadata_size, metadata_category=metadata_category, metadata_uuid=metadata_uuid, metadata_labels=metadata_labels)
        print("The response of UploadsApi->get_s3_upload_params:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadsApi->get_s3_upload_params: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| A file name including file extension. | 
 **type** | **str**| The content-type or mime-type of the file to upload. | 
 **metadata_size** | **int**| The size of the file to upload in bytes. | [optional] 
 **metadata_category** | **str**| File category metadata. | [optional] 
 **metadata_uuid** | **str**| File UUID metadata. | [optional] 
 **metadata_labels** | **str**| Comma-separated list of label names to be added to the file after upload completes. | [optional] 

### Return type

[**GetS3UploadParams200Response**](GetS3UploadParams200Response.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Upload initialization information. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upload_by_id**
> GetPendingUploads200ResponseInner get_upload_by_id(upload_id)

Get Upload by ID

Retrieve a specific upload by its unique identifier.

Example CURL command:
```
  curl -X GET https://lilt.com/2/upload/12345?key=API_KEY
```


### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.get_pending_uploads200_response_inner import GetPendingUploads200ResponseInner
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
    api_instance = lilt.UploadsApi(api_client)
    upload_id = 56 # int | Unique upload identifier

    try:
        # Get Upload by ID
        api_response = api_instance.get_upload_by_id(upload_id)
        print("The response of UploadsApi->get_upload_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadsApi->get_upload_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **int**| Unique upload identifier | 

### Return type

[**GetPendingUploads200ResponseInner**](GetPendingUploads200ResponseInner.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Upload details. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initiate_multipart_upload**
> InitiateMultipartUpload200Response initiate_multipart_upload(initiate_multipart_upload_body)

Initiate Multipart Upload

Initiate a multipart upload for large files. This endpoint provides the necessary information
to start a multipart upload process.

Supports both single file and bulk upload requests. For bulk uploads, pass an array of upload
objects (maximum 100 items). The response format matches the request format - a single object
for single file requests, or an array for bulk requests.

Example CURL command (single file):
```
  curl -X POST https://lilt.com/v2/upload/s3/multipart?key=API_KEY \
  --header "Content-Type: application/json" \
  --data-raw '{
    "filename": "large-file.zip",
    "type": "application/zip",
    "metadata": {
      "size": 104857600
    }
  }'
```

Example CURL command (bulk upload):
```
  curl -X POST https://lilt.com/v2/upload/s3/multipart?key=API_KEY \
  --header "Content-Type: application/json" \
  --data-raw '[
    {
      "filename": "large-file1.zip",
      "type": "application/zip",
      "metadata": { "size": 104857600 }
    },
    {
      "filename": "large-file2.zip",
      "type": "application/zip",
      "metadata": { "size": 209715200 }
    }
  ]'
```


### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.initiate_multipart_upload200_response import InitiateMultipartUpload200Response
from lilt.models.initiate_multipart_upload_body import InitiateMultipartUploadBody
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
    api_instance = lilt.UploadsApi(api_client)
    initiate_multipart_upload_body = lilt.InitiateMultipartUploadBody() # InitiateMultipartUploadBody | Information about the file(s) to be uploaded. Can be a single object or an array of objects (max 100).  Single file request: `{ \"filename\": \"...\", \"type\": \"...\", \"metadata\": {...} }` Bulk request: `[{ \"filename\": \"...\", \"type\": \"...\", \"metadata\": {...} }, ...]` 

    try:
        # Initiate Multipart Upload
        api_response = api_instance.initiate_multipart_upload(initiate_multipart_upload_body)
        print("The response of UploadsApi->initiate_multipart_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadsApi->initiate_multipart_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **initiate_multipart_upload_body** | [**InitiateMultipartUploadBody**](InitiateMultipartUploadBody.md)| Information about the file(s) to be uploaded. Can be a single object or an array of objects (max 100).  Single file request: &#x60;{ \&quot;filename\&quot;: \&quot;...\&quot;, \&quot;type\&quot;: \&quot;...\&quot;, \&quot;metadata\&quot;: {...} }&#x60; Bulk request: &#x60;[{ \&quot;filename\&quot;: \&quot;...\&quot;, \&quot;type\&quot;: \&quot;...\&quot;, \&quot;metadata\&quot;: {...} }, ...]&#x60;  | 

### Return type

[**InitiateMultipartUpload200Response**](InitiateMultipartUpload200Response.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Multipart upload initialization information. Returns a single object for single file requests, or an array of objects for bulk requests.  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initiate_s3_upload**
> GetS3UploadParams200Response initiate_s3_upload(initiate_upload_body)

Initiate File Upload to Cloud Storage

Initiate the upload of a file to cloud storage. This endpoint provides the necessary information
to complete the file upload process.

Supports both single file and bulk upload requests. For bulk uploads, pass an array of upload
objects (maximum 100 items). The response format matches the request format - a single object
for single file requests, or an array for bulk requests.

Example CURL command (single file):
```
  curl -X POST https://lilt.com/v2/upload/s3/params?key=API_KEY \
  --header "Content-Type: application/json" \
  --data-raw '{
    "filename": "example.json",
    "type": "application/json",
    "metadata": {
      "size": 1024,
      "labels": ["important", "review-needed"]
    }
  }'
```

Example CURL command (bulk upload):
```
  curl -X POST https://lilt.com/v2/upload/s3/params?key=API_KEY \
  --header "Content-Type: application/json" \
  --data-raw '[
    {
      "filename": "file1.json",
      "type": "application/json",
      "metadata": { "size": 1024 }
    },
    {
      "filename": "file2.txt",
      "type": "text/plain",
      "metadata": { "size": 2048 }
    }
  ]'
```


### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.get_s3_upload_params200_response import GetS3UploadParams200Response
from lilt.models.initiate_upload_body import InitiateUploadBody
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
    api_instance = lilt.UploadsApi(api_client)
    initiate_upload_body = lilt.InitiateUploadBody() # InitiateUploadBody | Information about the file(s) to be uploaded. Can be a single object or an array of objects (max 100).  Single file request: `{ \"filename\": \"...\", \"type\": \"...\", \"metadata\": {...} }` Bulk request: `[{ \"filename\": \"...\", \"type\": \"...\", \"metadata\": {...} }, ...]` 

    try:
        # Initiate File Upload to Cloud Storage
        api_response = api_instance.initiate_s3_upload(initiate_upload_body)
        print("The response of UploadsApi->initiate_s3_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadsApi->initiate_s3_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **initiate_upload_body** | [**InitiateUploadBody**](InitiateUploadBody.md)| Information about the file(s) to be uploaded. Can be a single object or an array of objects (max 100).  Single file request: &#x60;{ \&quot;filename\&quot;: \&quot;...\&quot;, \&quot;type\&quot;: \&quot;...\&quot;, \&quot;metadata\&quot;: {...} }&#x60; Bulk request: &#x60;[{ \&quot;filename\&quot;: \&quot;...\&quot;, \&quot;type\&quot;: \&quot;...\&quot;, \&quot;metadata\&quot;: {...} }, ...]&#x60;  | 

### Return type

[**GetS3UploadParams200Response**](GetS3UploadParams200Response.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Upload initialization information. Returns a single object for single file requests, or an array of objects for bulk requests.  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sign_upload_part**
> SignUploadPart200Response sign_upload_part(upload_id, part_number, s3_key, size)

Sign Upload Part

Get a signed URL for uploading a specific part of a multipart upload.

Make sure to set the part size to 8MB (8388608 bytes).

Example CURL command:
```
  curl -X GET "https://lilt.com/v2/upload/s3/multipart/abc123def456/1?key=API_KEY&key=uploads/user123/file456.zip&size=5242880"
```


### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import lilt
from lilt.models.sign_upload_part200_response import SignUploadPart200Response
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
    api_instance = lilt.UploadsApi(api_client)
    upload_id = 'upload_id_example' # str | Multipart upload ID from initiate response
    part_number = 56 # int | Part number (1-based)
    s3_key = 's3_key_example' # str | Upload key from initiate response
    size = 56 # int | Size of this part in bytes

    try:
        # Sign Upload Part
        api_response = api_instance.sign_upload_part(upload_id, part_number, s3_key, size)
        print("The response of UploadsApi->sign_upload_part:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadsApi->sign_upload_part: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **str**| Multipart upload ID from initiate response | 
 **part_number** | **int**| Part number (1-based) | 
 **s3_key** | **str**| Upload key from initiate response | 
 **size** | **int**| Size of this part in bytes | 

### Return type

[**SignUploadPart200Response**](SignUploadPart200Response.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Signed URL for part upload. |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

