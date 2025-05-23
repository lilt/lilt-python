# SignLiltCreateTermsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signed_agreement** | **bool** | Whether or not the agreement has been signed. | [optional] 

## Example

```python
from lilt.models.sign_lilt_create_terms_response import SignLiltCreateTermsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SignLiltCreateTermsResponse from a JSON string
sign_lilt_create_terms_response_instance = SignLiltCreateTermsResponse.from_json(json)
# print the JSON string representation of the object
print(SignLiltCreateTermsResponse.to_json())

# convert the object into a dict
sign_lilt_create_terms_response_dict = sign_lilt_create_terms_response_instance.to_dict()
# create an instance of SignLiltCreateTermsResponse from a dict
sign_lilt_create_terms_response_from_dict = SignLiltCreateTermsResponse.from_dict(sign_lilt_create_terms_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


