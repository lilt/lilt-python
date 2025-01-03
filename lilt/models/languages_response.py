# coding: utf-8

"""
    Lilt REST API

    Lilt REST API Support: https://lilt.atlassian.net/servicedesk/customer/portals    The Lilt REST API enables programmatic access to the full-range of Lilt backend services including:   * Training of and translating with interactive, adaptive machine translation   * Large-scale translation memory   * The Lexicon (a large-scale termbase)   * Programmatic control of the Lilt CAT environment   * Translation memory synchronization  Requests and responses are in JSON format. The REST API only responds to HTTPS / SSL requests.  The base url for this REST API is `https://api.lilt.com/`.  ## Authentication  Requests are authenticated via REST API key, which requires the Business plan.  Requests are authenticated using [HTTP Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication). Add your REST API key as both the `username` and `password`.  For development, you may also pass the REST API key via the `key` query parameter. This is less secure than HTTP Basic Auth, and is not recommended for production use.  ## Quotas  Our services have a general quota of 4000 requests per minute. Should you hit the maximum requests per minute, you will need to wait 60 seconds before you can send another request.   # noqa: E501

    The version of the OpenAPI document: v3.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from lilt.configuration import Configuration


class LanguagesResponse(object):
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
        'source_to_target': 'object',
        'code_to_name': 'object'
    }

    attribute_map = {
        'source_to_target': 'source_to_target',
        'code_to_name': 'code_to_name'
    }

    def __init__(self, source_to_target=None, code_to_name=None, local_vars_configuration=None):  # noqa: E501
        """LanguagesResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._source_to_target = None
        self._code_to_name = None
        self.discriminator = None

        if source_to_target is not None:
            self.source_to_target = source_to_target
        if code_to_name is not None:
            self.code_to_name = code_to_name

    @property
    def source_to_target(self):
        """Gets the source_to_target of this LanguagesResponse.  # noqa: E501

        A two-dimensional object in which the first key is an ISO 639-1 language code indicating the source, and the second key is an ISO 639-1 language code indicating the target.  # noqa: E501

        :return: The source_to_target of this LanguagesResponse.  # noqa: E501
        :rtype: object
        """
        return self._source_to_target

    @source_to_target.setter
    def source_to_target(self, source_to_target):
        """Sets the source_to_target of this LanguagesResponse.

        A two-dimensional object in which the first key is an ISO 639-1 language code indicating the source, and the second key is an ISO 639-1 language code indicating the target.  # noqa: E501

        :param source_to_target: The source_to_target of this LanguagesResponse.  # noqa: E501
        :type: object
        """

        self._source_to_target = source_to_target

    @property
    def code_to_name(self):
        """Gets the code_to_name of this LanguagesResponse.  # noqa: E501

        An object in which the key is an ISO 639-1 language code, and the value is the language name.  # noqa: E501

        :return: The code_to_name of this LanguagesResponse.  # noqa: E501
        :rtype: object
        """
        return self._code_to_name

    @code_to_name.setter
    def code_to_name(self, code_to_name):
        """Sets the code_to_name of this LanguagesResponse.

        An object in which the key is an ISO 639-1 language code, and the value is the language name.  # noqa: E501

        :param code_to_name: The code_to_name of this LanguagesResponse.  # noqa: E501
        :type: object
        """

        self._code_to_name = code_to_name

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
        if not isinstance(other, LanguagesResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LanguagesResponse):
            return True

        return self.to_dict() != other.to_dict()
