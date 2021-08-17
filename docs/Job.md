# Job

A Job is a collection of multiple Projects. Each project is specific to a language pair, and is associated with exactly one Memory for that language pair. The Memory association cannot be changed after the Project is created. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A name for the job. | [optional] 
**creation_status** | **str** | Status of job creation process that includes PENDING, COMPLETE, and FAILED. | [optional] 
**delivered_at** | **datetime** |  | [optional] 
**status** | **str** | Current status of job that includes archived, delivered, and active. | [optional] 
**due** | **str** | An ISO string date. | [optional] 
**id** | **int** | An id for the job. | [optional] 
**is_processing** | **int** | Values include &#x60;1&#x60; while in progress, &#x60;0&#x60; when idle and &#x60;-2&#x60; when processing failed. | [optional] 
**stats** | [**JobStats**](JobStats.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


