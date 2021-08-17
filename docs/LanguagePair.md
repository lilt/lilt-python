# LanguagePair

A language pair couples the source and target language along with memory and pre-translations settings associated to a project. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**src_lang** | **str** | Source langauge, an ISO 639-1 language identifier. | [optional] 
**src_locale** | **str** | A locale identifier, supported for source langauge. | [optional] 
**trg_lang** | **str** | Target langauge, an ISO 639-1 language identifier. | 
**trg_locale** | **str** | A locale identifier, supported for target language. | [optional] 
**due_date** | **str** | An ISO date. | [optional] 
**memory_id** | **int** | A unique number identifying the associated Memory. | 
**pretranslate** | **bool** | Attribute translation authorship of exact matches to the creator of the document being pretranslated. | [optional] 
**auto_accept** | **bool** | Accept and lock exact matches. | [optional] 
**case_sensitive** | **bool** | Use case sensitive translation memory matching. | [optional] 
**take_match_attribution** | **bool** | Use MT for unmatched segments. | [optional] 
**config_id** | **int** | Configuration id | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


