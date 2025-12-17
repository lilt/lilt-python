# CompleteMultipartUpload200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Upload completion status | [optional] 
**location** | **str** | Final file location | [optional] 

## Example

```python
from lilt.models.complete_multipart_upload200_response import CompleteMultipartUpload200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CompleteMultipartUpload200Response from a JSON string
complete_multipart_upload200_response_instance = CompleteMultipartUpload200Response.from_json(json)
# print the JSON string representation of the object
print(CompleteMultipartUpload200Response.to_json())

# convert the object into a dict
complete_multipart_upload200_response_dict = complete_multipart_upload200_response_instance.to_dict()
# create an instance of CompleteMultipartUpload200Response from a dict
complete_multipart_upload200_response_from_dict = CompleteMultipartUpload200Response.from_dict(complete_multipart_upload200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


