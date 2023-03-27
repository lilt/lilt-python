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


class QARuleMatches(object):
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
        'matches': 'list[QARuleMatchesMatches]',
        'custom_rules': 'list[QARuleMatchesCustomRules]'
    }

    attribute_map = {
        'matches': 'matches',
        'custom_rules': 'custom_rules'
    }

    def __init__(self, matches=None, custom_rules=None, local_vars_configuration=None):  # noqa: E501
        """QARuleMatches - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._matches = None
        self._custom_rules = None
        self.discriminator = None

        if matches is not None:
            self.matches = matches
        if custom_rules is not None:
            self.custom_rules = custom_rules

    @property
    def matches(self):
        """Gets the matches of this QARuleMatches.  # noqa: E501


        :return: The matches of this QARuleMatches.  # noqa: E501
        :rtype: list[QARuleMatchesMatches]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this QARuleMatches.


        :param matches: The matches of this QARuleMatches.  # noqa: E501
        :type: list[QARuleMatchesMatches]
        """

        self._matches = matches

    @property
    def custom_rules(self):
        """Gets the custom_rules of this QARuleMatches.  # noqa: E501


        :return: The custom_rules of this QARuleMatches.  # noqa: E501
        :rtype: list[QARuleMatchesCustomRules]
        """
        return self._custom_rules

    @custom_rules.setter
    def custom_rules(self, custom_rules):
        """Sets the custom_rules of this QARuleMatches.


        :param custom_rules: The custom_rules of this QARuleMatches.  # noqa: E501
        :type: list[QARuleMatchesCustomRules]
        """

        self._custom_rules = custom_rules

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
        if not isinstance(other, QARuleMatches):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QARuleMatches):
            return True

        return self.to_dict() != other.to_dict()
