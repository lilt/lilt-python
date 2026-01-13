# InitiateMultipartUploadBodyMetadata

Optional file metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** | The size of the file to upload in bytes. | [optional] 
**category** | **str** | File category. | [optional] 
**uuid** | **str** | File UUID. | [optional] 
**labels** | **List[str]** | Array of label names to be added to the file after upload completes. | [optional] 

## Example

```python
from lilt.models.initiate_multipart_upload_body_metadata import InitiateMultipartUploadBodyMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of InitiateMultipartUploadBodyMetadata from a JSON string
initiate_multipart_upload_body_metadata_instance = InitiateMultipartUploadBodyMetadata.from_json(json)
# print the JSON string representation of the object
print(InitiateMultipartUploadBodyMetadata.to_json())

# convert the object into a dict
initiate_multipart_upload_body_metadata_dict = initiate_multipart_upload_body_metadata_instance.to_dict()
# create an instance of InitiateMultipartUploadBodyMetadata from a dict
initiate_multipart_upload_body_metadata_from_dict = InitiateMultipartUploadBodyMetadata.from_dict(initiate_multipart_upload_body_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


