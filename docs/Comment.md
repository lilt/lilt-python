# Comment

A Comment is a translator's or a reviewer's comment on a segment. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique number identifying the Comment. | [optional] 
**text** | **str** | The comment text. | [optional] 
**user_id** | **int** | The User who created this Comment. | [optional] 
**is_resolved** | **bool** | Whether the Comment is resolved. | [optional] 
**annotations** | [**list[Annotation]**](Annotation.md) | A list of optional Annotations. | [optional] 
**created_at** | **int** | Time at which the object was created. Measured in seconds since the Unix epoch. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


