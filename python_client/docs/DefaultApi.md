# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_drivers_driver_id_delete**](DefaultApi.md#api_drivers_driver_id_delete) | **DELETE** /api/drivers/{driver_id} | Delete a driver
[**api_drivers_driver_id_get**](DefaultApi.md#api_drivers_driver_id_get) | **GET** /api/drivers/{driver_id} | Get details of a specific driver
[**api_drivers_driver_id_patch**](DefaultApi.md#api_drivers_driver_id_patch) | **PATCH** /api/drivers/{driver_id} | Update driver details
[**api_drivers_get**](DefaultApi.md#api_drivers_get) | **GET** /api/drivers | Get a list of all drivers
[**api_drivers_post**](DefaultApi.md#api_drivers_post) | **POST** /api/drivers | Add a new driver


# **api_drivers_driver_id_delete**
> api_drivers_driver_id_delete(driver_id)

Delete a driver

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    driver_id = 56 # int | 

    try:
        # Delete a driver
        api_instance.api_drivers_driver_id_delete(driver_id)
    except Exception as e:
        print("Exception when calling DefaultApi->api_drivers_driver_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **driver_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Driver deleted successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_drivers_driver_id_get**
> api_drivers_driver_id_get(driver_id)

Get details of a specific driver

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    driver_id = 56 # int | 

    try:
        # Get details of a specific driver
        api_instance.api_drivers_driver_id_get(driver_id)
    except Exception as e:
        print("Exception when calling DefaultApi->api_drivers_driver_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **driver_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_drivers_driver_id_patch**
> api_drivers_driver_id_patch(driver_id, driver_updates)

Update driver details

### Example


```python
import openapi_client
from openapi_client.models.driver_updates import DriverUpdates
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    driver_id = 56 # int | 
    driver_updates = openapi_client.DriverUpdates() # DriverUpdates | 

    try:
        # Update driver details
        api_instance.api_drivers_driver_id_patch(driver_id, driver_updates)
    except Exception as e:
        print("Exception when calling DefaultApi->api_drivers_driver_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **driver_id** | **int**|  | 
 **driver_updates** | [**DriverUpdates**](DriverUpdates.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Driver updated successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_drivers_get**
> api_drivers_get()

Get a list of all drivers

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Get a list of all drivers
        api_instance.api_drivers_get()
    except Exception as e:
        print("Exception when calling DefaultApi->api_drivers_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_drivers_post**
> api_drivers_post(driver)

Add a new driver

### Example


```python
import openapi_client
from openapi_client.models.driver import Driver
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    driver = openapi_client.Driver() # Driver | 

    try:
        # Add a new driver
        api_instance.api_drivers_post(driver)
    except Exception as e:
        print("Exception when calling DefaultApi->api_drivers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **driver** | [**Driver**](Driver.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Driver added successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

