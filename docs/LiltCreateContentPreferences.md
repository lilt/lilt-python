# LiltCreateContentPreferences

The preferences of the content.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tone** | **str** | The tone of the content. | [optional] 
**styleguide** | **str** | The styleguide of the content. | [optional] 

## Example

```python
from lilt.models.lilt_create_content_preferences import LiltCreateContentPreferences

# TODO update the JSON string below
json = "{}"
# create an instance of LiltCreateContentPreferences from a JSON string
lilt_create_content_preferences_instance = LiltCreateContentPreferences.from_json(json)
# print the JSON string representation of the object
print(LiltCreateContentPreferences.to_json())

# convert the object into a dict
lilt_create_content_preferences_dict = lilt_create_content_preferences_instance.to_dict()
# create an instance of LiltCreateContentPreferences from a dict
lilt_create_content_preferences_from_dict = LiltCreateContentPreferences.from_dict(lilt_create_content_preferences_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


