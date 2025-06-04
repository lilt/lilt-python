# CreateConverterConfigParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signed_agreement** | **bool** | Signifies that the Organization has signed the agreement or not. | 

## Example

```python
from lilt.models.create_converter_config_parameters import CreateConverterConfigParameters

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConverterConfigParameters from a JSON string
create_converter_config_parameters_instance = CreateConverterConfigParameters.from_json(json)
# print the JSON string representation of the object
print(CreateConverterConfigParameters.to_json())

# convert the object into a dict
create_converter_config_parameters_dict = create_converter_config_parameters_instance.to_dict()
# create an instance of CreateConverterConfigParameters from a dict
create_converter_config_parameters_from_dict = CreateConverterConfigParameters.from_dict(create_converter_config_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


