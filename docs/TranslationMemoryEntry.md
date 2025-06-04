# TranslationMemoryEntry

A translation memory entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | The source string. | [optional] 
**target** | **str** | The target string. Tags will be automatically placed according to the query string. | [optional] 
**score** | **int** | The fuzzy match score. | [optional] 
**metadata** | **object** | Attributes describing the translation memory entry. | [optional] 

## Example

```python
from lilt.models.translation_memory_entry import TranslationMemoryEntry

# TODO update the JSON string below
json = "{}"
# create an instance of TranslationMemoryEntry from a JSON string
translation_memory_entry_instance = TranslationMemoryEntry.from_json(json)
# print the JSON string representation of the object
print(TranslationMemoryEntry.to_json())

# convert the object into a dict
translation_memory_entry_dict = translation_memory_entry_instance.to_dict()
# create an instance of TranslationMemoryEntry from a dict
translation_memory_entry_from_dict = TranslationMemoryEntry.from_dict(translation_memory_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


