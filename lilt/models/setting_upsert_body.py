# coding: utf-8

"""
    Lilt REST API

    The Lilt REST API enables programmatic access to the full-range of Lilt backend services including:   * Training of and translating with interactive, adaptive machine translation   * Large-scale translation memory   * The Lexicon (a large-scale termbase)   * Programmatic control of the Lilt CAT environment   * Translation memory synchronization  Requests and responses are in JSON format. The REST API only responds to HTTPS / SSL requests.  ## Authentication  Requests are authenticated via REST API key, which requires the Business plan.  Requests are authenticated using [HTTP Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication). Add your REST API key as both the `username` and `password`.  For development, you may also pass the REST API key via the `key` query parameter. This is less secure than HTTP Basic Auth, and is not recommended for production use.  ## Quotas  Our services have a general quota of 4000 requests per minute. Should you hit the maximum requests per minute, you will need to wait 60 seconds before you can send another request.   # noqa: E501

    The version of the OpenAPI document: v2.0
    Contact: support@lilt.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from lilt.configuration import Configuration


class SettingUpsertBody(object):
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
        'setting_name': 'str',
        'scope': 'str',
        'is_enforced': 'bool',
        'project_id': 'float',
        'organization_id': 'float'
    }

    attribute_map = {
        'setting_name': 'settingName',
        'scope': 'scope',
        'is_enforced': 'isEnforced',
        'project_id': 'projectId',
        'organization_id': 'organizationId'
    }

    def __init__(self, setting_name=None, scope=None, is_enforced=None, project_id=None, organization_id=None, local_vars_configuration=None):  # noqa: E501
        """SettingUpsertBody - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._setting_name = None
        self._scope = None
        self._is_enforced = None
        self._project_id = None
        self._organization_id = None
        self.discriminator = None

        self.setting_name = setting_name
        self.scope = scope
        if is_enforced is not None:
            self.is_enforced = is_enforced
        if project_id is not None:
            self.project_id = project_id
        if organization_id is not None:
            self.organization_id = organization_id

    @property
    def setting_name(self):
        """Gets the setting_name of this SettingUpsertBody.  # noqa: E501

        The name of the setting.  # noqa: E501

        :return: The setting_name of this SettingUpsertBody.  # noqa: E501
        :rtype: str
        """
        return self._setting_name

    @setting_name.setter
    def setting_name(self, setting_name):
        """Sets the setting_name of this SettingUpsertBody.

        The name of the setting.  # noqa: E501

        :param setting_name: The setting_name of this SettingUpsertBody.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and setting_name is None:  # noqa: E501
            raise ValueError("Invalid value for `setting_name`, must not be `None`")  # noqa: E501

        self._setting_name = setting_name

    @property
    def scope(self):
        """Gets the scope of this SettingUpsertBody.  # noqa: E501

        The entity scope the setting should be applied to.  # noqa: E501

        :return: The scope of this SettingUpsertBody.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this SettingUpsertBody.

        The entity scope the setting should be applied to.  # noqa: E501

        :param scope: The scope of this SettingUpsertBody.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and scope is None:  # noqa: E501
            raise ValueError("Invalid value for `scope`, must not be `None`")  # noqa: E501

        self._scope = scope

    @property
    def is_enforced(self):
        """Gets the is_enforced of this SettingUpsertBody.  # noqa: E501

        Whether this value should override others set for the same setting key.   # noqa: E501

        :return: The is_enforced of this SettingUpsertBody.  # noqa: E501
        :rtype: bool
        """
        return self._is_enforced

    @is_enforced.setter
    def is_enforced(self, is_enforced):
        """Sets the is_enforced of this SettingUpsertBody.

        Whether this value should override others set for the same setting key.   # noqa: E501

        :param is_enforced: The is_enforced of this SettingUpsertBody.  # noqa: E501
        :type: bool
        """

        self._is_enforced = is_enforced

    @property
    def project_id(self):
        """Gets the project_id of this SettingUpsertBody.  # noqa: E501

        Id of the the project the setting will be applied to. Required when scope is `Project`.   # noqa: E501

        :return: The project_id of this SettingUpsertBody.  # noqa: E501
        :rtype: float
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this SettingUpsertBody.

        Id of the the project the setting will be applied to. Required when scope is `Project`.   # noqa: E501

        :param project_id: The project_id of this SettingUpsertBody.  # noqa: E501
        :type: float
        """

        self._project_id = project_id

    @property
    def organization_id(self):
        """Gets the organization_id of this SettingUpsertBody.  # noqa: E501

        Id of the the project the setting will be applied to. Required when scope is `Organization`.   # noqa: E501

        :return: The organization_id of this SettingUpsertBody.  # noqa: E501
        :rtype: float
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this SettingUpsertBody.

        Id of the the project the setting will be applied to. Required when scope is `Organization`.   # noqa: E501

        :param organization_id: The organization_id of this SettingUpsertBody.  # noqa: E501
        :type: float
        """

        self._organization_id = organization_id

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
        if not isinstance(other, SettingUpsertBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SettingUpsertBody):
            return True

        return self.to_dict() != other.to_dict()
