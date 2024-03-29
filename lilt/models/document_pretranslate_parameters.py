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


class DocumentPretranslateParameters(object):
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
        'id': 'list[int]',
        'auto_accept': 'bool',
        'case_sensitive': 'bool',
        'attribute_to_creator': 'bool',
        'mode': 'str'
    }

    attribute_map = {
        'id': 'id',
        'auto_accept': 'auto_accept',
        'case_sensitive': 'case_sensitive',
        'attribute_to_creator': 'attribute_to_creator',
        'mode': 'mode'
    }

    def __init__(self, id=None, auto_accept=None, case_sensitive=None, attribute_to_creator=None, mode=None, local_vars_configuration=None):  # noqa: E501
        """DocumentPretranslateParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._auto_accept = None
        self._case_sensitive = None
        self._attribute_to_creator = None
        self._mode = None
        self.discriminator = None

        self.id = id
        if auto_accept is not None:
            self.auto_accept = auto_accept
        if case_sensitive is not None:
            self.case_sensitive = case_sensitive
        if attribute_to_creator is not None:
            self.attribute_to_creator = attribute_to_creator
        if mode is not None:
            self.mode = mode

    @property
    def id(self):
        """Gets the id of this DocumentPretranslateParameters.  # noqa: E501

        A list of unique Document identifiers.  # noqa: E501

        :return: The id of this DocumentPretranslateParameters.  # noqa: E501
        :rtype: list[int]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DocumentPretranslateParameters.

        A list of unique Document identifiers.  # noqa: E501

        :param id: The id of this DocumentPretranslateParameters.  # noqa: E501
        :type: list[int]
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def auto_accept(self):
        """Gets the auto_accept of this DocumentPretranslateParameters.  # noqa: E501

        Optional parameter for auto-accepting 100% TM hits.  # noqa: E501

        :return: The auto_accept of this DocumentPretranslateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._auto_accept

    @auto_accept.setter
    def auto_accept(self, auto_accept):
        """Sets the auto_accept of this DocumentPretranslateParameters.

        Optional parameter for auto-accepting 100% TM hits.  # noqa: E501

        :param auto_accept: The auto_accept of this DocumentPretranslateParameters.  # noqa: E501
        :type: bool
        """

        self._auto_accept = auto_accept

    @property
    def case_sensitive(self):
        """Gets the case_sensitive of this DocumentPretranslateParameters.  # noqa: E501

        Optional for using case matching against TM hits..  # noqa: E501

        :return: The case_sensitive of this DocumentPretranslateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._case_sensitive

    @case_sensitive.setter
    def case_sensitive(self, case_sensitive):
        """Sets the case_sensitive of this DocumentPretranslateParameters.

        Optional for using case matching against TM hits..  # noqa: E501

        :param case_sensitive: The case_sensitive of this DocumentPretranslateParameters.  # noqa: E501
        :type: bool
        """

        self._case_sensitive = case_sensitive

    @property
    def attribute_to_creator(self):
        """Gets the attribute_to_creator of this DocumentPretranslateParameters.  # noqa: E501

        Optional parameter for attributing translation authorship of exact matches to document creator.  # noqa: E501

        :return: The attribute_to_creator of this DocumentPretranslateParameters.  # noqa: E501
        :rtype: bool
        """
        return self._attribute_to_creator

    @attribute_to_creator.setter
    def attribute_to_creator(self, attribute_to_creator):
        """Sets the attribute_to_creator of this DocumentPretranslateParameters.

        Optional parameter for attributing translation authorship of exact matches to document creator.  # noqa: E501

        :param attribute_to_creator: The attribute_to_creator of this DocumentPretranslateParameters.  # noqa: E501
        :type: bool
        """

        self._attribute_to_creator = attribute_to_creator

    @property
    def mode(self):
        """Gets the mode of this DocumentPretranslateParameters.  # noqa: E501

        An optional parameter indicating how the document will be pretranslated.  The accepted values are `tm`, or `tm+mt`. Default is `tm`.   # noqa: E501

        :return: The mode of this DocumentPretranslateParameters.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this DocumentPretranslateParameters.

        An optional parameter indicating how the document will be pretranslated.  The accepted values are `tm`, or `tm+mt`. Default is `tm`.   # noqa: E501

        :param mode: The mode of this DocumentPretranslateParameters.  # noqa: E501
        :type: str
        """

        self._mode = mode

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
        if not isinstance(other, DocumentPretranslateParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DocumentPretranslateParameters):
            return True

        return self.to_dict() != other.to_dict()
