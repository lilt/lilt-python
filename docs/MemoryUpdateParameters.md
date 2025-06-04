# MemoryUpdateParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique Memory identifier. | 
**name** | **str** | The Memory name. | 

## Example

```python
from lilt.models.memory_update_parameters import MemoryUpdateParameters

# TODO update the JSON string below
json = "{}"
# create an instance of MemoryUpdateParameters from a JSON string
memory_update_parameters_instance = MemoryUpdateParameters.from_json(json)
# print the JSON string representation of the object
print(MemoryUpdateParameters.to_json())

# convert the object into a dict
memory_update_parameters_dict = memory_update_parameters_instance.to_dict()
# create an instance of MemoryUpdateParameters from a dict
memory_update_parameters_from_dict = MemoryUpdateParameters.from_dict(memory_update_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


