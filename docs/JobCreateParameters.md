# JobCreateParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A name for the Job. | 
**language_pairs** | [**List[LanguagePair]**](LanguagePair.md) | Language pairs is a set of one or more pairs that includes source language, source locale(optional), target language, target locale(optional), and memoryId. | 
**file_ids** | **List[int]** | A list of file ids to upload to job creation. | 
**due** | **str** | An ISO string date representing job due date. | [optional] 
**src_lang** | **str** | 2-letter ISO source language code | 
**src_locale** | **str** | 2-letter source language code | [optional] 
**is_plural** | **bool** | A boolean value representing if the files have plurals. | [optional] 
**workflow_template_id** | **int** | ID of the workflow template to be used. Use the [workflows templates endpoint](#tag/Workflows/operation/getWorkflowTemplates) to get the list of available workflows. | [optional] 
**domain_id** | **int** | ID of the domain to be used. Use the [domains endpoint](#tag/Domains/operation/getDomains) to get the list of available domains. | [optional] 

## Example

```python
from lilt.models.job_create_parameters import JobCreateParameters

# TODO update the JSON string below
json = "{}"
# create an instance of JobCreateParameters from a JSON string
job_create_parameters_instance = JobCreateParameters.from_json(json)
# print the JSON string representation of the object
print(JobCreateParameters.to_json())

# convert the object into a dict
job_create_parameters_dict = job_create_parameters_instance.to_dict()
# create an instance of JobCreateParameters from a dict
job_create_parameters_from_dict = JobCreateParameters.from_dict(job_create_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


