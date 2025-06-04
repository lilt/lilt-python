# JobDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique Project identifier. | [optional] 

## Example

```python
from lilt.models.job_delete_response import JobDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JobDeleteResponse from a JSON string
job_delete_response_instance = JobDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(JobDeleteResponse.to_json())

# convert the object into a dict
job_delete_response_dict = job_delete_response_instance.to_dict()
# create an instance of JobDeleteResponse from a dict
job_delete_response_from_dict = JobDeleteResponse.from_dict(job_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


