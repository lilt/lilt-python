# WebhooksUpdateRequestAnyOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_name** | **str** | The name of the webhook configuration. | 

## Example

```python
from lilt.models.webhooks_update_request_any_of import WebhooksUpdateRequestAnyOf

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksUpdateRequestAnyOf from a JSON string
webhooks_update_request_any_of_instance = WebhooksUpdateRequestAnyOf.from_json(json)
# print the JSON string representation of the object
print(WebhooksUpdateRequestAnyOf.to_json())

# convert the object into a dict
webhooks_update_request_any_of_dict = webhooks_update_request_any_of_instance.to_dict()
# create an instance of WebhooksUpdateRequestAnyOf from a dict
webhooks_update_request_any_of_from_dict = WebhooksUpdateRequestAnyOf.from_dict(webhooks_update_request_any_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


