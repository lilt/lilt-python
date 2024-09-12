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


class SourceFile(object):
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
        'file_hash': 'str',
        'detected_lang': 'str',
        'detected_lang_confidence': 'float',
        'category': 'str',
        'labels': 'list[str]',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'file_hash': 'file_hash',
        'detected_lang': 'detected_lang',
        'detected_lang_confidence': 'detected_lang_confidence',
        'category': 'category',
        'labels': 'labels',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, file_hash=None, detected_lang=None, detected_lang_confidence=None, category=None, labels=None, created_at=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """SourceFile - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._file_hash = None
        self._detected_lang = None
        self._detected_lang_confidence = None
        self._category = None
        self._labels = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if file_hash is not None:
            self.file_hash = file_hash
        if detected_lang is not None:
            self.detected_lang = detected_lang
        if detected_lang_confidence is not None:
            self.detected_lang_confidence = detected_lang_confidence
        if category is not None:
            self.category = category
        if labels is not None:
            self.labels = labels
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this SourceFile.  # noqa: E501

        A unique number identifying the SourceFile.  # noqa: E501

        :return: The id of this SourceFile.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SourceFile.

        A unique number identifying the SourceFile.  # noqa: E501

        :param id: The id of this SourceFile.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this SourceFile.  # noqa: E501

        The file name.  # noqa: E501

        :return: The name of this SourceFile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SourceFile.

        The file name.  # noqa: E501

        :param name: The name of this SourceFile.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def file_hash(self):
        """Gets the file_hash of this SourceFile.  # noqa: E501

        A unique hash value associated with the file. An MD5 hash of the file content will be used by default.  # noqa: E501

        :return: The file_hash of this SourceFile.  # noqa: E501
        :rtype: str
        """
        return self._file_hash

    @file_hash.setter
    def file_hash(self, file_hash):
        """Sets the file_hash of this SourceFile.

        A unique hash value associated with the file. An MD5 hash of the file content will be used by default.  # noqa: E501

        :param file_hash: The file_hash of this SourceFile.  # noqa: E501
        :type: str
        """

        self._file_hash = file_hash

    @property
    def detected_lang(self):
        """Gets the detected_lang of this SourceFile.  # noqa: E501

        Language associated with the file.  # noqa: E501

        :return: The detected_lang of this SourceFile.  # noqa: E501
        :rtype: str
        """
        return self._detected_lang

    @detected_lang.setter
    def detected_lang(self, detected_lang):
        """Sets the detected_lang of this SourceFile.

        Language associated with the file.  # noqa: E501

        :param detected_lang: The detected_lang of this SourceFile.  # noqa: E501
        :type: str
        """

        self._detected_lang = detected_lang

    @property
    def detected_lang_confidence(self):
        """Gets the detected_lang_confidence of this SourceFile.  # noqa: E501

        Confidence score for the language associated with the file.  # noqa: E501

        :return: The detected_lang_confidence of this SourceFile.  # noqa: E501
        :rtype: float
        """
        return self._detected_lang_confidence

    @detected_lang_confidence.setter
    def detected_lang_confidence(self, detected_lang_confidence):
        """Sets the detected_lang_confidence of this SourceFile.

        Confidence score for the language associated with the file.  # noqa: E501

        :param detected_lang_confidence: The detected_lang_confidence of this SourceFile.  # noqa: E501
        :type: float
        """

        self._detected_lang_confidence = detected_lang_confidence

    @property
    def category(self):
        """Gets the category of this SourceFile.  # noqa: E501

        The category of the file. The options are `REFERENCE`, or `API`. The default is API. Files with the `REFERENCE` category will be displayed as reference material.  # noqa: E501

        :return: The category of this SourceFile.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this SourceFile.

        The category of the file. The options are `REFERENCE`, or `API`. The default is API. Files with the `REFERENCE` category will be displayed as reference material.  # noqa: E501

        :param category: The category of this SourceFile.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def labels(self):
        """Gets the labels of this SourceFile.  # noqa: E501

        The list of labels associated with the file.  # noqa: E501

        :return: The labels of this SourceFile.  # noqa: E501
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this SourceFile.

        The list of labels associated with the file.  # noqa: E501

        :param labels: The labels of this SourceFile.  # noqa: E501
        :type: list[str]
        """

        self._labels = labels

    @property
    def created_at(self):
        """Gets the created_at of this SourceFile.  # noqa: E501

        Time at which the object was created.  # noqa: E501

        :return: The created_at of this SourceFile.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SourceFile.

        Time at which the object was created.  # noqa: E501

        :param created_at: The created_at of this SourceFile.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this SourceFile.  # noqa: E501

        Time at which the object was created.  # noqa: E501

        :return: The updated_at of this SourceFile.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this SourceFile.

        Time at which the object was created.  # noqa: E501

        :param updated_at: The updated_at of this SourceFile.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if not isinstance(other, SourceFile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SourceFile):
            return True

        return self.to_dict() != other.to_dict()
