# WebhookResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for the webhook configuration. | 
**webhook_name** | **str** | The name of the webhook configuration. | 
**webhook_url** | **str** | The URL to which the webhook notifications will be sent. | 
**event_type** | **List[str]** | The list of event types that will trigger the webhook notification. | 

## Example

```python
from lilt.models.webhook_response import WebhookResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookResponse from a JSON string
webhook_response_instance = WebhookResponse.from_json(json)
# print the JSON string representation of the object
print(WebhookResponse.to_json())

# convert the object into a dict
webhook_response_dict = webhook_response_instance.to_dict()
# create an instance of WebhookResponse from a dict
webhook_response_from_dict = WebhookResponse.from_dict(webhook_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


