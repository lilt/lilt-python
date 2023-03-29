# WorkflowTemplate

A workflow template which defines the workflow's possible steps (combination of Translation, Review and Customer Review).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | Identifier of a teams Workflow template. Can be used during Job creation for specifying the workflow used for a job or language pair. | [optional] 
**name** | **str** |  | [optional] 
**team_id** | **float** | The name of a given Workflow template. | [optional] 
**stages** | [**list[WorkflowStageTemplate]**](WorkflowStageTemplate.md) | The stages in this workflow template. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


