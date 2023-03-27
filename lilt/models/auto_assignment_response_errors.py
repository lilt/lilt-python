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


class AutoAssignmentResponseErrors(object):
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
        'error_type': 'str',
        'project_id': 'int',
        'document_id': 'int',
        'error': 'str'
    }

    attribute_map = {
        'error_type': 'errorType',
        'project_id': 'projectId',
        'document_id': 'documentId',
        'error': 'error'
    }

    def __init__(self, error_type=None, project_id=None, document_id=None, error=None, local_vars_configuration=None):  # noqa: E501
        """AutoAssignmentResponseErrors - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._error_type = None
        self._project_id = None
        self._document_id = None
        self._error = None
        self.discriminator = None

        self.error_type = error_type
        self.project_id = project_id
        self.document_id = document_id
        self.error = error

    @property
    def error_type(self):
        """Gets the error_type of this AutoAssignmentResponseErrors.  # noqa: E501


        :return: The error_type of this AutoAssignmentResponseErrors.  # noqa: E501
        :rtype: str
        """
        return self._error_type

    @error_type.setter
    def error_type(self, error_type):
        """Sets the error_type of this AutoAssignmentResponseErrors.


        :param error_type: The error_type of this AutoAssignmentResponseErrors.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and error_type is None:  # noqa: E501
            raise ValueError("Invalid value for `error_type`, must not be `None`")  # noqa: E501

        self._error_type = error_type

    @property
    def project_id(self):
        """Gets the project_id of this AutoAssignmentResponseErrors.  # noqa: E501


        :return: The project_id of this AutoAssignmentResponseErrors.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this AutoAssignmentResponseErrors.


        :param project_id: The project_id of this AutoAssignmentResponseErrors.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and project_id is None:  # noqa: E501
            raise ValueError("Invalid value for `project_id`, must not be `None`")  # noqa: E501

        self._project_id = project_id

    @property
    def document_id(self):
        """Gets the document_id of this AutoAssignmentResponseErrors.  # noqa: E501


        :return: The document_id of this AutoAssignmentResponseErrors.  # noqa: E501
        :rtype: int
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this AutoAssignmentResponseErrors.


        :param document_id: The document_id of this AutoAssignmentResponseErrors.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and document_id is None:  # noqa: E501
            raise ValueError("Invalid value for `document_id`, must not be `None`")  # noqa: E501

        self._document_id = document_id

    @property
    def error(self):
        """Gets the error of this AutoAssignmentResponseErrors.  # noqa: E501


        :return: The error of this AutoAssignmentResponseErrors.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this AutoAssignmentResponseErrors.


        :param error: The error of this AutoAssignmentResponseErrors.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and error is None:  # noqa: E501
            raise ValueError("Invalid value for `error`, must not be `None`")  # noqa: E501

        self._error = error

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
        if not isinstance(other, AutoAssignmentResponseErrors):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AutoAssignmentResponseErrors):
            return True

        return self.to_dict() != other.to_dict()
