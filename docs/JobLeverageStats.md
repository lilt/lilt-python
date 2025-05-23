# JobLeverageStats

A job leverage stats object shows an overview of job's statistical data including total number of exact words, fuzzy words, and exact words for the job in total and for each project. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_words** | **int** | Total number of source words. | [optional] 
**exact_words** | **int** | Total number of exact words. | [optional] 
**fuzzy_words** | **int** | Total number of fuzzy words. | [optional] 
**new_words** | **int** | Total number of new words. | [optional] 
**projects** | [**List[ProjectStats]**](ProjectStats.md) |  | [optional] 

## Example

```python
from lilt.models.job_leverage_stats import JobLeverageStats

# TODO update the JSON string below
json = "{}"
# create an instance of JobLeverageStats from a JSON string
job_leverage_stats_instance = JobLeverageStats.from_json(json)
# print the JSON string representation of the object
print(JobLeverageStats.to_json())

# convert the object into a dict
job_leverage_stats_dict = job_leverage_stats_instance.to_dict()
# create an instance of JobLeverageStats from a dict
job_leverage_stats_from_dict = JobLeverageStats.from_dict(job_leverage_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


