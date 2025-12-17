# InitiateMultipartUploadBody

A single upload request object, or an array of upload request objects (max 100).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | A file name including file extension. | 
**type** | **str** | The content-type or mime-type of the file to upload. | 
**metadata** | [**InitiateMultipartUploadBodyMetadata**](InitiateMultipartUploadBodyMetadata.md) |  | [optional] 

## Example

```python
from lilt.models.initiate_multipart_upload_body import InitiateMultipartUploadBody

# TODO update the JSON string below
json = "{}"
# create an instance of InitiateMultipartUploadBody from a JSON string
initiate_multipart_upload_body_instance = InitiateMultipartUploadBody.from_json(json)
# print the JSON string representation of the object
print(InitiateMultipartUploadBody.to_json())

# convert the object into a dict
initiate_multipart_upload_body_dict = initiate_multipart_upload_body_instance.to_dict()
# create an instance of InitiateMultipartUploadBody from a dict
initiate_multipart_upload_body_from_dict = InitiateMultipartUploadBody.from_dict(initiate_multipart_upload_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


