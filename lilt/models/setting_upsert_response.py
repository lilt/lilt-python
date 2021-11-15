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


class SettingUpsertResponse(object):
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
        'scoped_setting': 'Setting',
        'active_settings': 'dict(str, Setting)'
    }

    attribute_map = {
        'scoped_setting': 'scopedSetting',
        'active_settings': 'activeSettings'
    }

    def __init__(self, scoped_setting=None, active_settings=None, local_vars_configuration=None):  # noqa: E501
        """SettingUpsertResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._scoped_setting = None
        self._active_settings = None
        self.discriminator = None

        if scoped_setting is not None:
            self.scoped_setting = scoped_setting
        if active_settings is not None:
            self.active_settings = active_settings

    @property
    def scoped_setting(self):
        """Gets the scoped_setting of this SettingUpsertResponse.  # noqa: E501


        :return: The scoped_setting of this SettingUpsertResponse.  # noqa: E501
        :rtype: Setting
        """
        return self._scoped_setting

    @scoped_setting.setter
    def scoped_setting(self, scoped_setting):
        """Sets the scoped_setting of this SettingUpsertResponse.


        :param scoped_setting: The scoped_setting of this SettingUpsertResponse.  # noqa: E501
        :type: Setting
        """

        self._scoped_setting = scoped_setting

    @property
    def active_settings(self):
        """Gets the active_settings of this SettingUpsertResponse.  # noqa: E501

        A dictionary of configuration settings, keyed by setting name  # noqa: E501

        :return: The active_settings of this SettingUpsertResponse.  # noqa: E501
        :rtype: dict(str, Setting)
        """
        return self._active_settings

    @active_settings.setter
    def active_settings(self, active_settings):
        """Sets the active_settings of this SettingUpsertResponse.

        A dictionary of configuration settings, keyed by setting name  # noqa: E501

        :param active_settings: The active_settings of this SettingUpsertResponse.  # noqa: E501
        :type: dict(str, Setting)
        """

        self._active_settings = active_settings

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
        if not isinstance(other, SettingUpsertResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SettingUpsertResponse):
            return True

        return self.to_dict() != other.to_dict()
