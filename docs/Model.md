# Model


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the model. | [optional] 
**name** | **str** | The name of the model. | [optional] 
**provider** | **str** | The provider of the model. | [optional] 
**status** | **str** | The status of the model. | [optional] 
**src_lang** | **str** | The source language of the model. | [optional] 
**trg_lang** | **str** | The target language of the model. | [optional] 
**src_locale** | **str** | The source locale of the model. | [optional] 
**trg_locale** | **str** | The target locale of the model. | [optional] 

## Example

```python
from lilt.models.model import Model

# TODO update the JSON string below
json = "{}"
# create an instance of Model from a JSON string
model_instance = Model.from_json(json)
# print the JSON string representation of the object
print(Model.to_json())

# convert the object into a dict
model_dict = model_instance.to_dict()
# create an instance of Model from a dict
model_from_dict = Model.from_dict(model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


