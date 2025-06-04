# WebhooksUpdateRequestAnyOf2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **List[str]** | The list of event types that will trigger the webhook notification. | 

## Example

```python
from lilt.models.webhooks_update_request_any_of2 import WebhooksUpdateRequestAnyOf2

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksUpdateRequestAnyOf2 from a JSON string
webhooks_update_request_any_of2_instance = WebhooksUpdateRequestAnyOf2.from_json(json)
# print the JSON string representation of the object
print(WebhooksUpdateRequestAnyOf2.to_json())

# convert the object into a dict
webhooks_update_request_any_of2_dict = webhooks_update_request_any_of2_instance.to_dict()
# create an instance of WebhooksUpdateRequestAnyOf2 from a dict
webhooks_update_request_any_of2_from_dict = WebhooksUpdateRequestAnyOf2.from_dict(webhooks_update_request_any_of2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


