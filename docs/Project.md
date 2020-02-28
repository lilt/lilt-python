# Project

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique number identifying the Project. | [optional] 
**memory_id** | **int** | A unique number identifying the associated Memory. | [optional] 
**srclang** | **str** | An ISO 639-1 language identifier. | [optional] 
**trglang** | **str** | An ISO 639-1 language identifier. | [optional] 
**srclocale** | **str** | A locale identifier, supported for srclang. | [optional] 
**trglocale** | **str** | A locale identifier, supported for trglang. | [optional] 
**name** | **str** | A name for the project. | [optional] 
**state** | **str** | The project&#x27;s state. The possible states are &#x27;backlog&#x27;, &#x27;inProgress&#x27;, &#x27;inReview&#x27;, &#x27;inQA&#x27;, and &#x27;done&#x27; | [optional] 
**due_date** | **int** | The due date. Measured in seconds since the Unix epoch. | [optional] 
**archived** | **bool** | The archived state of the Project. | [optional] 
**metadata** | **object** | A JSON object for storing various project metadata. | [optional] 
**created_at** | **int** | Time at which the object was created. Measured in seconds since the Unix epoch. | [optional] 
**updated_at** | **int** | Time at which the object was created. Measured in seconds since the Unix epoch. | [optional] 
**document** | [**list[DocumentWithoutSegments]**](DocumentWithoutSegments.md) | A list of Documents. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

