# TermbaseExportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique Memory identifier. | [optional] 
**is_processing** | **int** | The current state of the import. | [optional] 

## Example

```python
from lilt.models.termbase_export_response import TermbaseExportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TermbaseExportResponse from a JSON string
termbase_export_response_instance = TermbaseExportResponse.from_json(json)
# print the JSON string representation of the object
print(TermbaseExportResponse.to_json())

# convert the object into a dict
termbase_export_response_dict = termbase_export_response_instance.to_dict()
# create an instance of TermbaseExportResponse from a dict
termbase_export_response_from_dict = TermbaseExportResponse.from_dict(termbase_export_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


