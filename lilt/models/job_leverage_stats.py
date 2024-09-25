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


class JobLeverageStats(object):
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
        'source_words': 'int',
        'exact_words': 'int',
        'fuzzy_words': 'int',
        'new_words': 'int',
        'projects': 'list[ProjectStats]'
    }

    attribute_map = {
        'source_words': 'sourceWords',
        'exact_words': 'exactWords',
        'fuzzy_words': 'fuzzyWords',
        'new_words': 'newWords',
        'projects': 'projects'
    }

    def __init__(self, source_words=None, exact_words=None, fuzzy_words=None, new_words=None, projects=None, local_vars_configuration=None):  # noqa: E501
        """JobLeverageStats - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._source_words = None
        self._exact_words = None
        self._fuzzy_words = None
        self._new_words = None
        self._projects = None
        self.discriminator = None

        if source_words is not None:
            self.source_words = source_words
        if exact_words is not None:
            self.exact_words = exact_words
        if fuzzy_words is not None:
            self.fuzzy_words = fuzzy_words
        if new_words is not None:
            self.new_words = new_words
        if projects is not None:
            self.projects = projects

    @property
    def source_words(self):
        """Gets the source_words of this JobLeverageStats.  # noqa: E501

        Total number of source words.  # noqa: E501

        :return: The source_words of this JobLeverageStats.  # noqa: E501
        :rtype: int
        """
        return self._source_words

    @source_words.setter
    def source_words(self, source_words):
        """Sets the source_words of this JobLeverageStats.

        Total number of source words.  # noqa: E501

        :param source_words: The source_words of this JobLeverageStats.  # noqa: E501
        :type: int
        """

        self._source_words = source_words

    @property
    def exact_words(self):
        """Gets the exact_words of this JobLeverageStats.  # noqa: E501

        Total number of exact words.  # noqa: E501

        :return: The exact_words of this JobLeverageStats.  # noqa: E501
        :rtype: int
        """
        return self._exact_words

    @exact_words.setter
    def exact_words(self, exact_words):
        """Sets the exact_words of this JobLeverageStats.

        Total number of exact words.  # noqa: E501

        :param exact_words: The exact_words of this JobLeverageStats.  # noqa: E501
        :type: int
        """

        self._exact_words = exact_words

    @property
    def fuzzy_words(self):
        """Gets the fuzzy_words of this JobLeverageStats.  # noqa: E501

        Total number of fuzzy words.  # noqa: E501

        :return: The fuzzy_words of this JobLeverageStats.  # noqa: E501
        :rtype: int
        """
        return self._fuzzy_words

    @fuzzy_words.setter
    def fuzzy_words(self, fuzzy_words):
        """Sets the fuzzy_words of this JobLeverageStats.

        Total number of fuzzy words.  # noqa: E501

        :param fuzzy_words: The fuzzy_words of this JobLeverageStats.  # noqa: E501
        :type: int
        """

        self._fuzzy_words = fuzzy_words

    @property
    def new_words(self):
        """Gets the new_words of this JobLeverageStats.  # noqa: E501

        Total number of new words.  # noqa: E501

        :return: The new_words of this JobLeverageStats.  # noqa: E501
        :rtype: int
        """
        return self._new_words

    @new_words.setter
    def new_words(self, new_words):
        """Sets the new_words of this JobLeverageStats.

        Total number of new words.  # noqa: E501

        :param new_words: The new_words of this JobLeverageStats.  # noqa: E501
        :type: int
        """

        self._new_words = new_words

    @property
    def projects(self):
        """Gets the projects of this JobLeverageStats.  # noqa: E501


        :return: The projects of this JobLeverageStats.  # noqa: E501
        :rtype: list[ProjectStats]
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        """Sets the projects of this JobLeverageStats.


        :param projects: The projects of this JobLeverageStats.  # noqa: E501
        :type: list[ProjectStats]
        """

        self._projects = projects

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
        if not isinstance(other, JobLeverageStats):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JobLeverageStats):
            return True

        return self.to_dict() != other.to_dict()
