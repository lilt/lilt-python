# ProjectDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique Project identifier. | [optional] 
**deleted** | **bool** | If the operation succeeded, then &#x60;true&#x60;. Otherwise, &#x60;false&#x60;. | [optional] 

## Example

```python
from lilt.models.project_delete_response import ProjectDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDeleteResponse from a JSON string
project_delete_response_instance = ProjectDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(ProjectDeleteResponse.to_json())

# convert the object into a dict
project_delete_response_dict = project_delete_response_instance.to_dict()
# create an instance of ProjectDeleteResponse from a dict
project_delete_response_from_dict = ProjectDeleteResponse.from_dict(project_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


