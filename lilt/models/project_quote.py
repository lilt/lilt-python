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


class ProjectQuote(object):
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
        'num_words_new': 'int',
        'num_segments_new': 'int',
        'num_words_repetition': 'int',
        'num_segments_repetition': 'int',
        'bands': 'list[MatchBand]',
        'documents': 'list[DocumentQuote]'
    }

    attribute_map = {
        'id': 'id',
        'num_source_words': 'num_source_words',
        'num_words_new': 'num_words_new',
        'num_segments_new': 'num_segments_new',
        'num_words_repetition': 'num_words_repetition',
        'num_segments_repetition': 'num_segments_repetition',
        'bands': 'bands',
        'documents': 'documents'
    }

    def __init__(self, id=None, num_source_words=None, num_words_new=None, num_segments_new=None, num_words_repetition=None, num_segments_repetition=None, bands=None, documents=None, local_vars_configuration=None):  # noqa: E501
        """ProjectQuote - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._num_source_words = None
        self._num_words_new = None
        self._num_segments_new = None
        self._num_words_repetition = None
        self._num_segments_repetition = None
        self._bands = None
        self._documents = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if num_source_words is not None:
            self.num_source_words = num_source_words
        if num_words_new is not None:
            self.num_words_new = num_words_new
        if num_segments_new is not None:
            self.num_segments_new = num_segments_new
        if num_words_repetition is not None:
            self.num_words_repetition = num_words_repetition
        if num_segments_repetition is not None:
            self.num_segments_repetition = num_segments_repetition
        if bands is not None:
            self.bands = bands
        if documents is not None:
            self.documents = documents

    @property
    def id(self):
        """Gets the id of this ProjectQuote.  # noqa: E501

        A unique Project identifier.  # noqa: E501

        :return: The id of this ProjectQuote.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectQuote.

        A unique Project identifier.  # noqa: E501

        :param id: The id of this ProjectQuote.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def num_source_words(self):
        """Gets the num_source_words of this ProjectQuote.  # noqa: E501

        The number of source words in the Project.  # noqa: E501

        :return: The num_source_words of this ProjectQuote.  # noqa: E501
        :rtype: int
        """
        return self._num_source_words

    @num_source_words.setter
    def num_source_words(self, num_source_words):
        """Sets the num_source_words of this ProjectQuote.

        The number of source words in the Project.  # noqa: E501

        :param num_source_words: The num_source_words of this ProjectQuote.  # noqa: E501
        :type: int
        """

        self._num_source_words = num_source_words

    @property
    def num_words_new(self):
        """Gets the num_words_new of this ProjectQuote.  # noqa: E501

        The number of new source words in the Project.  # noqa: E501

        :return: The num_words_new of this ProjectQuote.  # noqa: E501
        :rtype: int
        """
        return self._num_words_new

    @num_words_new.setter
    def num_words_new(self, num_words_new):
        """Sets the num_words_new of this ProjectQuote.

        The number of new source words in the Project.  # noqa: E501

        :param num_words_new: The num_words_new of this ProjectQuote.  # noqa: E501
        :type: int
        """

        self._num_words_new = num_words_new

    @property
    def num_segments_new(self):
        """Gets the num_segments_new of this ProjectQuote.  # noqa: E501

        The number of new segments in the Project.  # noqa: E501

        :return: The num_segments_new of this ProjectQuote.  # noqa: E501
        :rtype: int
        """
        return self._num_segments_new

    @num_segments_new.setter
    def num_segments_new(self, num_segments_new):
        """Sets the num_segments_new of this ProjectQuote.

        The number of new segments in the Project.  # noqa: E501

        :param num_segments_new: The num_segments_new of this ProjectQuote.  # noqa: E501
        :type: int
        """

        self._num_segments_new = num_segments_new

    @property
    def num_words_repetition(self):
        """Gets the num_words_repetition of this ProjectQuote.  # noqa: E501

        The number of repetition source words in the Project.  # noqa: E501

        :return: The num_words_repetition of this ProjectQuote.  # noqa: E501
        :rtype: int
        """
        return self._num_words_repetition

    @num_words_repetition.setter
    def num_words_repetition(self, num_words_repetition):
        """Sets the num_words_repetition of this ProjectQuote.

        The number of repetition source words in the Project.  # noqa: E501

        :param num_words_repetition: The num_words_repetition of this ProjectQuote.  # noqa: E501
        :type: int
        """

        self._num_words_repetition = num_words_repetition

    @property
    def num_segments_repetition(self):
        """Gets the num_segments_repetition of this ProjectQuote.  # noqa: E501

        The number of repetition segments in the Project.  # noqa: E501

        :return: The num_segments_repetition of this ProjectQuote.  # noqa: E501
        :rtype: int
        """
        return self._num_segments_repetition

    @num_segments_repetition.setter
    def num_segments_repetition(self, num_segments_repetition):
        """Sets the num_segments_repetition of this ProjectQuote.

        The number of repetition segments in the Project.  # noqa: E501

        :param num_segments_repetition: The num_segments_repetition of this ProjectQuote.  # noqa: E501
        :type: int
        """

        self._num_segments_repetition = num_segments_repetition

    @property
    def bands(self):
        """Gets the bands of this ProjectQuote.  # noqa: E501

        A list of MatchBand objects that represent translation memory leverage statistics.  # noqa: E501

        :return: The bands of this ProjectQuote.  # noqa: E501
        :rtype: list[MatchBand]
        """
        return self._bands

    @bands.setter
    def bands(self, bands):
        """Sets the bands of this ProjectQuote.

        A list of MatchBand objects that represent translation memory leverage statistics.  # noqa: E501

        :param bands: The bands of this ProjectQuote.  # noqa: E501
        :type: list[MatchBand]
        """

        self._bands = bands

    @property
    def documents(self):
        """Gets the documents of this ProjectQuote.  # noqa: E501

        A list of DocumentQuote objects that quotes information for a Document.  # noqa: E501

        :return: The documents of this ProjectQuote.  # noqa: E501
        :rtype: list[DocumentQuote]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """Sets the documents of this ProjectQuote.

        A list of DocumentQuote objects that quotes information for a Document.  # noqa: E501

        :param documents: The documents of this ProjectQuote.  # noqa: E501
        :type: list[DocumentQuote]
        """

        self._documents = documents

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
        if not isinstance(other, ProjectQuote):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectQuote):
            return True

        return self.to_dict() != other.to_dict()
