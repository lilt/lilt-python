# SegmentDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique Segment identifier. | [optional] 
**deleted** | **bool** | If the operation succeeded, then &#x60;true&#x60;. Otherwise, &#x60;false&#x60;. | [optional] 

## Example

```python
from lilt.models.segment_delete_response import SegmentDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentDeleteResponse from a JSON string
segment_delete_response_instance = SegmentDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(SegmentDeleteResponse.to_json())

# convert the object into a dict
segment_delete_response_dict = segment_delete_response_instance.to_dict()
# create an instance of SegmentDeleteResponse from a dict
segment_delete_response_from_dict = SegmentDeleteResponse.from_dict(segment_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


