# Driver


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**wins** | **int** |  | [optional] 
**poles** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.driver import Driver

# TODO update the JSON string below
json = "{}"
# create an instance of Driver from a JSON string
driver_instance = Driver.from_json(json)
# print the JSON string representation of the object
print(Driver.to_json())

# convert the object into a dict
driver_dict = driver_instance.to_dict()
# create an instance of Driver from a dict
driver_from_dict = Driver.from_dict(driver_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


