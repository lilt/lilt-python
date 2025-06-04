# Domain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_id** | **int** | The unique identifier for the domain. | 
**domain_name** | **str** | The name of the domain. | 
**models** | [**List[Model]**](Model.md) | The models associated with the domain. | 
**filter_configs** | [**List[FilterConfig]**](FilterConfig.md) | The filter configurations associated with the domain. | 
**domain_metadata** | [**List[DomainMetadata]**](DomainMetadata.md) | Metadata associated with the domain. | 

## Example

```python
from lilt.models.domain import Domain

# TODO update the JSON string below
json = "{}"
# create an instance of Domain from a JSON string
domain_instance = Domain.from_json(json)
# print the JSON string representation of the object
print(Domain.to_json())

# convert the object into a dict
domain_dict = domain_instance.to_dict()
# create an instance of Domain from a dict
domain_from_dict = Domain.from_dict(domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


