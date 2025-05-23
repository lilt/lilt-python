# CreateWebhookOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_name** | **str** | The name of the webhook configuration. | 
**webhook_url** | **str** | The URL to which the webhook notifications will be sent. | 
**event_type** | **List[str]** | The list of event types that will trigger the webhook notification. | 

## Example

```python
from lilt.models.create_webhook_options import CreateWebhookOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebhookOptions from a JSON string
create_webhook_options_instance = CreateWebhookOptions.from_json(json)
# print the JSON string representation of the object
print(CreateWebhookOptions.to_json())

# convert the object into a dict
create_webhook_options_dict = create_webhook_options_instance.to_dict()
# create an instance of CreateWebhookOptions from a dict
create_webhook_options_from_dict = CreateWebhookOptions.from_dict(create_webhook_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


