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


class ProjectStatus(object):
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
        'num_source_words': 'int',
        'num_words_confirmed': 'int',
        'num_words_reviewed': 'int',
        'time_elapsed': 'int',
        'time_elapsed_translation': 'int',
        'time_elapsed_research': 'int',
        'time_elapsed_review': 'int',
        'updated_at': 'int',
        'resources': 'list[ResourceStatus]'
    }

    attribute_map = {
        'id': 'id',
        'num_source_words': 'num_source_words',
        'num_words_confirmed': 'num_words_confirmed',
        'num_words_reviewed': 'num_words_reviewed',
        'time_elapsed': 'time_elapsed',
        'time_elapsed_translation': 'time_elapsed_translation',
        'time_elapsed_research': 'time_elapsed_research',
        'time_elapsed_review': 'time_elapsed_review',
        'updated_at': 'updated_at',
        'resources': 'resources'
    }

    def __init__(self, id=None, num_source_words=None, num_words_confirmed=None, num_words_reviewed=None, time_elapsed=None, time_elapsed_translation=None, time_elapsed_research=None, time_elapsed_review=None, updated_at=None, resources=None, local_vars_configuration=None):  # noqa: E501
        """ProjectStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._num_source_words = None
        self._num_words_confirmed = None
        self._num_words_reviewed = None
        self._time_elapsed = None
        self._time_elapsed_translation = None
        self._time_elapsed_research = None
        self._time_elapsed_review = None
        self._updated_at = None
        self._resources = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if num_source_words is not None:
            self.num_source_words = num_source_words
        if num_words_confirmed is not None:
            self.num_words_confirmed = num_words_confirmed
        if num_words_reviewed is not None:
            self.num_words_reviewed = num_words_reviewed
        if time_elapsed is not None:
            self.time_elapsed = time_elapsed
        if time_elapsed_translation is not None:
            self.time_elapsed_translation = time_elapsed_translation
        if time_elapsed_research is not None:
            self.time_elapsed_research = time_elapsed_research
        if time_elapsed_review is not None:
            self.time_elapsed_review = time_elapsed_review
        if updated_at is not None:
            self.updated_at = updated_at
        if resources is not None:
            self.resources = resources

    @property
    def id(self):
        """Gets the id of this ProjectStatus.  # noqa: E501

        A unique Project identifier.  # noqa: E501

        :return: The id of this ProjectStatus.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectStatus.

        A unique Project identifier.  # noqa: E501

        :param id: The id of this ProjectStatus.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def num_source_words(self):
        """Gets the num_source_words of this ProjectStatus.  # noqa: E501

        The number of source words in the Project.  # noqa: E501

        :return: The num_source_words of this ProjectStatus.  # noqa: E501
        :rtype: int
        """
        return self._num_source_words

    @num_source_words.setter
    def num_source_words(self, num_source_words):
        """Sets the num_source_words of this ProjectStatus.

        The number of source words in the Project.  # noqa: E501

        :param num_source_words: The num_source_words of this ProjectStatus.  # noqa: E501
        :type: int
        """

        self._num_source_words = num_source_words

    @property
    def num_words_confirmed(self):
        """Gets the num_words_confirmed of this ProjectStatus.  # noqa: E501

        The number of confirmed source words.  # noqa: E501

        :return: The num_words_confirmed of this ProjectStatus.  # noqa: E501
        :rtype: int
        """
        return self._num_words_confirmed

    @num_words_confirmed.setter
    def num_words_confirmed(self, num_words_confirmed):
        """Sets the num_words_confirmed of this ProjectStatus.

        The number of confirmed source words.  # noqa: E501

        :param num_words_confirmed: The num_words_confirmed of this ProjectStatus.  # noqa: E501
        :type: int
        """

        self._num_words_confirmed = num_words_confirmed

    @property
    def num_words_reviewed(self):
        """Gets the num_words_reviewed of this ProjectStatus.  # noqa: E501

        The number of reviewed source words.  # noqa: E501

        :return: The num_words_reviewed of this ProjectStatus.  # noqa: E501
        :rtype: int
        """
        return self._num_words_reviewed

    @num_words_reviewed.setter
    def num_words_reviewed(self, num_words_reviewed):
        """Sets the num_words_reviewed of this ProjectStatus.

        The number of reviewed source words.  # noqa: E501

        :param num_words_reviewed: The num_words_reviewed of this ProjectStatus.  # noqa: E501
        :type: int
        """

        self._num_words_reviewed = num_words_reviewed

    @property
    def time_elapsed(self):
        """Gets the time_elapsed of this ProjectStatus.  # noqa: E501

        The total time spent on the project by all resources. Measured in milliseconds.  # noqa: E501

        :return: The time_elapsed of this ProjectStatus.  # noqa: E501
        :rtype: int
        """
        return self._time_elapsed

    @time_elapsed.setter
    def time_elapsed(self, time_elapsed):
        """Sets the time_elapsed of this ProjectStatus.

        The total time spent on the project by all resources. Measured in milliseconds.  # noqa: E501

        :param time_elapsed: The time_elapsed of this ProjectStatus.  # noqa: E501
        :type: int
        """

        self._time_elapsed = time_elapsed

    @property
    def time_elapsed_translation(self):
        """Gets the time_elapsed_translation of this ProjectStatus.  # noqa: E501

        The total time spent on translation by all resources. Measured in milliseconds.  # noqa: E501

        :return: The time_elapsed_translation of this ProjectStatus.  # noqa: E501
        :rtype: int
        """
        return self._time_elapsed_translation

    @time_elapsed_translation.setter
    def time_elapsed_translation(self, time_elapsed_translation):
        """Sets the time_elapsed_translation of this ProjectStatus.

        The total time spent on translation by all resources. Measured in milliseconds.  # noqa: E501

        :param time_elapsed_translation: The time_elapsed_translation of this ProjectStatus.  # noqa: E501
        :type: int
        """

        self._time_elapsed_translation = time_elapsed_translation

    @property
    def time_elapsed_research(self):
        """Gets the time_elapsed_research of this ProjectStatus.  # noqa: E501

        The total time spent on research by all resources. Measured in milliseconds.  # noqa: E501

        :return: The time_elapsed_research of this ProjectStatus.  # noqa: E501
        :rtype: int
        """
        return self._time_elapsed_research

    @time_elapsed_research.setter
    def time_elapsed_research(self, time_elapsed_research):
        """Sets the time_elapsed_research of this ProjectStatus.

        The total time spent on research by all resources. Measured in milliseconds.  # noqa: E501

        :param time_elapsed_research: The time_elapsed_research of this ProjectStatus.  # noqa: E501
        :type: int
        """

        self._time_elapsed_research = time_elapsed_research

    @property
    def time_elapsed_review(self):
        """Gets the time_elapsed_review of this ProjectStatus.  # noqa: E501

        The total time spent on reviewing by all resources. Measured in milliseconds.  # noqa: E501

        :return: The time_elapsed_review of this ProjectStatus.  # noqa: E501
        :rtype: int
        """
        return self._time_elapsed_review

    @time_elapsed_review.setter
    def time_elapsed_review(self, time_elapsed_review):
        """Sets the time_elapsed_review of this ProjectStatus.

        The total time spent on reviewing by all resources. Measured in milliseconds.  # noqa: E501

        :param time_elapsed_review: The time_elapsed_review of this ProjectStatus.  # noqa: E501
        :type: int
        """

        self._time_elapsed_review = time_elapsed_review

    @property
    def updated_at(self):
        """Gets the updated_at of this ProjectStatus.  # noqa: E501

        The project update date and time. Measured in seconds.  # noqa: E501

        :return: The updated_at of this ProjectStatus.  # noqa: E501
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ProjectStatus.

        The project update date and time. Measured in seconds.  # noqa: E501

        :param updated_at: The updated_at of this ProjectStatus.  # noqa: E501
        :type: int
        """

        self._updated_at = updated_at

    @property
    def resources(self):
        """Gets the resources of this ProjectStatus.  # noqa: E501

        A list of ResourceStatus objects that represent per-resource statistics.  # noqa: E501

        :return: The resources of this ProjectStatus.  # noqa: E501
        :rtype: list[ResourceStatus]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ProjectStatus.

        A list of ResourceStatus objects that represent per-resource statistics.  # noqa: E501

        :param resources: The resources of this ProjectStatus.  # noqa: E501
        :type: list[ResourceStatus]
        """

        self._resources = resources

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
        if not isinstance(other, ProjectStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectStatus):
            return True

        return self.to_dict() != other.to_dict()
