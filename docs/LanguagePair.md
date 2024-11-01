# LanguagePair

A language pair couples the source and target language along with memory and pre-translations settings associated to a project. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trg_lang** | **str** | Target language, an ISO 639-1 language identifier. | 
**trg_locale** | **str** | A locale identifier, supported for target language. | [optional] 
**due_date** | **str** | An ISO date. | [optional] 
**memory_id** | **int** | A unique number identifying the associated Memory. | 
**external_model_id** | **int** | A unique identifier for working with a third party model in the Lilt Platform | [optional] 
**pretranslate** | **bool** | Attribute translation authorship of exact matches to the creator of the document being pretranslated. | [optional] 
**auto_accept** | **bool** | Accept and lock exact matches. | [optional] 
**case_sensitive** | **bool** | Use case sensitive translation memory matching. | [optional] 
**take_match_attribution** | **bool** | Use MT for unmatched segments. | [optional] 
**config_id** | **int** | Configuration id | [optional] 
**workflow_template_id** | **int** | Workflow Template id, to assign a specific Workflow to the project created out of this Language Pair. WorkflowTemplateIds can be retrieved via the /workflows/templates endpoint. If not specified then the Job level workflowTemplateId will be used. | [optional] 
**workflow_template_name** | **int** | Workflow Template Name, when passed with TeamId it allows for an on the fly look up of the correct WorkflowTemplate to use. If workflowTemplateId is passed the workflowTemplateId supercedes other lookups. | [optional] 
**workflow_stage_assignments** | [**list[WorkflowStageAssignment]**](WorkflowStageAssignment.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


