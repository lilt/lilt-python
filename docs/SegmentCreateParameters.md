# SegmentCreateParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory_id** | **int** | A unique Memory identifier. | [optional] 
**document_id** | **int** | A unique Document identifier. | [optional] 
**source** | **str** | The source string. | 
**target** | **str** | The target string. | [optional] 
**should_apply_segmentation** | **bool** | A flag for whether this segment should be broken down into smaller segments. If this is true then the response is an array of segments. | [optional] 
**src_lang** | **str** | A two letter language code for the source language. Required if &#x60;shouldApplySegmentation&#x60; is enabled. | [optional] 

## Example

```python
from lilt.models.segment_create_parameters import SegmentCreateParameters

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentCreateParameters from a JSON string
segment_create_parameters_instance = SegmentCreateParameters.from_json(json)
# print the JSON string representation of the object
print(SegmentCreateParameters.to_json())

# convert the object into a dict
segment_create_parameters_dict = segment_create_parameters_instance.to_dict()
# create an instance of SegmentCreateParameters from a dict
segment_create_parameters_from_dict = SegmentCreateParameters.from_dict(segment_create_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


