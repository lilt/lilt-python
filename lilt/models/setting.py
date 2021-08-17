# coding: utf-8

"""
    Lilt REST API

    The Lilt REST API enables programmatic access to the full-range of Lilt backend services including:   * Training of and translating with interactive, adaptive machine translation   * Large-scale translation memory   * The Lexicon (a large-scale termbase)   * Programmatic control of the Lilt CAT environment   * Translation memory synchronization  Requests and responses are in JSON format. The REST API only responds to HTTPS / SSL requests. ## Authentication Requests are authenticated via REST API key, which requires the Business plan.  Requests are authenticated using [HTTP Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication). Add your REST API key as both the `username` and `password`.  For development, you may also pass the REST API key via the `key` query parameter. This is less secure than HTTP Basic Auth, and is not recommended for production use.   # noqa: E501

    The version of the OpenAPI document: v2.0
    Contact: support@lilt.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from lilt.configuration import Configuration


class Setting(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'int',
        'name': 'str',
        'value_type': 'str',
        'is_user_facing': 'bool',
        'is_default': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'value_type': 'valueType',
        'is_user_facing': 'isUserFacing',
        'is_default': 'isDefault'
    }

    def __init__(self, id=None, name=None, value_type=None, is_user_facing=None, is_default=None, local_vars_configuration=None):  # noqa: E501
        """Setting - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._value_type = None
        self._is_user_facing = None
        self._is_default = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if value_type is not None:
            self.value_type = value_type
        if is_user_facing is not None:
            self.is_user_facing = is_user_facing
        if is_default is not None:
            self.is_default = is_default

    @property
    def id(self):
        """Gets the id of this Setting.  # noqa: E501

        The identifier of the setting.  # noqa: E501

        :return: The id of this Setting.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Setting.

        The identifier of the setting.  # noqa: E501

        :param id: The id of this Setting.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Setting.  # noqa: E501

        The name of the setting.  # noqa: E501

        :return: The name of this Setting.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Setting.

        The name of the setting.  # noqa: E501

        :param name: The name of this Setting.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def value_type(self):
        """Gets the value_type of this Setting.  # noqa: E501

        the type of value the setting may have - Boolean, Json, Number, String.  # noqa: E501

        :return: The value_type of this Setting.  # noqa: E501
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this Setting.

        the type of value the setting may have - Boolean, Json, Number, String.  # noqa: E501

        :param value_type: The value_type of this Setting.  # noqa: E501
        :type: str
        """

        self._value_type = value_type

    @property
    def is_user_facing(self):
        """Gets the is_user_facing of this Setting.  # noqa: E501

        Whether the setting is editable by the user.  # noqa: E501

        :return: The is_user_facing of this Setting.  # noqa: E501
        :rtype: bool
        """
        return self._is_user_facing

    @is_user_facing.setter
    def is_user_facing(self, is_user_facing):
        """Sets the is_user_facing of this Setting.

        Whether the setting is editable by the user.  # noqa: E501

        :param is_user_facing: The is_user_facing of this Setting.  # noqa: E501
        :type: bool
        """

        self._is_user_facing = is_user_facing

    @property
    def is_default(self):
        """Gets the is_default of this Setting.  # noqa: E501

        True when the setting value is inherited from the default setting.  # noqa: E501

        :return: The is_default of this Setting.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this Setting.

        True when the setting value is inherited from the default setting.  # noqa: E501

        :param is_default: The is_default of this Setting.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Setting):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Setting):
            return True

        return self.to_dict() != other.to_dict()
