# CompleteMultipartUploadBodyPartsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e_tag** | **str** | ETag of the uploaded part | 
**part_number** | **int** | Part number (1-based) | 

## Example

```python
from lilt.models.complete_multipart_upload_body_parts_inner import CompleteMultipartUploadBodyPartsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompleteMultipartUploadBodyPartsInner from a JSON string
complete_multipart_upload_body_parts_inner_instance = CompleteMultipartUploadBodyPartsInner.from_json(json)
# print the JSON string representation of the object
print(CompleteMultipartUploadBodyPartsInner.to_json())

# convert the object into a dict
complete_multipart_upload_body_parts_inner_dict = complete_multipart_upload_body_parts_inner_instance.to_dict()
# create an instance of CompleteMultipartUploadBodyPartsInner from a dict
complete_multipart_upload_body_parts_inner_from_dict = CompleteMultipartUploadBodyPartsInner.from_dict(complete_multipart_upload_body_parts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


