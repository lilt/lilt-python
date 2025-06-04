# TranslationList

An ranked list of translations and associated metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**untokenized_source** | **str** | The untokenized source segment. Punctuation has not been separated from words. | [optional] 
**tokenized_source** | **str** | The tokenized source segment. Punctuation has been separated from words. | [optional] 
**source_delimiters** | **List[str]** | A format string that indicates, for each word, if the word should be preceded by a space. | [optional] 
**translation** | [**List[Translation]**](Translation.md) | A list of Translation objects. | [optional] 

## Example

```python
from lilt.models.translation_list import TranslationList

# TODO update the JSON string below
json = "{}"
# create an instance of TranslationList from a JSON string
translation_list_instance = TranslationList.from_json(json)
# print the JSON string representation of the object
print(TranslationList.to_json())

# convert the object into a dict
translation_list_dict = translation_list_instance.to_dict()
# create an instance of TranslationList from a dict
translation_list_from_dict = TranslationList.from_dict(translation_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


