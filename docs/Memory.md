# Memory

A Memory is a collection of parallel (source/target) segments from which a MT/TM model is trained. When a translator confirms a segment in the Interface, a parallel segment is added to the Memory. Parallel segments from existing translation memories and bitexts can also be added to the Memory via the REST API. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique number identifying the Memory. | [optional] 
**srclang** | **str** | An ISO 639-1 language identifier. | [optional] 
**trglang** | **str** | An ISO 639-1 language identifier. | [optional] 
**srclocale** | **str** | An ISO 639-1 language identifier. | [optional] 
**trglocale** | **str** | An ISO 639-1 language identifier. | [optional] 
**name** | **str** | A name for the Memory. | [optional] 
**version** | **int** | The current version of the Memory, which is the number of updates since the memory was created. | [optional] 
**created_at** | **int** | Time at which the object was created. Measured in seconds since the Unix epoch. | [optional] 
**updated_at** | **int** | Time at which the object was created. Measured in seconds since the Unix epoch. | [optional] 
**resources** | **list[str]** | The resource files (translation memories and termbases) associated with this Memory. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


