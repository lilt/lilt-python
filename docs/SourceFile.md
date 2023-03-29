# SourceFile

A SourceFile is an unprocessed source file that can later be added to a project.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique number identifying the SourceFile. | [optional] 
**name** | **str** | The file name. | [optional] 
**file_hash** | **str** | A unique hash value associated with the file. An MD5 hash of the file content will be used by default. | [optional] 
**detected_lang** | **str** | Language associated with the file. | [optional] 
**detected_lang_confidence** | **float** | Confidence score for the language associated with the file. | [optional] 
**category** | **str** | The category of the file. The options are &#x60;REFERENCE&#x60;, or &#x60;API&#x60;. The default is API. Files with the &#x60;REFERENCE&#x60; category will be displayed as reference material. | [optional] 
**labels** | **list[str]** | The list of labels associated with the file. | [optional] 
**created_at** | **datetime** | Time at which the object was created. | [optional] 
**updated_at** | **datetime** | Time at which the object was created. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


