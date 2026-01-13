# CancelMultipartUpload200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Cancellation status | [optional] 
**message** | **str** | Cancellation message | [optional] 

## Example

```python
from lilt.models.cancel_multipart_upload200_response import CancelMultipartUpload200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CancelMultipartUpload200Response from a JSON string
cancel_multipart_upload200_response_instance = CancelMultipartUpload200Response.from_json(json)
# print the JSON string representation of the object
print(CancelMultipartUpload200Response.to_json())

# convert the object into a dict
cancel_multipart_upload200_response_dict = cancel_multipart_upload200_response_instance.to_dict()
# create an instance of CancelMultipartUpload200Response from a dict
cancel_multipart_upload200_response_from_dict = CancelMultipartUpload200Response.from_dict(cancel_multipart_upload200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


