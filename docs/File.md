# File

A File is an unprocessed source file that can later be added to a project.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique number identifying the File. | [optional] 
**name** | **str** | The file name. | [optional] 
**file_hash** | **str** | A unique hash value associated with the file. An MD5 hash of the file content will be used by default. | [optional] 
**export_uri** | **str** | A webhook endpoint that will export the translated document back to the source repository. | [optional] 
**created_at** | **int** | Time at which the object was created. Measured in seconds since the Unix epoch. | [optional] 
**updated_at** | **int** | Time at which the object was created. Measured in seconds since the Unix epoch. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


