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
**sample_review_percentage** | **int** | The Project&#39;s sample review percentage. Must be an integer between 10 and 100, a multiple of 10 and greater than minimum value (displayed in error message). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


