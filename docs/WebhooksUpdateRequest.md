# WebhooksUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_name** | **str** | The name of the webhook configuration. | 
**webhook_url** | **str** | The URL to which the webhook notifications will be sent. | 
**event_type** | **List[str]** | The list of event types that will trigger the webhook notification. | 

## Example

```python
from lilt.models.webhooks_update_request import WebhooksUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksUpdateRequest from a JSON string
webhooks_update_request_instance = WebhooksUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(WebhooksUpdateRequest.to_json())

# convert the object into a dict
webhooks_update_request_dict = webhooks_update_request_instance.to_dict()
# create an instance of WebhooksUpdateRequest from a dict
webhooks_update_request_from_dict = WebhooksUpdateRequest.from_dict(webhooks_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


