# Segment

A Segment is a source string and, optionally, its translation. A Segment can be associated with both a Memory and a Document. The Segment object contains additional metadata about the source and target strings. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique number identifying the Segment. | [optional] 
**created_at** | **int** | Time at which the object was created. Measured in seconds since the Unix epoch. | [optional] 
**updated_at** | **int** | Time at which the object was created. Measured in seconds since the Unix epoch. | [optional] 
**document_id** | **int** | A unique Document identifier. | [optional] 
**memory_id** | **int** | The Memory with which this Segment is associated. | [optional] 
**source** | **str** | The source string. | [optional] 
**srclang** | **str** | An ISO 639-1 language code. | [optional] 
**target** | **str** | The target string. | [optional] 
**trglang** | **str** | An ISO 639-1 language code. | [optional] 
**is_confirmed** | **bool** | The confirmation status. | [optional] 
**is_reviewed** | **bool** | The review status. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


