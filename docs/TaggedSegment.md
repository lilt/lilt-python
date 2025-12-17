# TaggedSegment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_tagged** | **str** | The tagged source string. | [optional] 
**target_tagged** | **str** | The tagged target string. | [optional] 

## Example

```python
from lilt.models.tagged_segment import TaggedSegment

# TODO update the JSON string below
json = "{}"
# create an instance of TaggedSegment from a JSON string
tagged_segment_instance = TaggedSegment.from_json(json)
# print the JSON string representation of the object
print(TaggedSegment.to_json())

# convert the object into a dict
tagged_segment_dict = tagged_segment_instance.to_dict()
# create an instance of TaggedSegment from a dict
tagged_segment_from_dict = TaggedSegment.from_dict(tagged_segment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


