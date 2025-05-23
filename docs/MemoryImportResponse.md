# MemoryImportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique Memory identifier. | [optional] 
**is_processing** | **int** | The current state of the import. | [optional] 

## Example

```python
from lilt.models.memory_import_response import MemoryImportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MemoryImportResponse from a JSON string
memory_import_response_instance = MemoryImportResponse.from_json(json)
# print the JSON string representation of the object
print(MemoryImportResponse.to_json())

# convert the object into a dict
memory_import_response_dict = memory_import_response_instance.to_dict()
# create an instance of MemoryImportResponse from a dict
memory_import_response_from_dict = MemoryImportResponse.from_dict(memory_import_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


