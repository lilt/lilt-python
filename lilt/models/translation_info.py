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


class TranslationInfo(object):
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
        'file_id': 'int',
        'status': 'str',
        'created_at': 'int',
        'error_msg': 'str'
    }

    attribute_map = {
        'id': 'id',
        'file_id': 'fileId',
        'status': 'status',
        'created_at': 'createdAt',
        'error_msg': 'errorMsg'
    }

    def __init__(self, id=None, file_id=None, status=None, created_at=None, error_msg=None, local_vars_configuration=None):  # noqa: E501
        """TranslationInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._file_id = None
        self._status = None
        self._created_at = None
        self._error_msg = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if file_id is not None:
            self.file_id = file_id
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def id(self):
        """Gets the id of this TranslationInfo.  # noqa: E501

        Unique identifier for this translation.  # noqa: E501

        :return: The id of this TranslationInfo.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TranslationInfo.

        Unique identifier for this translation.  # noqa: E501

        :param id: The id of this TranslationInfo.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def file_id(self):
        """Gets the file_id of this TranslationInfo.  # noqa: E501

        id of the File that is being translated.  # noqa: E501

        :return: The file_id of this TranslationInfo.  # noqa: E501
        :rtype: int
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this TranslationInfo.

        id of the File that is being translated.  # noqa: E501

        :param file_id: The file_id of this TranslationInfo.  # noqa: E501
        :type: int
        """

        self._file_id = file_id

    @property
    def status(self):
        """Gets the status of this TranslationInfo.  # noqa: E501

        Status of the translation - `InProgress`, `ReadyForDownload`, `Completed`, `Failed`.  # noqa: E501

        :return: The status of this TranslationInfo.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TranslationInfo.

        Status of the translation - `InProgress`, `ReadyForDownload`, `Completed`, `Failed`.  # noqa: E501

        :param status: The status of this TranslationInfo.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this TranslationInfo.  # noqa: E501

        Time when this translation was started, in seconds since the Unix epoch.  # noqa: E501

        :return: The created_at of this TranslationInfo.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TranslationInfo.

        Time when this translation was started, in seconds since the Unix epoch.  # noqa: E501

        :param created_at: The created_at of this TranslationInfo.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def error_msg(self):
        """Gets the error_msg of this TranslationInfo.  # noqa: E501

        Error message, present when status is `Failed`.  # noqa: E501

        :return: The error_msg of this TranslationInfo.  # noqa: E501
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this TranslationInfo.

        Error message, present when status is `Failed`.  # noqa: E501

        :param error_msg: The error_msg of this TranslationInfo.  # noqa: E501
        :type: str
        """

        self._error_msg = error_msg

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
        if not isinstance(other, TranslationInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TranslationInfo):
            return True

        return self.to_dict() != other.to_dict()
