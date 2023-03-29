# AutoAssignmentResponse

Auto assignment status.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **float** | The id of the project. | 
**success** | **bool** | True if the operation was successful for this project. | 
**error** | **str** | An optional error message if success &#x3D; false | [optional] 
**errors** | [**list[AssignmentError]**](AssignmentError.md) | A list of errors if there were any. | [optional] 
**assignments** | [**list[AssignmentDetails]**](AssignmentDetails.md) | Assignment details, like which user was assigned and which role. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


