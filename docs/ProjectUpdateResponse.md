# ProjectUpdateResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique Project identifier. | 
**name** | **str** | The Project name. | [optional] 
**state** | **str** | The project&#39;s state. The possible states are &#39;backlog&#39;, &#39;inProgress&#39;, &#39;inReview&#39;, &#39;inQA&#39;, and &#39;done&#39; | [optional] 
**due_date** | **int** | The due date. Measured in seconds since the Unix epoch. | [optional] 
**archived** | **bool** | True if the project is archived. Otherwise, false. | [optional] 
**metadata** | [**object**](.md) | Metadata associated with a project. This field must be valid JSON. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


