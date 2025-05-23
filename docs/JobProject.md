# JobProject

A job project contains project statistical data that belongs to a specific job. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | An id for the project. | [optional] 
**src_lang** | **str** | Source language, an ISO 639-1 language identifier. | [optional] 
**src_locale** | **str** | A locale identifier, supported for source language. | [optional] 
**trg_lang** | **str** | Target language, an ISO 639-1 language identifier. | [optional] 
**trg_locale** | **str** | A locale identifier, supported for target language. | [optional] 
**name** | **str** | A name for the project. | [optional] 
**due** | **str** | An ISO date. | [optional] 
**is_complete** | **bool** | A state that checks project was completed. | [optional] 
**is_archived** | **bool** | The archived state of the project. | [optional] 
**state** | **str** | Current state of the project. Example, backlog, inProgress, inReview, done. | [optional] 
**num_source_tokens** | **int** | Total number of source tokens. | [optional] 
**created_at** | **str** | Time at which the object was created. | [optional] 
**updated_at** | **str** | Time at which the object was updated. | [optional] 
**is_deleted** | **bool** | A state that checks project was deleted. | [optional] 
**memory_id** | **int** | A unique number identifying the associated Memory. | [optional] 
**workflow_status** | **str** | The status of the Workflow for the current project. | [optional] 
**workflow_name** | **str** | Human readable name of the workflow associated with the current project. | [optional] 

## Example

```python
from lilt.models.job_project import JobProject

# TODO update the JSON string below
json = "{}"
# create an instance of JobProject from a JSON string
job_project_instance = JobProject.from_json(json)
# print the JSON string representation of the object
print(JobProject.to_json())

# convert the object into a dict
job_project_dict = job_project_instance.to_dict()
# create an instance of JobProject from a dict
job_project_from_dict = JobProject.from_dict(job_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


