# Memory

A Memory is a collection of parallel (source/target) segments from which a MT/TM model is trained. When a translator confirms a segment in the Interface, a parallel segment is added to the Memory. Parallel segments from existing translation memories and bitexts can also be added to the Memory via the REST API. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique number identifying the Memory. | [optional] 
**srclang** | **str** | An ISO 639-1 language identifier. | [optional] 
**trglang** | **str** | An ISO 639-1 language identifier. | [optional] 
**srclocale** | **str** | An ISO 639-1 language identifier. | [optional] 
**trglocale** | **str** | An ISO 639-1 language identifier. | [optional] 
**name** | **str** | A name for the Memory. | [optional] 
**is_processing** | **bool** | Indicates the memory is being processed. | [optional] 
**version** | **int** | The current version of the Memory, which is the number of updates since the memory was created. | [optional] 
**created_at** | **int** | Time at which the object was created. Measured in seconds since the Unix epoch. | [optional] 
**updated_at** | **int** | Time at which the object was created. Measured in seconds since the Unix epoch. | [optional] 
**resources** | **List[str]** | The resource files (translation memories and termbases) associated with this Memory. | [optional] 

## Example

```python
from lilt.models.memory import Memory

# TODO update the JSON string below
json = "{}"
# create an instance of Memory from a JSON string
memory_instance = Memory.from_json(json)
# print the JSON string representation of the object
print(Memory.to_json())

# convert the object into a dict
memory_dict = memory_instance.to_dict()
# create an instance of Memory from a dict
memory_from_dict = Memory.from_dict(memory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


