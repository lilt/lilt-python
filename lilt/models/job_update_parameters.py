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


class JobUpdateParameters(object):
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
        'name': 'str',
        'due_date': 'int',
        'is_processing': 'str',
        'processing_error_msg': 'str'
    }

    attribute_map = {
        'name': 'name',
        'due_date': 'dueDate',
        'is_processing': 'isProcessing',
        'processing_error_msg': 'processingErrorMsg'
    }

    def __init__(self, name=None, due_date=None, is_processing=None, processing_error_msg=None, local_vars_configuration=None):  # noqa: E501
        """JobUpdateParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._due_date = None
        self._is_processing = None
        self._processing_error_msg = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if due_date is not None:
            self.due_date = due_date
        if is_processing is not None:
            self.is_processing = is_processing
        if processing_error_msg is not None:
            self.processing_error_msg = processing_error_msg

    @property
    def name(self):
        """Gets the name of this JobUpdateParameters.  # noqa: E501

        A name for the Job.  # noqa: E501

        :return: The name of this JobUpdateParameters.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobUpdateParameters.

        A name for the Job.  # noqa: E501

        :param name: The name of this JobUpdateParameters.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def due_date(self):
        """Gets the due_date of this JobUpdateParameters.  # noqa: E501

        An ISO string date.  # noqa: E501

        :return: The due_date of this JobUpdateParameters.  # noqa: E501
        :rtype: int
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this JobUpdateParameters.

        An ISO string date.  # noqa: E501

        :param due_date: The due_date of this JobUpdateParameters.  # noqa: E501
        :type: int
        """

        self._due_date = due_date

    @property
    def is_processing(self):
        """Gets the is_processing of this JobUpdateParameters.  # noqa: E501

        The processing status of the job. Provide one of the following integers to indicate the status.  Ok = 0 Started = 1 ExportError = -2   # noqa: E501

        :return: The is_processing of this JobUpdateParameters.  # noqa: E501
        :rtype: str
        """
        return self._is_processing

    @is_processing.setter
    def is_processing(self, is_processing):
        """Sets the is_processing of this JobUpdateParameters.

        The processing status of the job. Provide one of the following integers to indicate the status.  Ok = 0 Started = 1 ExportError = -2   # noqa: E501

        :param is_processing: The is_processing of this JobUpdateParameters.  # noqa: E501
        :type: str
        """
        allowed_values = ["0", "1", "-2"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and is_processing not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `is_processing` ({0}), must be one of {1}"  # noqa: E501
                .format(is_processing, allowed_values)
            )

        self._is_processing = is_processing

    @property
    def processing_error_msg(self):
        """Gets the processing_error_msg of this JobUpdateParameters.  # noqa: E501

        The processing error message.  # noqa: E501

        :return: The processing_error_msg of this JobUpdateParameters.  # noqa: E501
        :rtype: str
        """
        return self._processing_error_msg

    @processing_error_msg.setter
    def processing_error_msg(self, processing_error_msg):
        """Sets the processing_error_msg of this JobUpdateParameters.

        The processing error message.  # noqa: E501

        :param processing_error_msg: The processing_error_msg of this JobUpdateParameters.  # noqa: E501
        :type: str
        """

        self._processing_error_msg = processing_error_msg

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
        if not isinstance(other, JobUpdateParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JobUpdateParameters):
            return True

        return self.to_dict() != other.to_dict()
