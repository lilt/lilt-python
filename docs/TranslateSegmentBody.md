# TranslateSegmentBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | A unique Segment identifier. | [optional] 
**memory_id** | **int** | A unique Memory identifier. | 
**source_hash** | **int** | A source hash code. | [optional] 
**n** | **int** | Return top n translations (deprecated). | [optional] 
**prefix** | **str** | A target prefix | [optional] 
**rich** | **bool** | Returns rich translation information (e.g., with word alignments). | [optional] [default to False]
**tm_matches** | **bool** | Include translation memory fuzzy matches. | [optional] [default to True]
**project_tags** | **bool** | Project tags. Projects tags in source to target if set to true. | [optional] [default to False]
**contains_icu_data** | **bool** | Contains ICU data. If true then tags in the source following the ICU standard will be parsed and retained. | [optional] [default to False]

## Example

```python
from lilt.models.translate_segment_body import TranslateSegmentBody

# TODO update the JSON string below
json = "{}"
# create an instance of TranslateSegmentBody from a JSON string
translate_segment_body_instance = TranslateSegmentBody.from_json(json)
# print the JSON string representation of the object
print(TranslateSegmentBody.to_json())

# convert the object into a dict
translate_segment_body_dict = translate_segment_body_instance.to_dict()
# create an instance of TranslateSegmentBody from a dict
translate_segment_body_from_dict = TranslateSegmentBody.from_dict(translate_segment_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


