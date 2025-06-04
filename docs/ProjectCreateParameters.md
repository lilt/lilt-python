# ProjectCreateParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A name for the Project. | 
**memory_id** | **int** | The Memory to associate with this new Project. | 
**job_id** | **int** | The Job to associate with this new Project. If a Job ID is not provided then a new Job will be created to contain the Project.  | [optional] 
**due_date** | **int** | The due date. Measured in seconds since the Unix epoch. | [optional] 
**metadata** | **object** | A JSON object of key/value string pairs. Stores custom project information. | [optional] 
**workflow_template_id** | **int** | The workflow template used to create this project. WorkflowTemplateIds can be retrieved via the /workflows/templates endpoint. If not specified then the organization default workflowTemplateId will be used. | [optional] 
**workflow_template_name** | **str** | Name of the workflow for the project, if a workflowTemplateId is passed, this field will be ignored. | [optional] 
**llm_provider** | **str** | The LLM provider to use for the project. Defaults to \&quot;neural\&quot;. | [optional] 
**external_model_id** | **int** | External model ID, if any. Must match the chosen llm_provider. | [optional] 
**is_plural** | **bool** | Whether the documents in this project contain ICU plural forms. | [optional] 
**require_batch_qa_translator** | **bool** | Whether to require batch QA from the translator side. | [optional] 
**enable_prompt_labeling** | **bool** | Whether to enable prompt labeling for the project. | [optional] 
**job_type** | **str** | (Optional) A specialized job type for advanced features. | [optional] 
**additional_guidelines** | **str** | (Optional) Additional instructions or guidelines. | [optional] 
**is_enhanced_human_ai_optimized** | **bool** | Whether the project is enhanced with AI optimization. | [optional] 
**domain_id** | **int** | A domain ID to categorize this project under. | [optional] 

## Example

```python
from lilt.models.project_create_parameters import ProjectCreateParameters

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectCreateParameters from a JSON string
project_create_parameters_instance = ProjectCreateParameters.from_json(json)
# print the JSON string representation of the object
print(ProjectCreateParameters.to_json())

# convert the object into a dict
project_create_parameters_dict = project_create_parameters_instance.to_dict()
# create an instance of ProjectCreateParameters from a dict
project_create_parameters_from_dict = ProjectCreateParameters.from_dict(project_create_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


