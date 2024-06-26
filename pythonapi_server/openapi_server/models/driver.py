from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class Driver(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, name=None, wins=None, poles=None):  # noqa: E501
        """Driver - a model defined in OpenAPI

        :param id: The id of this Driver.  # noqa: E501
        :type id: int
        :param name: The name of this Driver.  # noqa: E501
        :type name: str
        :param wins: The wins of this Driver.  # noqa: E501
        :type wins: int
        :param poles: The poles of this Driver.  # noqa: E501
        :type poles: int
        """
        self.openapi_types = {
            'id': int,
            'name': str,
            'wins': int,
            'poles': int
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'wins': 'wins',
            'poles': 'poles'
        }

        self._id = id
        self._name = name
        self._wins = wins
        self._poles = poles

    @classmethod
    def from_dict(cls, dikt) -> 'Driver':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Driver of this Driver.  # noqa: E501
        :rtype: Driver
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Driver.


        :return: The id of this Driver.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Driver.


        :param id: The id of this Driver.
        :type id: int
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this Driver.


        :return: The name of this Driver.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Driver.


        :param name: The name of this Driver.
        :type name: str
        """

        self._name = name

    @property
    def wins(self) -> int:
        """Gets the wins of this Driver.


        :return: The wins of this Driver.
        :rtype: int
        """
        return self._wins

    @wins.setter
    def wins(self, wins: int):
        """Sets the wins of this Driver.


        :param wins: The wins of this Driver.
        :type wins: int
        """

        self._wins = wins

    @property
    def poles(self) -> int:
        """Gets the poles of this Driver.


        :return: The poles of this Driver.
        :rtype: int
        """
        return self._poles

    @poles.setter
    def poles(self, poles: int):
        """Sets the poles of this Driver.


        :param poles: The poles of this Driver.
        :type poles: int
        """

        self._poles = poles
