# LanguagePair

A language pair couples the source and target language along with memory and pre-translations settings associated to a project. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trg_lang** | **str** | Target language, an ISO 639-1 language identifier. | 
**trg_locale** | **str** | A locale identifier, supported for target language. | [optional] 
**due_date** | **str** | An ISO date. | [optional] 
**memory_id** | **int** | A unique number identifying the associated Memory. | 
**external_model_id** | **int** | An optional parameter to specify a third-party model ID to use for translation. This allows you to use external MT providers instead of Lilt&#39;s built-in MT system. | [optional] 
**pretranslate** | **bool** | Attribute translation authorship of exact matches to the creator of the document being pretranslated. | [optional] 
**auto_accept** | **bool** | Accept and lock exact matches. | [optional] 
**case_sensitive** | **bool** | Use case sensitive translation memory matching. | [optional] 
**take_match_attribution** | **bool** | Use MT for unmatched segments. | [optional] 
**config_id** | **int** | Configuration id | [optional] 
**workflow_template_id** | **int** | Workflow Template id, to assign a specific Workflow to the project created out of this Language Pair. WorkflowTemplateIds can be retrieved via the /workflows/templates endpoint. If not specified then the Job level workflowTemplateId will be used. | [optional] 
**workflow_template_name** | **int** | Workflow Template Name, when passed with TeamId it allows for an on the fly look up of the correct WorkflowTemplate to use. If workflowTemplateId is passed the workflowTemplateId supercedes other lookups. | [optional] 
**workflow_stage_assignments** | [**List[WorkflowStageAssignment]**](WorkflowStageAssignment.md) |  | [optional] 

## Example

```python
from lilt.models.language_pair import LanguagePair

# TODO update the JSON string below
json = "{}"
# create an instance of LanguagePair from a JSON string
language_pair_instance = LanguagePair.from_json(json)
# print the JSON string representation of the object
print(LanguagePair.to_json())

# convert the object into a dict
language_pair_dict = language_pair_instance.to_dict()
# create an instance of LanguagePair from a dict
language_pair_from_dict = LanguagePair.from_dict(language_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


