# ProjectStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**source_words** | **int** |  | 
**exact_words** | **int** |  | 
**fuzzy_words** | **int** |  | 
**new_words** | **int** |  | 

## Example

```python
from lilt.models.project_stats import ProjectStats

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectStats from a JSON string
project_stats_instance = ProjectStats.from_json(json)
# print the JSON string representation of the object
print(ProjectStats.to_json())

# convert the object into a dict
project_stats_dict = project_stats_instance.to_dict()
# create an instance of ProjectStats from a dict
project_stats_from_dict = ProjectStats.from_dict(project_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


