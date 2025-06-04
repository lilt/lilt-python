# TranslationInfo

Information describing a batch translation process. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for this translation. | [optional] 
**file_id** | **int** | id of the File that is being translated. | [optional] 
**status** | **str** | Status of the translation - &#x60;InProgress&#x60;, &#x60;ReadyForDownload&#x60;, &#x60;Completed&#x60;, &#x60;Failed&#x60;. | [optional] 
**created_at** | **int** | Time when this translation was started, in seconds since the Unix epoch. | [optional] 
**error_msg** | **str** | Error message, present when status is &#x60;Failed&#x60;. | [optional] 

## Example

```python
from lilt.models.translation_info import TranslationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TranslationInfo from a JSON string
translation_info_instance = TranslationInfo.from_json(json)
# print the JSON string representation of the object
print(TranslationInfo.to_json())

# convert the object into a dict
translation_info_dict = translation_info_instance.to_dict()
# create an instance of TranslationInfo from a dict
translation_info_from_dict = TranslationInfo.from_dict(translation_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


