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


class ConnectorArguments(object):
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
        'args': 'object',
        'schedule': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'args': 'args',
        'schedule': 'schedule'
    }

    def __init__(self, id=None, name=None, args=None, schedule=None, local_vars_configuration=None):  # noqa: E501
        """ConnectorArguments - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._args = None
        self._schedule = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if args is not None:
            self.args = args
        if schedule is not None:
            self.schedule = schedule

    @property
    def id(self):
        """Gets the id of this ConnectorArguments.  # noqa: E501

        A unique Connector identifier.  # noqa: E501

        :return: The id of this ConnectorArguments.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConnectorArguments.

        A unique Connector identifier.  # noqa: E501

        :param id: The id of this ConnectorArguments.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ConnectorArguments.  # noqa: E501

        Name of connector.  # noqa: E501

        :return: The name of this ConnectorArguments.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConnectorArguments.

        Name of connector.  # noqa: E501

        :param name: The name of this ConnectorArguments.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def args(self):
        """Gets the args of this ConnectorArguments.  # noqa: E501

        Connector parameters.  # noqa: E501

        :return: The args of this ConnectorArguments.  # noqa: E501
        :rtype: object
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this ConnectorArguments.

        Connector parameters.  # noqa: E501

        :param args: The args of this ConnectorArguments.  # noqa: E501
        :type: object
        """

        self._args = args

    @property
    def schedule(self):
        """Gets the schedule of this ConnectorArguments.  # noqa: E501

        Cron string  # noqa: E501

        :return: The schedule of this ConnectorArguments.  # noqa: E501
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this ConnectorArguments.

        Cron string  # noqa: E501

        :param schedule: The schedule of this ConnectorArguments.  # noqa: E501
        :type: str
        """

        self._schedule = schedule

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
        if not isinstance(other, ConnectorArguments):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConnectorArguments):
            return True

        return self.to_dict() != other.to_dict()
