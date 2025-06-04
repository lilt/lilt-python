# SDLXLIFFFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conf_name** | **str** | the current state of the SDLXLIFF Trans Unit. | 
**allowable_percentage** | **int** | This represents for the current conf_name what percentage the filter applies to.  If you pass -1 it will take any value for this field and won&#39;t ignore blank values. If you pass 50, Lilt will only import Segments that have a 50 percent match or better. | [optional] 
**allow_unlocked_segments** | **bool** | Boolean that tells Lilt whether we should allow unlocked Segments for this conf_name. | [optional] 

## Example

```python
from lilt.models.sdlxliff_filter import SDLXLIFFFilter

# TODO update the JSON string below
json = "{}"
# create an instance of SDLXLIFFFilter from a JSON string
sdlxliff_filter_instance = SDLXLIFFFilter.from_json(json)
# print the JSON string representation of the object
print(SDLXLIFFFilter.to_json())

# convert the object into a dict
sdlxliff_filter_dict = sdlxliff_filter_instance.to_dict()
# create an instance of SDLXLIFFFilter from a dict
sdlxliff_filter_from_dict = SDLXLIFFFilter.from_dict(sdlxliff_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


