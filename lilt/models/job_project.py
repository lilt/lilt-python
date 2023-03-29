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


class JobProject(object):
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
        'src_lang': 'str',
        'src_locale': 'str',
        'trg_lang': 'str',
        'trg_locale': 'str',
        'name': 'str',
        'due': 'str',
        'is_complete': 'bool',
        'is_archived': 'bool',
        'state': 'str',
        'num_source_tokens': 'int',
        'created_at': 'str',
        'updated_at': 'str',
        'is_deleted': 'bool',
        'memory_id': 'int',
        'workflow_status': 'str',
        'workflow_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'src_lang': 'srcLang',
        'src_locale': 'srcLocale',
        'trg_lang': 'trgLang',
        'trg_locale': 'trgLocale',
        'name': 'name',
        'due': 'due',
        'is_complete': 'isComplete',
        'is_archived': 'isArchived',
        'state': 'state',
        'num_source_tokens': 'numSourceTokens',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'is_deleted': 'isDeleted',
        'memory_id': 'memoryId',
        'workflow_status': 'workflowStatus',
        'workflow_name': 'workflowName'
    }

    def __init__(self, id=None, src_lang=None, src_locale=None, trg_lang=None, trg_locale=None, name=None, due=None, is_complete=None, is_archived=None, state=None, num_source_tokens=None, created_at=None, updated_at=None, is_deleted=None, memory_id=None, workflow_status=None, workflow_name=None, local_vars_configuration=None):  # noqa: E501
        """JobProject - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._src_lang = None
        self._src_locale = None
        self._trg_lang = None
        self._trg_locale = None
        self._name = None
        self._due = None
        self._is_complete = None
        self._is_archived = None
        self._state = None
        self._num_source_tokens = None
        self._created_at = None
        self._updated_at = None
        self._is_deleted = None
        self._memory_id = None
        self._workflow_status = None
        self._workflow_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if src_lang is not None:
            self.src_lang = src_lang
        if src_locale is not None:
            self.src_locale = src_locale
        if trg_lang is not None:
            self.trg_lang = trg_lang
        if trg_locale is not None:
            self.trg_locale = trg_locale
        if name is not None:
            self.name = name
        if due is not None:
            self.due = due
        if is_complete is not None:
            self.is_complete = is_complete
        if is_archived is not None:
            self.is_archived = is_archived
        if state is not None:
            self.state = state
        if num_source_tokens is not None:
            self.num_source_tokens = num_source_tokens
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if is_deleted is not None:
            self.is_deleted = is_deleted
        if memory_id is not None:
            self.memory_id = memory_id
        if workflow_status is not None:
            self.workflow_status = workflow_status
        if workflow_name is not None:
            self.workflow_name = workflow_name

    @property
    def id(self):
        """Gets the id of this JobProject.  # noqa: E501

        An id for the project.  # noqa: E501

        :return: The id of this JobProject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JobProject.

        An id for the project.  # noqa: E501

        :param id: The id of this JobProject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def src_lang(self):
        """Gets the src_lang of this JobProject.  # noqa: E501

        Source language, an ISO 639-1 language identifier.  # noqa: E501

        :return: The src_lang of this JobProject.  # noqa: E501
        :rtype: str
        """
        return self._src_lang

    @src_lang.setter
    def src_lang(self, src_lang):
        """Sets the src_lang of this JobProject.

        Source language, an ISO 639-1 language identifier.  # noqa: E501

        :param src_lang: The src_lang of this JobProject.  # noqa: E501
        :type: str
        """

        self._src_lang = src_lang

    @property
    def src_locale(self):
        """Gets the src_locale of this JobProject.  # noqa: E501

        A locale identifier, supported for source language.  # noqa: E501

        :return: The src_locale of this JobProject.  # noqa: E501
        :rtype: str
        """
        return self._src_locale

    @src_locale.setter
    def src_locale(self, src_locale):
        """Sets the src_locale of this JobProject.

        A locale identifier, supported for source language.  # noqa: E501

        :param src_locale: The src_locale of this JobProject.  # noqa: E501
        :type: str
        """

        self._src_locale = src_locale

    @property
    def trg_lang(self):
        """Gets the trg_lang of this JobProject.  # noqa: E501

        Target language, an ISO 639-1 language identifier.  # noqa: E501

        :return: The trg_lang of this JobProject.  # noqa: E501
        :rtype: str
        """
        return self._trg_lang

    @trg_lang.setter
    def trg_lang(self, trg_lang):
        """Sets the trg_lang of this JobProject.

        Target language, an ISO 639-1 language identifier.  # noqa: E501

        :param trg_lang: The trg_lang of this JobProject.  # noqa: E501
        :type: str
        """

        self._trg_lang = trg_lang

    @property
    def trg_locale(self):
        """Gets the trg_locale of this JobProject.  # noqa: E501

        A locale identifier, supported for target language.  # noqa: E501

        :return: The trg_locale of this JobProject.  # noqa: E501
        :rtype: str
        """
        return self._trg_locale

    @trg_locale.setter
    def trg_locale(self, trg_locale):
        """Sets the trg_locale of this JobProject.

        A locale identifier, supported for target language.  # noqa: E501

        :param trg_locale: The trg_locale of this JobProject.  # noqa: E501
        :type: str
        """

        self._trg_locale = trg_locale

    @property
    def name(self):
        """Gets the name of this JobProject.  # noqa: E501

        A name for the project.  # noqa: E501

        :return: The name of this JobProject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobProject.

        A name for the project.  # noqa: E501

        :param name: The name of this JobProject.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def due(self):
        """Gets the due of this JobProject.  # noqa: E501

        An ISO date.  # noqa: E501

        :return: The due of this JobProject.  # noqa: E501
        :rtype: str
        """
        return self._due

    @due.setter
    def due(self, due):
        """Sets the due of this JobProject.

        An ISO date.  # noqa: E501

        :param due: The due of this JobProject.  # noqa: E501
        :type: str
        """

        self._due = due

    @property
    def is_complete(self):
        """Gets the is_complete of this JobProject.  # noqa: E501

        A state that checks project was completed.  # noqa: E501

        :return: The is_complete of this JobProject.  # noqa: E501
        :rtype: bool
        """
        return self._is_complete

    @is_complete.setter
    def is_complete(self, is_complete):
        """Sets the is_complete of this JobProject.

        A state that checks project was completed.  # noqa: E501

        :param is_complete: The is_complete of this JobProject.  # noqa: E501
        :type: bool
        """

        self._is_complete = is_complete

    @property
    def is_archived(self):
        """Gets the is_archived of this JobProject.  # noqa: E501

        The archived state of the project.  # noqa: E501

        :return: The is_archived of this JobProject.  # noqa: E501
        :rtype: bool
        """
        return self._is_archived

    @is_archived.setter
    def is_archived(self, is_archived):
        """Sets the is_archived of this JobProject.

        The archived state of the project.  # noqa: E501

        :param is_archived: The is_archived of this JobProject.  # noqa: E501
        :type: bool
        """

        self._is_archived = is_archived

    @property
    def state(self):
        """Gets the state of this JobProject.  # noqa: E501

        Current state of the project. Example, backlog, inProgress, inReview, done.  # noqa: E501

        :return: The state of this JobProject.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this JobProject.

        Current state of the project. Example, backlog, inProgress, inReview, done.  # noqa: E501

        :param state: The state of this JobProject.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def num_source_tokens(self):
        """Gets the num_source_tokens of this JobProject.  # noqa: E501

        Total number of source tokens.  # noqa: E501

        :return: The num_source_tokens of this JobProject.  # noqa: E501
        :rtype: int
        """
        return self._num_source_tokens

    @num_source_tokens.setter
    def num_source_tokens(self, num_source_tokens):
        """Sets the num_source_tokens of this JobProject.

        Total number of source tokens.  # noqa: E501

        :param num_source_tokens: The num_source_tokens of this JobProject.  # noqa: E501
        :type: int
        """

        self._num_source_tokens = num_source_tokens

    @property
    def created_at(self):
        """Gets the created_at of this JobProject.  # noqa: E501

        Time at which the object was created.  # noqa: E501

        :return: The created_at of this JobProject.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this JobProject.

        Time at which the object was created.  # noqa: E501

        :param created_at: The created_at of this JobProject.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this JobProject.  # noqa: E501

        Time at which the object was updated.  # noqa: E501

        :return: The updated_at of this JobProject.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this JobProject.

        Time at which the object was updated.  # noqa: E501

        :param updated_at: The updated_at of this JobProject.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def is_deleted(self):
        """Gets the is_deleted of this JobProject.  # noqa: E501

        A state that checks project was deleted.  # noqa: E501

        :return: The is_deleted of this JobProject.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this JobProject.

        A state that checks project was deleted.  # noqa: E501

        :param is_deleted: The is_deleted of this JobProject.  # noqa: E501
        :type: bool
        """

        self._is_deleted = is_deleted

    @property
    def memory_id(self):
        """Gets the memory_id of this JobProject.  # noqa: E501

        A unique number identifying the associated Memory.  # noqa: E501

        :return: The memory_id of this JobProject.  # noqa: E501
        :rtype: int
        """
        return self._memory_id

    @memory_id.setter
    def memory_id(self, memory_id):
        """Sets the memory_id of this JobProject.

        A unique number identifying the associated Memory.  # noqa: E501

        :param memory_id: The memory_id of this JobProject.  # noqa: E501
        :type: int
        """

        self._memory_id = memory_id

    @property
    def workflow_status(self):
        """Gets the workflow_status of this JobProject.  # noqa: E501

        The status of the Workflow for the current project.  # noqa: E501

        :return: The workflow_status of this JobProject.  # noqa: E501
        :rtype: str
        """
        return self._workflow_status

    @workflow_status.setter
    def workflow_status(self, workflow_status):
        """Sets the workflow_status of this JobProject.

        The status of the Workflow for the current project.  # noqa: E501

        :param workflow_status: The workflow_status of this JobProject.  # noqa: E501
        :type: str
        """
        allowed_values = ["READY_TO_START", "IN_PROGRESS", "DONE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and workflow_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `workflow_status` ({0}), must be one of {1}"  # noqa: E501
                .format(workflow_status, allowed_values)
            )

        self._workflow_status = workflow_status

    @property
    def workflow_name(self):
        """Gets the workflow_name of this JobProject.  # noqa: E501

        Human readable name of the workflow associated with the current project.  # noqa: E501

        :return: The workflow_name of this JobProject.  # noqa: E501
        :rtype: str
        """
        return self._workflow_name

    @workflow_name.setter
    def workflow_name(self, workflow_name):
        """Sets the workflow_name of this JobProject.

        Human readable name of the workflow associated with the current project.  # noqa: E501

        :param workflow_name: The workflow_name of this JobProject.  # noqa: E501
        :type: str
        """

        self._workflow_name = workflow_name

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
        if not isinstance(other, JobProject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JobProject):
            return True

        return self.to_dict() != other.to_dict()
