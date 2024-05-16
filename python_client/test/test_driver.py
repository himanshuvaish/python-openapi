# coding: utf-8

"""
    Formula 1 Drivers API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.driver import Driver

class TestDriver(unittest.TestCase):
    """Driver unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Driver:
        """Test Driver
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Driver`
        """
        model = Driver()
        if include_optional:
            return Driver(
                id = 56,
                name = '',
                wins = 56,
                poles = 56
            )
        else:
            return Driver(
        )
        """

    def testDriver(self):
        """Test Driver"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
