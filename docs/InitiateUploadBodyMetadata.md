# InitiateUploadBodyMetadata

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
from lilt.models.initiate_upload_body_metadata import InitiateUploadBodyMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of InitiateUploadBodyMetadata from a JSON string
initiate_upload_body_metadata_instance = InitiateUploadBodyMetadata.from_json(json)
# print the JSON string representation of the object
print(InitiateUploadBodyMetadata.to_json())

# convert the object into a dict
initiate_upload_body_metadata_dict = initiate_upload_body_metadata_instance.to_dict()
# create an instance of InitiateUploadBodyMetadata from a dict
initiate_upload_body_metadata_from_dict = InitiateUploadBodyMetadata.from_dict(initiate_upload_body_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


