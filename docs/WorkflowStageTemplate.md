# WorkflowStageTemplate

A single stage within a Workflow Template.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The human readable name of a Workflow stage. | [optional] 
**assignment_type** | **str** | An enum to represent all possible types of Workflow stage. | [optional] 

## Example

```python
from lilt.models.workflow_stage_template import WorkflowStageTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowStageTemplate from a JSON string
workflow_stage_template_instance = WorkflowStageTemplate.from_json(json)
# print the JSON string representation of the object
print(WorkflowStageTemplate.to_json())

# convert the object into a dict
workflow_stage_template_dict = workflow_stage_template_instance.to_dict()
# create an instance of WorkflowStageTemplate from a dict
workflow_stage_template_from_dict = WorkflowStageTemplate.from_dict(workflow_stage_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


