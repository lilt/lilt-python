# JobUpdateParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A name for the Job. | [optional] 
**due_date** | **int** | An ISO string date. | [optional] 
**is_processing** | **str** | The processing status of the job. Provide one of the following integers to indicate the status.  Ok &#x3D; 0 Started &#x3D; 1 ExportError &#x3D; -2  | [optional] 
**processing_error_msg** | **str** | The processing error message. | [optional] 

## Example

```python
from lilt.models.job_update_parameters import JobUpdateParameters

# TODO update the JSON string below
json = "{}"
# create an instance of JobUpdateParameters from a JSON string
job_update_parameters_instance = JobUpdateParameters.from_json(json)
# print the JSON string representation of the object
print(JobUpdateParameters.to_json())

# convert the object into a dict
job_update_parameters_dict = job_update_parameters_instance.to_dict()
# create an instance of JobUpdateParameters from a dict
job_update_parameters_from_dict = JobUpdateParameters.from_dict(job_update_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


