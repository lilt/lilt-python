# GetS3UploadParams200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Pre-signed URL for file upload | [optional] 
**key** | **str** | Upload key identifier | [optional] 
**method** | **str** | HTTP method to use for upload | [optional] 

## Example

```python
from lilt.models.get_s3_upload_params200_response import GetS3UploadParams200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetS3UploadParams200Response from a JSON string
get_s3_upload_params200_response_instance = GetS3UploadParams200Response.from_json(json)
# print the JSON string representation of the object
print(GetS3UploadParams200Response.to_json())

# convert the object into a dict
get_s3_upload_params200_response_dict = get_s3_upload_params200_response_instance.to_dict()
# create an instance of GetS3UploadParams200Response from a dict
get_s3_upload_params200_response_from_dict = GetS3UploadParams200Response.from_dict(get_s3_upload_params200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


