# Project

A Project is a collection of zero or more Documents. It is specific to a language pair, and is associated with exactly one Memory for that language pair. The Memory association cannot be changed after the Project is created. 
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
**state** | **str** | The project&#39;s state. The possible states are &#39;backlog&#39;, &#39;inProgress&#39;, &#39;inReview&#39;, &#39;inQA&#39;, and &#39;done&#39; | [optional] 
**due_date** | **int** | The due date. Measured in seconds since the Unix epoch. | [optional] 
**archived** | **bool** | The archived state of the Project. | [optional] 
**metadata** | [**object**](.md) | A JSON object for storing various project metadata. | [optional] 
**created_at** | **int** | Time at which the object was created. Measured in seconds since the Unix epoch. | [optional] 
**updated_at** | **int** | Time at which the object was created. Measured in seconds since the Unix epoch. | [optional] 
**document** | [**list[DocumentWithoutSegments]**](DocumentWithoutSegments.md) | A list of Documents. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


