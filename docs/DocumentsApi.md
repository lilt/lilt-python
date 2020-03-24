# lilt.DocumentsApi

All URIs are relative to *https://lilt.com/2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_document**](DocumentsApi.md#assign_document) | **PUT** /documents/share | Assign a Document
[**create_document**](DocumentsApi.md#create_document) | **POST** /documents | Create a Document
[**delete_document**](DocumentsApi.md#delete_document) | **DELETE** /documents | Delete a Document
[**download_file**](DocumentsApi.md#download_file) | **GET** /documents/files | Download a File
[**get_document**](DocumentsApi.md#get_document) | **GET** /documents | Retrieve a Document
[**pretranslate_document**](DocumentsApi.md#pretranslate_document) | **POST** /documents/pretranslate | Pretranslate a Document
[**update_document**](DocumentsApi.md#update_document) | **PUT** /documents | Update a Document
[**upload_document_file**](DocumentsApi.md#upload_document_file) | **POST** /documents/files | Upload a File

# **assign_document**
> object assign_document(body)

Assign a Document

Assign and unassign a Document for translation and/or review.  

### Example
```python
from __future__ import print_function
import time
import lilt
from lilt.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = lilt.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'# Configure HTTP basic authorization: BasicAuth
configuration = lilt.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = lilt.DocumentsApi(lilt.ApiClient(configuration))
body = NULL # object | Attributes of the Document resource to assign.

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
 **body** | [**object**](object.md)| Attributes of the Document resource to assign. | 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_document**
> DocumentWithSegments create_document(body=body)

Create a Document

Create a new Document. A Document is a collection of one or more Segments. Documents are nested inside of Projects, and appear in the Project details view in the web app. Document-level relationships between Segments are considered by the machine translation system during adaptation. If there is no inherent document structure in your data, you still might consider grouping related Segments into Documents to improve translation quality. 

### Example
```python
from __future__ import print_function
import time
import lilt
from lilt.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = lilt.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'# Configure HTTP basic authorization: BasicAuth
configuration = lilt.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = lilt.DocumentsApi(lilt.ApiClient(configuration))
body = NULL # object | The Document resource to create. (optional)

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
 **body** | [**object**](object.md)| The Document resource to create. | [optional] 

### Return type

[**DocumentWithSegments**](DocumentWithSegments.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document**
> object delete_document(id)

Delete a Document

Delete a Document. 

### Example
```python
from __future__ import print_function
import time
import lilt
from lilt.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = lilt.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'# Configure HTTP basic authorization: BasicAuth
configuration = lilt.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = lilt.DocumentsApi(lilt.ApiClient(configuration))
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

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file**
> str download_file(id, is_xliff=is_xliff)

Download a File

Export a Document that has been translated in the Lilt web application. Any Document can be downloaded in XLIFF 1.2 format, or can be retrieved in its original uploaded format by setting `is_xliff=false`. This endpoint will fail if either (a) export or (b) pre-translation operations are in-progress. The status of those operations can be determined by retrieving the Document resource. Example CURL command: ```   curl -X GET https://lilt.com/2/documents/files?key=API_KEY&id=274 -o from_lilt.xliff ```  

### Example
```python
from __future__ import print_function
import time
import lilt
from lilt.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = lilt.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'# Configure HTTP basic authorization: BasicAuth
configuration = lilt.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = lilt.DocumentsApi(lilt.ApiClient(configuration))
id = 56 # int | An unique Document identifier.
is_xliff = true # bool | Download the document in XLIFF 1.2 format. (optional)

try:
    # Download a File
    api_response = api_instance.download_file(id, is_xliff=is_xliff)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->download_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| An unique Document identifier. | 
 **is_xliff** | **bool**| Download the document in XLIFF 1.2 format. | [optional] 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document**
> DocumentWithSegments get_document(id, with_segments=with_segments)

Retrieve a Document

List a Document.  The listing will include the pretranslation status for the document. When pretranslation is in progress for a document, the `GET /documents` endpoint's response will include `is_pretranslating = true` as well as a more detailed status property `status.pretranslation` one of `idle`, `pending`, or `running`.

### Example
```python
from __future__ import print_function
import time
import lilt
from lilt.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = lilt.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'# Configure HTTP basic authorization: BasicAuth
configuration = lilt.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = lilt.DocumentsApi(lilt.ApiClient(configuration))
id = 56 # int | A unique Document identifier.
with_segments = true # bool | Flag indicating whether full segment information should be returned. (optional)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pretranslate_document**
> object pretranslate_document(body, case_sensitive=case_sensitive, auto_accept=auto_accept)

Pretranslate a Document

Initiate pretranslation of a list of Documents. This request will mark document(s) as being pretranslated. Pretranslation in this context is: - Applying and confirming exact TM matches based on the Memory of the Project; - Translating all other segments via MT without confirming them.  Example cURL command: ``` curl -X POST https://lilt.com/2/documents/pretranslate?key=API_KEY -d {\"id\": [123]} -H \"Content-Type: application/json\" ```  Document translation is an asynchronous process that, in effect, is performed in the background.  To check the status of pretranslation for a document, use the `GET /documents` endpoint. When pretranslation is in progress for a document, the `GET /documents` endpoint's response will include `is_pretranslating = true` as well as a more detailed status property `status.pretranslation` one of `idle`, `pending`, or `running`.  Once pretranslation is finished, the document can be downloaded via `GET /documents/files`. 

### Example
```python
from __future__ import print_function
import time
import lilt
from lilt.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = lilt.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'# Configure HTTP basic authorization: BasicAuth
configuration = lilt.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = lilt.DocumentsApi(lilt.ApiClient(configuration))
body = NULL # object | A list of unique Document identifiers.
case_sensitive = true # bool | Optional for using case matching against TM hits. (optional)
auto_accept = true # bool | Optional parameter for auto-accepting 100% TM hits. (optional)

try:
    # Pretranslate a Document
    api_response = api_instance.pretranslate_document(body, case_sensitive=case_sensitive, auto_accept=auto_accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->pretranslate_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| A list of unique Document identifiers. | 
 **case_sensitive** | **bool**| Optional for using case matching against TM hits. | [optional] 
 **auto_accept** | **bool**| Optional parameter for auto-accepting 100% TM hits. | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_document**
> DocumentWithSegments update_document(body)

Update a Document

Update a Document. 

### Example
```python
from __future__ import print_function
import time
import lilt
from lilt.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = lilt.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'# Configure HTTP basic authorization: BasicAuth
configuration = lilt.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = lilt.DocumentsApi(lilt.ApiClient(configuration))
body = NULL # object | The Document resource to update.

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
 **body** | [**object**](object.md)| The Document resource to update. | 

### Return type

[**DocumentWithSegments**](DocumentWithSegments.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_document_file**
> DocumentWithSegments upload_document_file(body, name, project_id, pretranslate=pretranslate, auto_accept=auto_accept)

Upload a File

Create a Document from a file in any of the formats [documented in our knowledge base](https://support.lilt.com/hc/en-us/articles/360020816253-File-Formats). Request parameters should be passed as JSON object with the header  field `LILT-API`. Example CURL command: ```   curl -X POST https://lilt.com/2/documents/files?key=API_KEY \\   --header \"LILT-API: {\\\"name\\\": \\\"introduction.xliff\\\",\\\"pretranslate\\\": \\\"tm+mt\\\",\\\"project_id\\\": 9}\" \\   --header \"Content-Type: application/octet-stream\" \\   --data-binary @Introduction.xliff ```  

### Example
```python
from __future__ import print_function
import time
import lilt
from lilt.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = lilt.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'# Configure HTTP basic authorization: BasicAuth
configuration = lilt.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = lilt.DocumentsApi(lilt.ApiClient(configuration))
body = 'body_example' # str | The file contents to be uploaded. The entire POST body will be
treated as the file.

name = 'name_example' # str | A file name.
project_id = 56 # int | A unique Project identifier.
pretranslate = 'pretranslate_example' # str | An optional parameter indicating if and how the document will be pretranslated upon being uploaded.  The accepted values are `null`, `tm`, or `tm+mt`  (optional)
auto_accept = true # bool | An optional parameter to auto-accept segments with 100% translation memory matches when the `pretranslate` option is also set, or to auto-accept any target data that is present when the uploaded file is XLIFF. If omitted or set to `false`, no segments will be auto-accepted.  (optional)

try:
    # Upload a File
    api_response = api_instance.upload_document_file(body, name, project_id, pretranslate=pretranslate, auto_accept=auto_accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->upload_document_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| The file contents to be uploaded. The entire POST body will be
treated as the file.
 | 
 **name** | **str**| A file name. | 
 **project_id** | **int**| A unique Project identifier. | 
 **pretranslate** | **str**| An optional parameter indicating if and how the document will be pretranslated upon being uploaded.  The accepted values are &#x60;null&#x60;, &#x60;tm&#x60;, or &#x60;tm+mt&#x60;  | [optional] 
 **auto_accept** | **bool**| An optional parameter to auto-accept segments with 100% translation memory matches when the &#x60;pretranslate&#x60; option is also set, or to auto-accept any target data that is present when the uploaded file is XLIFF. If omitted or set to &#x60;false&#x60;, no segments will be auto-accepted.  | [optional] 

### Return type

[**DocumentWithSegments**](DocumentWithSegments.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

