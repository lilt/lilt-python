# InitiateMultipartUpload200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload_id** | **str** | Multipart upload ID for subsequent part uploads | [optional] 
**key** | **str** | Upload key identifier | [optional] 

## Example

```python
from lilt.models.initiate_multipart_upload200_response import InitiateMultipartUpload200Response

# TODO update the JSON string below
json = "{}"
# create an instance of InitiateMultipartUpload200Response from a JSON string
initiate_multipart_upload200_response_instance = InitiateMultipartUpload200Response.from_json(json)
# print the JSON string representation of the object
print(InitiateMultipartUpload200Response.to_json())

# convert the object into a dict
initiate_multipart_upload200_response_dict = initiate_multipart_upload200_response_instance.to_dict()
# create an instance of InitiateMultipartUpload200Response from a dict
initiate_multipart_upload200_response_from_dict = InitiateMultipartUpload200Response.from_dict(initiate_multipart_upload200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


