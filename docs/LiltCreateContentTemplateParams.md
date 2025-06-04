# LiltCreateContentTemplateParams

The template parameters of the content.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_length** | **int** | The length of the content. | [optional] 
**memory_id** | **int** | The ID referencing a Data Source. | [optional] 
**language** | **str** | The language of the content. | 
**sections** | **List[str]** | The sections of the content. | [optional] 
**summary** | **str** | The summary of the content. | [optional] 

## Example

```python
from lilt.models.lilt_create_content_template_params import LiltCreateContentTemplateParams

# TODO update the JSON string below
json = "{}"
# create an instance of LiltCreateContentTemplateParams from a JSON string
lilt_create_content_template_params_instance = LiltCreateContentTemplateParams.from_json(json)
# print the JSON string representation of the object
print(LiltCreateContentTemplateParams.to_json())

# convert the object into a dict
lilt_create_content_template_params_dict = lilt_create_content_template_params_instance.to_dict()
# create an instance of LiltCreateContentTemplateParams from a dict
lilt_create_content_template_params_from_dict = LiltCreateContentTemplateParams.from_dict(lilt_create_content_template_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


