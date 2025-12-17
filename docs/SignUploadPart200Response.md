# SignUploadPart200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Pre-signed URL for this part upload | [optional] 
**method** | **str** | HTTP method to use for upload | [optional] 

## Example

```python
from lilt.models.sign_upload_part200_response import SignUploadPart200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SignUploadPart200Response from a JSON string
sign_upload_part200_response_instance = SignUploadPart200Response.from_json(json)
# print the JSON string representation of the object
print(SignUploadPart200Response.to_json())

# convert the object into a dict
sign_upload_part200_response_dict = sign_upload_part200_response_instance.to_dict()
# create an instance of SignUploadPart200Response from a dict
sign_upload_part200_response_from_dict = SignUploadPart200Response.from_dict(sign_upload_part200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


