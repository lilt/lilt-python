# GetPendingUploads200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique upload identifier | [optional] 
**filename** | **str** | Name of the uploaded file | [optional] 
**status** | **str** | Current upload status | [optional] 
**created_at** | **datetime** | Upload creation timestamp | [optional] 

## Example

```python
from lilt.models.get_pending_uploads200_response_inner import GetPendingUploads200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetPendingUploads200ResponseInner from a JSON string
get_pending_uploads200_response_inner_instance = GetPendingUploads200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetPendingUploads200ResponseInner.to_json())

# convert the object into a dict
get_pending_uploads200_response_inner_dict = get_pending_uploads200_response_inner_instance.to_dict()
# create an instance of GetPendingUploads200ResponseInner from a dict
get_pending_uploads200_response_inner_from_dict = GetPendingUploads200ResponseInner.from_dict(get_pending_uploads200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


