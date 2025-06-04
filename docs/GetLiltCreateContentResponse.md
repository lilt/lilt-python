# GetLiltCreateContentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contents** | [**List[LiltCreateContent]**](LiltCreateContent.md) | List of LiltCreateContent objects | [optional] 

## Example

```python
from lilt.models.get_lilt_create_content_response import GetLiltCreateContentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetLiltCreateContentResponse from a JSON string
get_lilt_create_content_response_instance = GetLiltCreateContentResponse.from_json(json)
# print the JSON string representation of the object
print(GetLiltCreateContentResponse.to_json())

# convert the object into a dict
get_lilt_create_content_response_dict = get_lilt_create_content_response_instance.to_dict()
# create an instance of GetLiltCreateContentResponse from a dict
get_lilt_create_content_response_from_dict = GetLiltCreateContentResponse.from_dict(get_lilt_create_content_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


