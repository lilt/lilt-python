# ProjectStatus

The status of a Project. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique Project identifier. | [optional] 
**num_source_words** | **int** | The number of source words in the Project. | [optional] 
**num_words_confirmed** | **int** | The number of confirmed source words. | [optional] 
**num_words_reviewed** | **int** | The number of reviewed source words. | [optional] 
**time_elapsed** | **int** | The total time spent on the project by all resources. Measured in milliseconds. | [optional] 
**time_elapsed_translation** | **int** | The total time spent on translation by all resources. Measured in milliseconds. | [optional] 
**time_elapsed_research** | **int** | The total time spent on research by all resources. Measured in milliseconds. | [optional] 
**time_elapsed_review** | **int** | The total time spent on reviewing by all resources. Measured in milliseconds. | [optional] 
**updated_at** | **int** | The project update date and time. Measured in seconds. | [optional] 
**resources** | [**list[ResourceStatus]**](ResourceStatus.md) | A list of ResourceStatus objects that represent per-resource statistics. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


