# WorkflowStageAssignment

An assignment object that associates a user to a workflow stage template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_stage_template_id** | **int** |  | 
**user_id** | **int** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from lilt.models.workflow_stage_assignment import WorkflowStageAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowStageAssignment from a JSON string
workflow_stage_assignment_instance = WorkflowStageAssignment.from_json(json)
# print the JSON string representation of the object
print(WorkflowStageAssignment.to_json())

# convert the object into a dict
workflow_stage_assignment_dict = workflow_stage_assignment_instance.to_dict()
# create an instance of WorkflowStageAssignment from a dict
workflow_stage_assignment_from_dict = WorkflowStageAssignment.from_dict(workflow_stage_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


