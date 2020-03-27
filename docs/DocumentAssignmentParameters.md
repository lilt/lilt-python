# DocumentAssignmentParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique Document identifier. | 
**email** | **str** | An email address. | 
**is_translator** | **bool** | If true, assign for translating. If false, then unassign. | [optional] 
**is_reviewer** | **bool** | If true, assign for reviewing. If false, then unassign. | [optional] 
**due_date** | **datetime** | Due date for translation or review (set based on &#x60;is_translator&#x60; and &#x60;is_reviewer&#x60; flags). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


