# DomainMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the metadata. | [optional] 
**key** | **str** | The key of the metadata. | [optional] 
**value** | **str** | The value of the metadata. | [optional] 

## Example

```python
from lilt.models.domain_metadata import DomainMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of DomainMetadata from a JSON string
domain_metadata_instance = DomainMetadata.from_json(json)
# print the JSON string representation of the object
print(DomainMetadata.to_json())

# convert the object into a dict
domain_metadata_dict = domain_metadata_instance.to_dict()
# create an instance of DomainMetadata from a dict
domain_metadata_from_dict = DomainMetadata.from_dict(domain_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


