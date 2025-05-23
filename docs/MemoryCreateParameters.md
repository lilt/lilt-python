# MemoryCreateParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A name for the Memory. | 
**srclang** | **str** | An ISO 639-1 language identifier. | 
**trglang** | **str** | An ISO 639-1 language identifier. | 
**srclocale** | **str** | An ISO 3166-1 region name for language locales | [optional] 
**trglocale** | **str** | An ISO 3166-1 region name for language locales | [optional] 

## Example

```python
from lilt.models.memory_create_parameters import MemoryCreateParameters

# TODO update the JSON string below
json = "{}"
# create an instance of MemoryCreateParameters from a JSON string
memory_create_parameters_instance = MemoryCreateParameters.from_json(json)
# print the JSON string representation of the object
print(MemoryCreateParameters.to_json())

# convert the object into a dict
memory_create_parameters_dict = memory_create_parameters_instance.to_dict()
# create an instance of MemoryCreateParameters from a dict
memory_create_parameters_from_dict = MemoryCreateParameters.from_dict(memory_create_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


