# LiltCreateContentRequest

Content Parameters for LiltCreate. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A name for the request content. | [optional] 
**language** | **str** | The language of the content. | 
**template** | **str** | The template of the content. | 
**template_params** | [**LiltCreateContentTemplateParams**](LiltCreateContentTemplateParams.md) |  | 
**preferences** | [**LiltCreateContentPreferences**](LiltCreateContentPreferences.md) |  | [optional] 

## Example

```python
from lilt.models.lilt_create_content_request import LiltCreateContentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LiltCreateContentRequest from a JSON string
lilt_create_content_request_instance = LiltCreateContentRequest.from_json(json)
# print the JSON string representation of the object
print(LiltCreateContentRequest.to_json())

# convert the object into a dict
lilt_create_content_request_dict = lilt_create_content_request_instance.to_dict()
# create an instance of LiltCreateContentRequest from a dict
lilt_create_content_request_from_dict = LiltCreateContentRequest.from_dict(lilt_create_content_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


