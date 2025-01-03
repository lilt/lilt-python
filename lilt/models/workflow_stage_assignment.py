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


class WorkflowStageAssignment(object):
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
        'workflow_stage_template_id': 'int',
        'user_id': 'int',
        'email': 'str'
    }

    attribute_map = {
        'workflow_stage_template_id': 'workflowStageTemplateId',
        'user_id': 'userId',
        'email': 'email'
    }

    def __init__(self, workflow_stage_template_id=None, user_id=None, email=None, local_vars_configuration=None):  # noqa: E501
        """WorkflowStageAssignment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._workflow_stage_template_id = None
        self._user_id = None
        self._email = None
        self.discriminator = None

        self.workflow_stage_template_id = workflow_stage_template_id
        if user_id is not None:
            self.user_id = user_id
        if email is not None:
            self.email = email

    @property
    def workflow_stage_template_id(self):
        """Gets the workflow_stage_template_id of this WorkflowStageAssignment.  # noqa: E501


        :return: The workflow_stage_template_id of this WorkflowStageAssignment.  # noqa: E501
        :rtype: int
        """
        return self._workflow_stage_template_id

    @workflow_stage_template_id.setter
    def workflow_stage_template_id(self, workflow_stage_template_id):
        """Sets the workflow_stage_template_id of this WorkflowStageAssignment.


        :param workflow_stage_template_id: The workflow_stage_template_id of this WorkflowStageAssignment.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and workflow_stage_template_id is None:  # noqa: E501
            raise ValueError("Invalid value for `workflow_stage_template_id`, must not be `None`")  # noqa: E501

        self._workflow_stage_template_id = workflow_stage_template_id

    @property
    def user_id(self):
        """Gets the user_id of this WorkflowStageAssignment.  # noqa: E501


        :return: The user_id of this WorkflowStageAssignment.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this WorkflowStageAssignment.


        :param user_id: The user_id of this WorkflowStageAssignment.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def email(self):
        """Gets the email of this WorkflowStageAssignment.  # noqa: E501


        :return: The email of this WorkflowStageAssignment.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this WorkflowStageAssignment.


        :param email: The email of this WorkflowStageAssignment.  # noqa: E501
        :type: str
        """

        self._email = email

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
        if not isinstance(other, WorkflowStageAssignment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkflowStageAssignment):
            return True

        return self.to_dict() != other.to_dict()
