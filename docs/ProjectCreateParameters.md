# ProjectCreateParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A name for the Project. | 
**memory_id** | **int** | The Memory to associate with this new Project. | 
**job_id** | **int** | The Job to associate with this new Project. If a Job ID is not provided then a new Job will be created to contain the Project.  | [optional] 
**due_date** | **int** | The due date. Measured in seconds since the Unix epoch. | [optional] 
**metadata** | [**object**](.md) | A JSON object of key/value string pairs. Stores custom project information. | [optional] 
**workflow_template_id** | **int** | The workflow template used to create this project. WorkflowTemplateIds can be retrieved via the /workflows/templates endpoint. If not specified then the organization default workflowTemplateId will be used. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


