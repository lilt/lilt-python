# AddFileLabelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Label name. | [optional] 

## Example

```python
from lilt.models.add_file_label_request import AddFileLabelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddFileLabelRequest from a JSON string
add_file_label_request_instance = AddFileLabelRequest.from_json(json)
# print the JSON string representation of the object
print(AddFileLabelRequest.to_json())

# convert the object into a dict
add_file_label_request_dict = add_file_label_request_instance.to_dict()
# create an instance of AddFileLabelRequest from a dict
add_file_label_request_from_dict = AddFileLabelRequest.from_dict(add_file_label_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


