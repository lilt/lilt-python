# WorkflowTemplate

A workflow template which defines the workflow's possible steps (combination of Translation, Review and Customer Review).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | Identifier of a teams Workflow template. Can be used during Job creation for specifying the workflow used for a job or language pair. | [optional] 
**name** | **str** |  | [optional] 
**team_id** | **float** | The name of a given Workflow template. | [optional] 
**stages** | [**List[WorkflowStageTemplate]**](WorkflowStageTemplate.md) | The stages in this workflow template. | [optional] 

## Example

```python
from lilt.models.workflow_template import WorkflowTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowTemplate from a JSON string
workflow_template_instance = WorkflowTemplate.from_json(json)
# print the JSON string representation of the object
print(WorkflowTemplate.to_json())

# convert the object into a dict
workflow_template_dict = workflow_template_instance.to_dict()
# create an instance of WorkflowTemplate from a dict
workflow_template_from_dict = WorkflowTemplate.from_dict(workflow_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


