# DomainList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Domain]**](Domain.md) | The list of domains in the response. | 
**size** | **int** | The total number of domains in the list. | 

## Example

```python
from lilt.models.domain_list import DomainList

# TODO update the JSON string below
json = "{}"
# create an instance of DomainList from a JSON string
domain_list_instance = DomainList.from_json(json)
# print the JSON string representation of the object
print(DomainList.to_json())

# convert the object into a dict
domain_list_dict = domain_list_instance.to_dict()
# create an instance of DomainList from a dict
domain_list_from_dict = DomainList.from_dict(domain_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


