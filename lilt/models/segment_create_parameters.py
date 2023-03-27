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


class SegmentCreateParameters(object):
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
        'memory_id': 'int',
        'document_id': 'int',
        'source': 'str',
        'target': 'str'
    }

    attribute_map = {
        'memory_id': 'memory_id',
        'document_id': 'document_id',
        'source': 'source',
        'target': 'target'
    }

    def __init__(self, memory_id=None, document_id=None, source=None, target=None, local_vars_configuration=None):  # noqa: E501
        """SegmentCreateParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._memory_id = None
        self._document_id = None
        self._source = None
        self._target = None
        self.discriminator = None

        if memory_id is not None:
            self.memory_id = memory_id
        if document_id is not None:
            self.document_id = document_id
        self.source = source
        if target is not None:
            self.target = target

    @property
    def memory_id(self):
        """Gets the memory_id of this SegmentCreateParameters.  # noqa: E501

        A unique Memory identifier.  # noqa: E501

        :return: The memory_id of this SegmentCreateParameters.  # noqa: E501
        :rtype: int
        """
        return self._memory_id

    @memory_id.setter
    def memory_id(self, memory_id):
        """Sets the memory_id of this SegmentCreateParameters.

        A unique Memory identifier.  # noqa: E501

        :param memory_id: The memory_id of this SegmentCreateParameters.  # noqa: E501
        :type: int
        """

        self._memory_id = memory_id

    @property
    def document_id(self):
        """Gets the document_id of this SegmentCreateParameters.  # noqa: E501

        A unique Document identifier.  # noqa: E501

        :return: The document_id of this SegmentCreateParameters.  # noqa: E501
        :rtype: int
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this SegmentCreateParameters.

        A unique Document identifier.  # noqa: E501

        :param document_id: The document_id of this SegmentCreateParameters.  # noqa: E501
        :type: int
        """

        self._document_id = document_id

    @property
    def source(self):
        """Gets the source of this SegmentCreateParameters.  # noqa: E501

        The source string.  # noqa: E501

        :return: The source of this SegmentCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this SegmentCreateParameters.

        The source string.  # noqa: E501

        :param source: The source of this SegmentCreateParameters.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and source is None:  # noqa: E501
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def target(self):
        """Gets the target of this SegmentCreateParameters.  # noqa: E501

        The target string.  # noqa: E501

        :return: The target of this SegmentCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this SegmentCreateParameters.

        The target string.  # noqa: E501

        :param target: The target of this SegmentCreateParameters.  # noqa: E501
        :type: str
        """

        self._target = target

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
        if not isinstance(other, SegmentCreateParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SegmentCreateParameters):
            return True

        return self.to_dict() != other.to_dict()
