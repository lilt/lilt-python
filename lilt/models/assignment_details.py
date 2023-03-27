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


class AssignmentDetails(object):
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
        'is_preferred_translator': 'bool',
        'words_left_averaged_translator': 'int',
        'words_left_averaged_reviewer': 'int',
        'assignment_errors': 'list[str]',
        'doc_id': 'int',
        'project_id': 'int',
        'is_auto_assigned': 'bool',
        'translator_user_id': 'int',
        'translator_role_id': 'int',
        'translator_due_date': 'str',
        'reviewer_user_id': 'int'
    }

    attribute_map = {
        'is_preferred_translator': 'isPreferredTranslator',
        'words_left_averaged_translator': 'wordsLeftAveragedTranslator',
        'words_left_averaged_reviewer': 'wordsLeftAveragedReviewer',
        'assignment_errors': 'assignmentErrors',
        'doc_id': 'docId',
        'project_id': 'projectId',
        'is_auto_assigned': 'isAutoAssigned',
        'translator_user_id': 'translatorUserId',
        'translator_role_id': 'translatorRoleId',
        'translator_due_date': 'translatorDueDate',
        'reviewer_user_id': 'reviewerUserId'
    }

    def __init__(self, is_preferred_translator=None, words_left_averaged_translator=None, words_left_averaged_reviewer=None, assignment_errors=None, doc_id=None, project_id=None, is_auto_assigned=None, translator_user_id=None, translator_role_id=None, translator_due_date=None, reviewer_user_id=None, local_vars_configuration=None):  # noqa: E501
        """AssignmentDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._is_preferred_translator = None
        self._words_left_averaged_translator = None
        self._words_left_averaged_reviewer = None
        self._assignment_errors = None
        self._doc_id = None
        self._project_id = None
        self._is_auto_assigned = None
        self._translator_user_id = None
        self._translator_role_id = None
        self._translator_due_date = None
        self._reviewer_user_id = None
        self.discriminator = None

        if is_preferred_translator is not None:
            self.is_preferred_translator = is_preferred_translator
        if words_left_averaged_translator is not None:
            self.words_left_averaged_translator = words_left_averaged_translator
        if words_left_averaged_reviewer is not None:
            self.words_left_averaged_reviewer = words_left_averaged_reviewer
        if assignment_errors is not None:
            self.assignment_errors = assignment_errors
        if doc_id is not None:
            self.doc_id = doc_id
        if project_id is not None:
            self.project_id = project_id
        if is_auto_assigned is not None:
            self.is_auto_assigned = is_auto_assigned
        if translator_user_id is not None:
            self.translator_user_id = translator_user_id
        if translator_role_id is not None:
            self.translator_role_id = translator_role_id
        if translator_due_date is not None:
            self.translator_due_date = translator_due_date
        if reviewer_user_id is not None:
            self.reviewer_user_id = reviewer_user_id

    @property
    def is_preferred_translator(self):
        """Gets the is_preferred_translator of this AssignmentDetails.  # noqa: E501


        :return: The is_preferred_translator of this AssignmentDetails.  # noqa: E501
        :rtype: bool
        """
        return self._is_preferred_translator

    @is_preferred_translator.setter
    def is_preferred_translator(self, is_preferred_translator):
        """Sets the is_preferred_translator of this AssignmentDetails.


        :param is_preferred_translator: The is_preferred_translator of this AssignmentDetails.  # noqa: E501
        :type: bool
        """

        self._is_preferred_translator = is_preferred_translator

    @property
    def words_left_averaged_translator(self):
        """Gets the words_left_averaged_translator of this AssignmentDetails.  # noqa: E501


        :return: The words_left_averaged_translator of this AssignmentDetails.  # noqa: E501
        :rtype: int
        """
        return self._words_left_averaged_translator

    @words_left_averaged_translator.setter
    def words_left_averaged_translator(self, words_left_averaged_translator):
        """Sets the words_left_averaged_translator of this AssignmentDetails.


        :param words_left_averaged_translator: The words_left_averaged_translator of this AssignmentDetails.  # noqa: E501
        :type: int
        """

        self._words_left_averaged_translator = words_left_averaged_translator

    @property
    def words_left_averaged_reviewer(self):
        """Gets the words_left_averaged_reviewer of this AssignmentDetails.  # noqa: E501


        :return: The words_left_averaged_reviewer of this AssignmentDetails.  # noqa: E501
        :rtype: int
        """
        return self._words_left_averaged_reviewer

    @words_left_averaged_reviewer.setter
    def words_left_averaged_reviewer(self, words_left_averaged_reviewer):
        """Sets the words_left_averaged_reviewer of this AssignmentDetails.


        :param words_left_averaged_reviewer: The words_left_averaged_reviewer of this AssignmentDetails.  # noqa: E501
        :type: int
        """

        self._words_left_averaged_reviewer = words_left_averaged_reviewer

    @property
    def assignment_errors(self):
        """Gets the assignment_errors of this AssignmentDetails.  # noqa: E501


        :return: The assignment_errors of this AssignmentDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._assignment_errors

    @assignment_errors.setter
    def assignment_errors(self, assignment_errors):
        """Sets the assignment_errors of this AssignmentDetails.


        :param assignment_errors: The assignment_errors of this AssignmentDetails.  # noqa: E501
        :type: list[str]
        """

        self._assignment_errors = assignment_errors

    @property
    def doc_id(self):
        """Gets the doc_id of this AssignmentDetails.  # noqa: E501


        :return: The doc_id of this AssignmentDetails.  # noqa: E501
        :rtype: int
        """
        return self._doc_id

    @doc_id.setter
    def doc_id(self, doc_id):
        """Sets the doc_id of this AssignmentDetails.


        :param doc_id: The doc_id of this AssignmentDetails.  # noqa: E501
        :type: int
        """

        self._doc_id = doc_id

    @property
    def project_id(self):
        """Gets the project_id of this AssignmentDetails.  # noqa: E501


        :return: The project_id of this AssignmentDetails.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this AssignmentDetails.


        :param project_id: The project_id of this AssignmentDetails.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def is_auto_assigned(self):
        """Gets the is_auto_assigned of this AssignmentDetails.  # noqa: E501


        :return: The is_auto_assigned of this AssignmentDetails.  # noqa: E501
        :rtype: bool
        """
        return self._is_auto_assigned

    @is_auto_assigned.setter
    def is_auto_assigned(self, is_auto_assigned):
        """Sets the is_auto_assigned of this AssignmentDetails.


        :param is_auto_assigned: The is_auto_assigned of this AssignmentDetails.  # noqa: E501
        :type: bool
        """

        self._is_auto_assigned = is_auto_assigned

    @property
    def translator_user_id(self):
        """Gets the translator_user_id of this AssignmentDetails.  # noqa: E501


        :return: The translator_user_id of this AssignmentDetails.  # noqa: E501
        :rtype: int
        """
        return self._translator_user_id

    @translator_user_id.setter
    def translator_user_id(self, translator_user_id):
        """Sets the translator_user_id of this AssignmentDetails.


        :param translator_user_id: The translator_user_id of this AssignmentDetails.  # noqa: E501
        :type: int
        """

        self._translator_user_id = translator_user_id

    @property
    def translator_role_id(self):
        """Gets the translator_role_id of this AssignmentDetails.  # noqa: E501


        :return: The translator_role_id of this AssignmentDetails.  # noqa: E501
        :rtype: int
        """
        return self._translator_role_id

    @translator_role_id.setter
    def translator_role_id(self, translator_role_id):
        """Sets the translator_role_id of this AssignmentDetails.


        :param translator_role_id: The translator_role_id of this AssignmentDetails.  # noqa: E501
        :type: int
        """

        self._translator_role_id = translator_role_id

    @property
    def translator_due_date(self):
        """Gets the translator_due_date of this AssignmentDetails.  # noqa: E501


        :return: The translator_due_date of this AssignmentDetails.  # noqa: E501
        :rtype: str
        """
        return self._translator_due_date

    @translator_due_date.setter
    def translator_due_date(self, translator_due_date):
        """Sets the translator_due_date of this AssignmentDetails.


        :param translator_due_date: The translator_due_date of this AssignmentDetails.  # noqa: E501
        :type: str
        """

        self._translator_due_date = translator_due_date

    @property
    def reviewer_user_id(self):
        """Gets the reviewer_user_id of this AssignmentDetails.  # noqa: E501


        :return: The reviewer_user_id of this AssignmentDetails.  # noqa: E501
        :rtype: int
        """
        return self._reviewer_user_id

    @reviewer_user_id.setter
    def reviewer_user_id(self, reviewer_user_id):
        """Sets the reviewer_user_id of this AssignmentDetails.


        :param reviewer_user_id: The reviewer_user_id of this AssignmentDetails.  # noqa: E501
        :type: int
        """

        self._reviewer_user_id = reviewer_user_id

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
        if not isinstance(other, AssignmentDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssignmentDetails):
            return True

        return self.to_dict() != other.to_dict()
