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


class DocumentPretranslating(object):
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
        'id': 'float',
        'import_in_progress': 'bool',
        'import_succeeded': 'bool',
        'import_error_message': 'str',
        'is_processing': 'bool',
        'is_pretranslating': 'bool',
        'status': 'DocumentPretranslatingStatus'
    }

    attribute_map = {
        'id': 'id',
        'import_in_progress': 'import_in_progress',
        'import_succeeded': 'import_succeeded',
        'import_error_message': 'import_error_message',
        'is_processing': 'is_processing',
        'is_pretranslating': 'is_pretranslating',
        'status': 'status'
    }

    def __init__(self, id=None, import_in_progress=None, import_succeeded=None, import_error_message=None, is_processing=None, is_pretranslating=None, status=None, local_vars_configuration=None):  # noqa: E501
        """DocumentPretranslating - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._import_in_progress = None
        self._import_succeeded = None
        self._import_error_message = None
        self._is_processing = None
        self._is_pretranslating = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if import_in_progress is not None:
            self.import_in_progress = import_in_progress
        if import_succeeded is not None:
            self.import_succeeded = import_succeeded
        if import_error_message is not None:
            self.import_error_message = import_error_message
        if is_processing is not None:
            self.is_processing = is_processing
        if is_pretranslating is not None:
            self.is_pretranslating = is_pretranslating
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this DocumentPretranslating.  # noqa: E501

        A status object indicating the pretranslation status.  # noqa: E501

        :return: The id of this DocumentPretranslating.  # noqa: E501
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DocumentPretranslating.

        A status object indicating the pretranslation status.  # noqa: E501

        :param id: The id of this DocumentPretranslating.  # noqa: E501
        :type: float
        """

        self._id = id

    @property
    def import_in_progress(self):
        """Gets the import_in_progress of this DocumentPretranslating.  # noqa: E501

        Indicates that the document is being imported.  # noqa: E501

        :return: The import_in_progress of this DocumentPretranslating.  # noqa: E501
        :rtype: bool
        """
        return self._import_in_progress

    @import_in_progress.setter
    def import_in_progress(self, import_in_progress):
        """Sets the import_in_progress of this DocumentPretranslating.

        Indicates that the document is being imported.  # noqa: E501

        :param import_in_progress: The import_in_progress of this DocumentPretranslating.  # noqa: E501
        :type: bool
        """

        self._import_in_progress = import_in_progress

    @property
    def import_succeeded(self):
        """Gets the import_succeeded of this DocumentPretranslating.  # noqa: E501

        Indicates that the document was successfully imported.  # noqa: E501

        :return: The import_succeeded of this DocumentPretranslating.  # noqa: E501
        :rtype: bool
        """
        return self._import_succeeded

    @import_succeeded.setter
    def import_succeeded(self, import_succeeded):
        """Sets the import_succeeded of this DocumentPretranslating.

        Indicates that the document was successfully imported.  # noqa: E501

        :param import_succeeded: The import_succeeded of this DocumentPretranslating.  # noqa: E501
        :type: bool
        """

        self._import_succeeded = import_succeeded

    @property
    def import_error_message(self):
        """Gets the import_error_message of this DocumentPretranslating.  # noqa: E501

        Indicates there was an error importing the document.  # noqa: E501

        :return: The import_error_message of this DocumentPretranslating.  # noqa: E501
        :rtype: str
        """
        return self._import_error_message

    @import_error_message.setter
    def import_error_message(self, import_error_message):
        """Sets the import_error_message of this DocumentPretranslating.

        Indicates there was an error importing the document.  # noqa: E501

        :param import_error_message: The import_error_message of this DocumentPretranslating.  # noqa: E501
        :type: str
        """

        self._import_error_message = import_error_message

    @property
    def is_processing(self):
        """Gets the is_processing of this DocumentPretranslating.  # noqa: E501

        Indicates the document is being processed.  # noqa: E501

        :return: The is_processing of this DocumentPretranslating.  # noqa: E501
        :rtype: bool
        """
        return self._is_processing

    @is_processing.setter
    def is_processing(self, is_processing):
        """Sets the is_processing of this DocumentPretranslating.

        Indicates the document is being processed.  # noqa: E501

        :param is_processing: The is_processing of this DocumentPretranslating.  # noqa: E501
        :type: bool
        """

        self._is_processing = is_processing

    @property
    def is_pretranslating(self):
        """Gets the is_pretranslating of this DocumentPretranslating.  # noqa: E501

        Indicates the document is being pretranslated.  # noqa: E501

        :return: The is_pretranslating of this DocumentPretranslating.  # noqa: E501
        :rtype: bool
        """
        return self._is_pretranslating

    @is_pretranslating.setter
    def is_pretranslating(self, is_pretranslating):
        """Sets the is_pretranslating of this DocumentPretranslating.

        Indicates the document is being pretranslated.  # noqa: E501

        :param is_pretranslating: The is_pretranslating of this DocumentPretranslating.  # noqa: E501
        :type: bool
        """

        self._is_pretranslating = is_pretranslating

    @property
    def status(self):
        """Gets the status of this DocumentPretranslating.  # noqa: E501


        :return: The status of this DocumentPretranslating.  # noqa: E501
        :rtype: DocumentPretranslatingStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DocumentPretranslating.


        :param status: The status of this DocumentPretranslating.  # noqa: E501
        :type: DocumentPretranslatingStatus
        """

        self._status = status

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
        if not isinstance(other, DocumentPretranslating):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DocumentPretranslating):
            return True

        return self.to_dict() != other.to_dict()
