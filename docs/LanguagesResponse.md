# LanguagesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_to_target** | **object** | A two-dimensional object in which the first key is an ISO 639-1 language code indicating the source, and the second key is an ISO 639-1 language code indicating the target. | [optional] 
**code_to_name** | **object** | An object in which the key is an ISO 639-1 language code, and the value is the language name. | [optional] 

## Example

```python
from lilt.models.languages_response import LanguagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LanguagesResponse from a JSON string
languages_response_instance = LanguagesResponse.from_json(json)
# print the JSON string representation of the object
print(LanguagesResponse.to_json())

# convert the object into a dict
languages_response_dict = languages_response_instance.to_dict()
# create an instance of LanguagesResponse from a dict
languages_response_from_dict = LanguagesResponse.from_dict(languages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


