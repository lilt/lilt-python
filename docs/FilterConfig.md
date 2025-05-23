# FilterConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the filter configuration. | [optional] 
**is_default** | **bool** | Indicates if the filter configuration is the default. | [optional] 
**filter_config** | **str** | The filter configuration. | [optional] 
**filter_name** | **str** | The name of the filter. | [optional] 
**config_name** | **str** | The name of the configuration. | [optional] 
**config_description** | **str** | The description of the configuration. | [optional] 
**subfilters** | **str** | The subfilters. | [optional] 
**segmentation_config_setting** | **str** | The segmentation configuration setting. | [optional] 
**srx** | **str** | The SRX (Segmentation Rules eXchange) data. | [optional] 
**segmentation_config_name** | **str** | The name of the segmentation configuration. | [optional] 
**domains** | [**List[DomainReference]**](DomainReference.md) | The domains associated with the filter configuration. | [optional] 
**created_at** | **datetime** | The creation timestamp. | [optional] 
**updated_at** | **datetime** | The last update timestamp. | [optional] 
**default** | **bool** | Indicates if the filter configuration is the default. | [optional] 

## Example

```python
from lilt.models.filter_config import FilterConfig

# TODO update the JSON string below
json = "{}"
# create an instance of FilterConfig from a JSON string
filter_config_instance = FilterConfig.from_json(json)
# print the JSON string representation of the object
print(FilterConfig.to_json())

# convert the object into a dict
filter_config_dict = filter_config_instance.to_dict()
# create an instance of FilterConfig from a dict
filter_config_from_dict = FilterConfig.from_dict(filter_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


