# SettingUpsertBody

Body to create or update a setting.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**setting_name** | **str** | The name of the setting. | [optional] 
**scope** | **str** | The entity scope the setting should be applied to. | [optional] 
**is_enforced** | **bool** | Whether this value should override others set for the same setting key.  | [optional] 
**project_id** | **float** | Id of the the project the setting will be applied to. Required when scope is &#x60;Project&#x60;. | [optional] 
**organization_id** | **float** | Id of the the project the setting will be applied to. Required when scope is &#x60;Organization&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


