# SegmentDoneResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_ids** | **List[float]** | array of segment ids | 

## Example

```python
from lilt.models.segment_done_response import SegmentDoneResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentDoneResponse from a JSON string
segment_done_response_instance = SegmentDoneResponse.from_json(json)
# print the JSON string representation of the object
print(SegmentDoneResponse.to_json())

# convert the object into a dict
segment_done_response_dict = segment_done_response_instance.to_dict()
# create an instance of SegmentDoneResponse from a dict
segment_done_response_from_dict = SegmentDoneResponse.from_dict(segment_done_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


