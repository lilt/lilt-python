# LiltCreateContent

Content Parameters for LiltCreate. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A name for the request content. | [optional] 
**id** | **int** | A unique identifier for the generated content. | [optional] 
**language** | **str** | The language of the content. | 
**template** | **str** | The template of the content. | 
**template_params** | [**LiltCreateContentTemplateParams**](LiltCreateContentTemplateParams.md) |  | 
**preferences** | [**LiltCreateContentPreferences**](LiltCreateContentPreferences.md) |  | [optional] 

## Example

```python
from lilt.models.lilt_create_content import LiltCreateContent

# TODO update the JSON string below
json = "{}"
# create an instance of LiltCreateContent from a JSON string
lilt_create_content_instance = LiltCreateContent.from_json(json)
# print the JSON string representation of the object
print(LiltCreateContent.to_json())

# convert the object into a dict
lilt_create_content_dict = lilt_create_content_instance.to_dict()
# create an instance of LiltCreateContent from a dict
lilt_create_content_from_dict = LiltCreateContent.from_dict(lilt_create_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


