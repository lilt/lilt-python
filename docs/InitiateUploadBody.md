# InitiateUploadBody

A single upload request object, or an array of upload request objects (max 100).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | A file name including file extension. | 
**type** | **str** | The content-type or mime-type of the file to upload. | 
**metadata** | [**InitiateUploadBodyMetadata**](InitiateUploadBodyMetadata.md) |  | [optional] 

## Example

```python
from lilt.models.initiate_upload_body import InitiateUploadBody

# TODO update the JSON string below
json = "{}"
# create an instance of InitiateUploadBody from a JSON string
initiate_upload_body_instance = InitiateUploadBody.from_json(json)
# print the JSON string representation of the object
print(InitiateUploadBody.to_json())

# convert the object into a dict
initiate_upload_body_dict = initiate_upload_body_instance.to_dict()
# create an instance of InitiateUploadBody from a dict
initiate_upload_body_from_dict = InitiateUploadBody.from_dict(initiate_upload_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


