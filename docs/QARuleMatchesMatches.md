# QARuleMatchesMatches

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**QARuleMatchesContext**](QARuleMatchesContext.md) |  | 
**length** | **int** | The length of the error in characters. | 
**message** | **str** | Message about the error displayed to the user. | 
**offset** | **int** | The 0-based character offset of the error in the text. | 
**replacements** | [**list[QARuleMatchesReplacements]**](QARuleMatchesReplacements.md) | Replacements that might correct the error. The array can be empty, in this case there is no suggested replacement. | 
**rule** | [**QARuleMatchesRule**](QARuleMatchesRule.md) |  | [optional] 
**short_message** | **str** | An optional shorter version of &#39;message&#39;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


