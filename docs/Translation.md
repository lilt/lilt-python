# Translation

A machine translation (MT) or a translation memory (TM) match of a source segment.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | The target string. | [optional] 
**target_with_tags** | **str** | The target string with source tags projected into the target. | [optional] 
**align** | **str** | \&quot;MT only: A whitespace delimited list of source-target alignment indices.\&quot;  | [optional] 
**provenance** | **str** | Positive values indicate that the word is from the Memory, with contiguous identical entries (e.g., 2 2) indicating phrase matches. Negative contiguous values indicate entries from the Lexicon. 0 indicates a word from the background data.  | [optional] 
**score** | **float** | The score of the translation. | [optional] 
**is_tm_match** | **bool** | TM only: If true, indicates an exact translation memory match. | [optional] 
**target_delimiters** | **list[str]** | A format string that indicates, for each word, if the word should be preceded by a space. | [optional] 
**target_words** | **list[str]** | The target string can be constructed by suffixing each &#x60;targetDelimiters&#x60; entry with its corresponding word in &#x60;targetWords&#x60; and concatenating the constructed array. Please note that the &#x60;targetDelimiters&#x60; array has one more entry than &#x60;targetWords&#x60; array which is why the last entry in the array will be the last value of &#x60;targetDelimiters&#x60;.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


