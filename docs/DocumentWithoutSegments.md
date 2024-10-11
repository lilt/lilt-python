# DocumentWithoutSegments

A Document is a collection of zero or more Segments. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique number identifying the Document. | [optional] 
**project_id** | **int** | A unique number identifying the Project. | [optional] 
**srclang** | **str** | An ISO 639-1 language identifier. | [optional] 
**trglang** | **str** | An ISO 639-1 language identifier. | [optional] 
**name** | **str** | The document name. | [optional] 
**import_in_progress** | **bool** | True if the document is currently being imported | [optional] 
**import_succeeded** | **bool** | True if the import process succeeded. | [optional] 
**import_error_message** | **str** | Error message if &#x60;import_succeeded&#x3D;false&#x60; | [optional] 
**export_in_progress** | **bool** | True if the document is currently being exported for download | [optional] 
**export_succeeded** | **bool** | True if the export process succeeded. | [optional] 
**export_error_message** | **str** | Error message if &#x60;export_succeeded&#x3D;false&#x60; | [optional] 
**is_pretranslating** | **bool** | True if the document is currently being pretranslated. | [optional] 
**status** | [**DocumentWithoutSegmentsStatus**](DocumentWithoutSegmentsStatus.md) |  | [optional] 
**translator_email** | **str** | The email of the assigned translator. | [optional] 
**reviewer_email** | **str** | The email of the assigned reviewer. | [optional] 
**customer_reviewer_email** | **str** | The email of the assigned customer reviewer. Only present if the project was request by id. | [optional] 
**created_at** | **int** | Time at which the object was created. Measured in seconds since the Unix epoch. | [optional] 
**updated_at** | **int** | Time at which the object was created. Measured in seconds since the Unix epoch. | [optional] 
**is_review_complete** | **bool** | Document review status. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


