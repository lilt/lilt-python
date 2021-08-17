# JobProject

A job project contains project statistcal data that belongs to a specific job. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | An id for the project. | [optional] 
**src_lang** | **str** | Source langauge, an ISO 639-1 language identifier. | [optional] 
**src_locale** | **str** | A locale identifier, supported for source langauge. | [optional] 
**trg_lang** | **str** | Target langauge, an ISO 639-1 language identifier. | [optional] 
**trg_locale** | **str** | A locale identifier, supported for target langauge. | [optional] 
**name** | **str** | A name for the project. | [optional] 
**due** | **str** | An ISO date. | [optional] 
**is_complete** | **bool** | A state that checks project was completed. | [optional] 
**is_archived** | **bool** | The archived state of the project. | [optional] 
**state** | **str** | Current state of the project. Example, backlog, inProgress, inReview, done. | [optional] 
**num_source_tokens** | **int** | Total number of source tokens. | [optional] 
**created_at** | **str** | Time at which the object was created. | [optional] 
**updated_at** | **str** | Time at which the object was updated. | [optional] 
**is_deleted** | **bool** | A state that checks project was deleted. | [optional] 
**memory_id** | **int** | A unique number identifying the associated Memory. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


