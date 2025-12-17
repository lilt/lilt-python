# CompleteMultipartUploadBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parts** | [**List[CompleteMultipartUploadBodyPartsInner]**](CompleteMultipartUploadBodyPartsInner.md) | Array of completed upload parts. | 

## Example

```python
from lilt.models.complete_multipart_upload_body import CompleteMultipartUploadBody

# TODO update the JSON string below
json = "{}"
# create an instance of CompleteMultipartUploadBody from a JSON string
complete_multipart_upload_body_instance = CompleteMultipartUploadBody.from_json(json)
# print the JSON string representation of the object
print(CompleteMultipartUploadBody.to_json())

# convert the object into a dict
complete_multipart_upload_body_dict = complete_multipart_upload_body_instance.to_dict()
# create an instance of CompleteMultipartUploadBody from a dict
complete_multipart_upload_body_from_dict = CompleteMultipartUploadBody.from_dict(complete_multipart_upload_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


