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


class File(object):
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
        'export_uri': 'str',
        'created_at': 'int',
        'updated_at': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'file_hash': 'file_hash',
        'export_uri': 'export_uri',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, file_hash=None, export_uri=None, created_at=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """File - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._file_hash = None
        self._export_uri = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if file_hash is not None:
            self.file_hash = file_hash
        if export_uri is not None:
            self.export_uri = export_uri
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this File.  # noqa: E501

        A unique number identifying the File.  # noqa: E501

        :return: The id of this File.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this File.

        A unique number identifying the File.  # noqa: E501

        :param id: The id of this File.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this File.  # noqa: E501

        The file name.  # noqa: E501

        :return: The name of this File.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this File.

        The file name.  # noqa: E501

        :param name: The name of this File.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def file_hash(self):
        """Gets the file_hash of this File.  # noqa: E501

        A unique hash value associated with the file. An MD5 hash of the file content will be used by default.  # noqa: E501

        :return: The file_hash of this File.  # noqa: E501
        :rtype: str
        """
        return self._file_hash

    @file_hash.setter
    def file_hash(self, file_hash):
        """Sets the file_hash of this File.

        A unique hash value associated with the file. An MD5 hash of the file content will be used by default.  # noqa: E501

        :param file_hash: The file_hash of this File.  # noqa: E501
        :type: str
        """

        self._file_hash = file_hash

    @property
    def export_uri(self):
        """Gets the export_uri of this File.  # noqa: E501

        A webhook endpoint that will export the translated document back to the source repository.  # noqa: E501

        :return: The export_uri of this File.  # noqa: E501
        :rtype: str
        """
        return self._export_uri

    @export_uri.setter
    def export_uri(self, export_uri):
        """Sets the export_uri of this File.

        A webhook endpoint that will export the translated document back to the source repository.  # noqa: E501

        :param export_uri: The export_uri of this File.  # noqa: E501
        :type: str
        """

        self._export_uri = export_uri

    @property
    def created_at(self):
        """Gets the created_at of this File.  # noqa: E501

        Time at which the object was created. Measured in seconds since the Unix epoch.  # noqa: E501

        :return: The created_at of this File.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this File.

        Time at which the object was created. Measured in seconds since the Unix epoch.  # noqa: E501

        :param created_at: The created_at of this File.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this File.  # noqa: E501

        Time at which the object was created. Measured in seconds since the Unix epoch.  # noqa: E501

        :return: The updated_at of this File.  # noqa: E501
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this File.

        Time at which the object was created. Measured in seconds since the Unix epoch.  # noqa: E501

        :param updated_at: The updated_at of this File.  # noqa: E501
        :type: int
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
        if not isinstance(other, File):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, File):
            return True

        return self.to_dict() != other.to_dict()
