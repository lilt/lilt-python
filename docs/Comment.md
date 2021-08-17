# Comment

A Comment is a translator's or a reviewer's comment on a segment. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique number identifying the Comment. | [optional] 
**text** | **str** | The comment text. | [optional] 
**annotations** | [**list[Annotation]**](Annotation.md) | A list of optional Annotations. | [optional] 
**is_resolved** | **bool** | Whether the Comment is resolved. | [optional] 
**document_id** | **int** | The document to which the comment belongs. | [optional] 
**segment_id** | **int** | The individual segment to which the comment applies. | [optional] 
**segment_revision_id** | **int** | The revision of the individual segment to which the comment applies. | [optional] 
**user_id** | **int** | The user who created this comment. | [optional] 
**created_at** | **int** | Time at which the object was created. Measured in seconds since the Unix epoch. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


