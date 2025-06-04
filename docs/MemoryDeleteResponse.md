# MemoryDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique Memory identifier. | [optional] 
**deleted** | **bool** | If the operation succeeded, then &#x60;true&#x60;. Otherwise, &#x60;false&#x60;. | [optional] 

## Example

```python
from lilt.models.memory_delete_response import MemoryDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MemoryDeleteResponse from a JSON string
memory_delete_response_instance = MemoryDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(MemoryDeleteResponse.to_json())

# convert the object into a dict
memory_delete_response_dict = memory_delete_response_instance.to_dict()
# create an instance of MemoryDeleteResponse from a dict
memory_delete_response_from_dict = MemoryDeleteResponse.from_dict(memory_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


