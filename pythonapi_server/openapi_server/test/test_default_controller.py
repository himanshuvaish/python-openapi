import unittest

from flask import json

from openapi_server.models.driver import Driver  # noqa: E501
from openapi_server.models.driver_updates import DriverUpdates  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_api_drivers_driver_id_delete(self):
        """Test case for api_drivers_driver_id_delete

        Delete a driver
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/drivers/{driver_id}'.format(driver_id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_drivers_driver_id_get(self):
        """Test case for api_drivers_driver_id_get

        Get details of a specific driver
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/drivers/{driver_id}'.format(driver_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_drivers_driver_id_patch(self):
        """Test case for api_drivers_driver_id_patch

        Update driver details
        """
        driver_updates = {"wins":0,"poles":6}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/drivers/{driver_id}'.format(driver_id=56),
            method='PATCH',
            headers=headers,
            data=json.dumps(driver_updates),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_drivers_get(self):
        """Test case for api_drivers_get

        Get a list of all drivers
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/drivers',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_drivers_post(self):
        """Test case for api_drivers_post

        Add a new driver
        """
        driver = {"wins":6,"poles":1,"name":"name","id":0}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/drivers',
            method='POST',
            headers=headers,
            data=json.dumps(driver),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
