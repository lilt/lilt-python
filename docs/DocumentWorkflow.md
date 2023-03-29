# DocumentWorkflow

Workflow metadata related to a document.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **int** | Identifier of a document. | [optional] 
**workflow_id** | **int** | Identifier for a Workflow that the document is using. | [optional] 
**stages** | [**list[WorkflowStage]**](WorkflowStage.md) | The stages in the document&#39;s workflow. | [optional] 
**current_task** | [**WorkflowTask**](WorkflowTask.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


