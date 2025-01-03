# JobCreateParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A name for the Job. | 
**language_pairs** | [**list[LanguagePair]**](LanguagePair.md) | Language pairs is a set of one or more pairs that includes source language, source locale(optional), target language, target locale(optional), and memoryId. | 
**file_ids** | **list[int]** | A list of file ids to upload to job creation. | 
**due** | **str** | An ISO string date representing job due date. | [optional] 
**src_lang** | **str** | 2-letter ISO source language code | 
**src_locale** | **str** | 2-letter source language code | 
**is_plural** | **bool** | A boolean value representing if the files have plurals. | [optional] 
**workflow_template_id** | **int** | ID of the workflow template to be used. Use the [workflows templates endpoint](#tag/Workflows/operation/getWorkflowTemplates) to get the list of available workflows. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


