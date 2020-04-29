# ProjectQuote

Quoting information for a Project. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique Project identifier. | [optional] 
**num_source_words** | **int** | The number of source words in the Project. | [optional] 
**num_words_new** | **int** | The number of new source words in the Project. | [optional] 
**num_segments_new** | **int** | The number of new segments in the Project. | [optional] 
**num_words_repetition** | **int** | The number of repetition source words in the Project. | [optional] 
**num_segments_repetition** | **int** | The number of repetition segments in the Project. | [optional] 
**bands** | [**list[MatchBand]**](MatchBand.md) | A list of MatchBand objects that represent translation memory leverage statistics. | [optional] 
**documents** | [**list[DocumentQuote]**](DocumentQuote.md) | A list of DocumentQuote objects that quotes information for a Document. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


