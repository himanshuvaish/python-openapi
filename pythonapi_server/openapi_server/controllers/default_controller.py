import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.driver import Driver  # noqa: E501
from openapi_server.models.driver_updates import DriverUpdates  # noqa: E501
from openapi_server import util


def api_drivers_driver_id_delete(driver_id):  # noqa: E501
    """Delete a driver

     # noqa: E501

    :param driver_id: 
    :type driver_id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def api_drivers_driver_id_get(driver_id):  # noqa: E501
    """Get details of a specific driver

     # noqa: E501

    :param driver_id: 
    :type driver_id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def api_drivers_driver_id_patch(driver_id, driver_updates):  # noqa: E501
    """Update driver details

     # noqa: E501

    :param driver_id: 
    :type driver_id: int
    :param driver_updates: 
    :type driver_updates: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        driver_updates = DriverUpdates.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def api_drivers_get():  # noqa: E501
    """Get a list of all drivers

     # noqa: E501


    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def api_drivers_post(driver):  # noqa: E501
    """Add a new driver

     # noqa: E501

    :param driver: 
    :type driver: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        driver = Driver.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
