# JobCreateParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A name for the Job. | 
**language_pairs** | [**list[LanguagePair]**](LanguagePair.md) | Language pairs is a set of one or more pairs that includes source language, source locale(optional), target language, target locale(optional), and memoryId. | 
**file_ids** | **list[int]** | A list of file ids to upload to job creation. | 
**due** | **str** | An ISO string date representing job due date. | [optional] 
**workflow_template_id** | **int** | Identifier of the workflow template to be used when creating a job. If not passed the organization default will be used. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


