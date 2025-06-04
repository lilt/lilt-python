# Project

A Project is a collection of zero or more Documents. It is specific to a language pair, and is associated with exactly one Memory for that language pair. The Memory association cannot be changed after the Project is created. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique number identifying the Project. | [optional] 
**memory_id** | **int** | A unique number identifying the associated Memory. | [optional] 
**job_id** | **int** | A unique number identifying the associated Job. | [optional] 
**srclang** | **str** | An ISO 639-1 language identifier. | [optional] 
**trglang** | **str** | An ISO 639-1 language identifier. | [optional] 
**srclocale** | **str** | A locale identifier, supported for srclang. | [optional] 
**trglocale** | **str** | A locale identifier, supported for trglang. | [optional] 
**name** | **str** | A name for the project. | [optional] 
**state** | **str** | The project&#39;s state. The possible states are &#x60;backlog&#x60;, &#x60;inProgress&#x60;, &#x60;inReview&#x60;, &#x60;inQA&#x60;, and &#x60;done&#x60;. | [optional] 
**due_date** | **int** | The due date. Measured in seconds since the Unix epoch. | [optional] 
**archived** | **bool** | The archived state of the Project. | [optional] 
**metadata** | **object** | A JSON object of key/value string pairs. Stores custom project information. | [optional] 
**sample_review_percentage** | **int** | The project&#39;s sample review percentage. | [optional] 
**created_at** | **int** | Time at which the object was created. Measured in seconds since the Unix epoch. | [optional] 
**updated_at** | **int** | Time at which the object was created. Measured in seconds since the Unix epoch. | [optional] 
**workflow_status** | **str** | The status of the Workflow for the current project. This may not be present for all project endpoints even with workflows enabled. | [optional] 
**document** | [**List[DocumentWithoutSegments]**](DocumentWithoutSegments.md) | A list of Documents. | [optional] 

## Example

```python
from lilt.models.project import Project

# TODO update the JSON string below
json = "{}"
# create an instance of Project from a JSON string
project_instance = Project.from_json(json)
# print the JSON string representation of the object
print(Project.to_json())

# convert the object into a dict
project_dict = project_instance.to_dict()
# create an instance of Project from a dict
project_from_dict = Project.from_dict(project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


