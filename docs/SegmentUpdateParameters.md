# SegmentUpdateParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique Segment identifier. | 
**target** | **str** | The target string. | 

## Example

```python
from lilt.models.segment_update_parameters import SegmentUpdateParameters

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentUpdateParameters from a JSON string
segment_update_parameters_instance = SegmentUpdateParameters.from_json(json)
# print the JSON string representation of the object
print(SegmentUpdateParameters.to_json())

# convert the object into a dict
segment_update_parameters_dict = segment_update_parameters_instance.to_dict()
# create an instance of SegmentUpdateParameters from a dict
segment_update_parameters_from_dict = SegmentUpdateParameters.from_dict(segment_update_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


