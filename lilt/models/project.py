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


class Project(object):
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
        'memory_id': 'int',
        'srclang': 'str',
        'trglang': 'str',
        'srclocale': 'str',
        'trglocale': 'str',
        'name': 'str',
        'state': 'str',
        'due_date': 'int',
        'archived': 'bool',
        'metadata': 'object',
        'sample_review_percentage': 'int',
        'created_at': 'int',
        'updated_at': 'int',
        'document': 'list[DocumentWithoutSegments]'
    }

    attribute_map = {
        'id': 'id',
        'memory_id': 'memory_id',
        'srclang': 'srclang',
        'trglang': 'trglang',
        'srclocale': 'srclocale',
        'trglocale': 'trglocale',
        'name': 'name',
        'state': 'state',
        'due_date': 'due_date',
        'archived': 'archived',
        'metadata': 'metadata',
        'sample_review_percentage': 'sample_review_percentage',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'document': 'document'
    }

    def __init__(self, id=None, memory_id=None, srclang=None, trglang=None, srclocale=None, trglocale=None, name=None, state=None, due_date=None, archived=None, metadata=None, sample_review_percentage=None, created_at=None, updated_at=None, document=None, local_vars_configuration=None):  # noqa: E501
        """Project - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._memory_id = None
        self._srclang = None
        self._trglang = None
        self._srclocale = None
        self._trglocale = None
        self._name = None
        self._state = None
        self._due_date = None
        self._archived = None
        self._metadata = None
        self._sample_review_percentage = None
        self._created_at = None
        self._updated_at = None
        self._document = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if memory_id is not None:
            self.memory_id = memory_id
        if srclang is not None:
            self.srclang = srclang
        if trglang is not None:
            self.trglang = trglang
        if srclocale is not None:
            self.srclocale = srclocale
        if trglocale is not None:
            self.trglocale = trglocale
        if name is not None:
            self.name = name
        if state is not None:
            self.state = state
        if due_date is not None:
            self.due_date = due_date
        if archived is not None:
            self.archived = archived
        if metadata is not None:
            self.metadata = metadata
        if sample_review_percentage is not None:
            self.sample_review_percentage = sample_review_percentage
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if document is not None:
            self.document = document

    @property
    def id(self):
        """Gets the id of this Project.  # noqa: E501

        A unique number identifying the Project.  # noqa: E501

        :return: The id of this Project.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Project.

        A unique number identifying the Project.  # noqa: E501

        :param id: The id of this Project.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def memory_id(self):
        """Gets the memory_id of this Project.  # noqa: E501

        A unique number identifying the associated Memory.  # noqa: E501

        :return: The memory_id of this Project.  # noqa: E501
        :rtype: int
        """
        return self._memory_id

    @memory_id.setter
    def memory_id(self, memory_id):
        """Sets the memory_id of this Project.

        A unique number identifying the associated Memory.  # noqa: E501

        :param memory_id: The memory_id of this Project.  # noqa: E501
        :type: int
        """

        self._memory_id = memory_id

    @property
    def srclang(self):
        """Gets the srclang of this Project.  # noqa: E501

        An ISO 639-1 language identifier.  # noqa: E501

        :return: The srclang of this Project.  # noqa: E501
        :rtype: str
        """
        return self._srclang

    @srclang.setter
    def srclang(self, srclang):
        """Sets the srclang of this Project.

        An ISO 639-1 language identifier.  # noqa: E501

        :param srclang: The srclang of this Project.  # noqa: E501
        :type: str
        """

        self._srclang = srclang

    @property
    def trglang(self):
        """Gets the trglang of this Project.  # noqa: E501

        An ISO 639-1 language identifier.  # noqa: E501

        :return: The trglang of this Project.  # noqa: E501
        :rtype: str
        """
        return self._trglang

    @trglang.setter
    def trglang(self, trglang):
        """Sets the trglang of this Project.

        An ISO 639-1 language identifier.  # noqa: E501

        :param trglang: The trglang of this Project.  # noqa: E501
        :type: str
        """

        self._trglang = trglang

    @property
    def srclocale(self):
        """Gets the srclocale of this Project.  # noqa: E501

        A locale identifier, supported for srclang.  # noqa: E501

        :return: The srclocale of this Project.  # noqa: E501
        :rtype: str
        """
        return self._srclocale

    @srclocale.setter
    def srclocale(self, srclocale):
        """Sets the srclocale of this Project.

        A locale identifier, supported for srclang.  # noqa: E501

        :param srclocale: The srclocale of this Project.  # noqa: E501
        :type: str
        """

        self._srclocale = srclocale

    @property
    def trglocale(self):
        """Gets the trglocale of this Project.  # noqa: E501

        A locale identifier, supported for trglang.  # noqa: E501

        :return: The trglocale of this Project.  # noqa: E501
        :rtype: str
        """
        return self._trglocale

    @trglocale.setter
    def trglocale(self, trglocale):
        """Sets the trglocale of this Project.

        A locale identifier, supported for trglang.  # noqa: E501

        :param trglocale: The trglocale of this Project.  # noqa: E501
        :type: str
        """

        self._trglocale = trglocale

    @property
    def name(self):
        """Gets the name of this Project.  # noqa: E501

        A name for the project.  # noqa: E501

        :return: The name of this Project.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Project.

        A name for the project.  # noqa: E501

        :param name: The name of this Project.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def state(self):
        """Gets the state of this Project.  # noqa: E501

        The project's state. The possible states are 'backlog', 'inProgress', 'inReview', 'inQA', and 'done'  # noqa: E501

        :return: The state of this Project.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Project.

        The project's state. The possible states are 'backlog', 'inProgress', 'inReview', 'inQA', and 'done'  # noqa: E501

        :param state: The state of this Project.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def due_date(self):
        """Gets the due_date of this Project.  # noqa: E501

        The due date. Measured in seconds since the Unix epoch.  # noqa: E501

        :return: The due_date of this Project.  # noqa: E501
        :rtype: int
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this Project.

        The due date. Measured in seconds since the Unix epoch.  # noqa: E501

        :param due_date: The due_date of this Project.  # noqa: E501
        :type: int
        """

        self._due_date = due_date

    @property
    def archived(self):
        """Gets the archived of this Project.  # noqa: E501

        The archived state of the Project.  # noqa: E501

        :return: The archived of this Project.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this Project.

        The archived state of the Project.  # noqa: E501

        :param archived: The archived of this Project.  # noqa: E501
        :type: bool
        """

        self._archived = archived

    @property
    def metadata(self):
        """Gets the metadata of this Project.  # noqa: E501

        A JSON object for storing various project metadata.  # noqa: E501

        :return: The metadata of this Project.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Project.

        A JSON object for storing various project metadata.  # noqa: E501

        :param metadata: The metadata of this Project.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

    @property
    def sample_review_percentage(self):
        """Gets the sample_review_percentage of this Project.  # noqa: E501

        The project's sample review percentage.  # noqa: E501

        :return: The sample_review_percentage of this Project.  # noqa: E501
        :rtype: int
        """
        return self._sample_review_percentage

    @sample_review_percentage.setter
    def sample_review_percentage(self, sample_review_percentage):
        """Sets the sample_review_percentage of this Project.

        The project's sample review percentage.  # noqa: E501

        :param sample_review_percentage: The sample_review_percentage of this Project.  # noqa: E501
        :type: int
        """

        self._sample_review_percentage = sample_review_percentage

    @property
    def created_at(self):
        """Gets the created_at of this Project.  # noqa: E501

        Time at which the object was created. Measured in seconds since the Unix epoch.  # noqa: E501

        :return: The created_at of this Project.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Project.

        Time at which the object was created. Measured in seconds since the Unix epoch.  # noqa: E501

        :param created_at: The created_at of this Project.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Project.  # noqa: E501

        Time at which the object was created. Measured in seconds since the Unix epoch.  # noqa: E501

        :return: The updated_at of this Project.  # noqa: E501
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Project.

        Time at which the object was created. Measured in seconds since the Unix epoch.  # noqa: E501

        :param updated_at: The updated_at of this Project.  # noqa: E501
        :type: int
        """

        self._updated_at = updated_at

    @property
    def document(self):
        """Gets the document of this Project.  # noqa: E501

        A list of Documents.  # noqa: E501

        :return: The document of this Project.  # noqa: E501
        :rtype: list[DocumentWithoutSegments]
        """
        return self._document

    @document.setter
    def document(self, document):
        """Sets the document of this Project.

        A list of Documents.  # noqa: E501

        :param document: The document of this Project.  # noqa: E501
        :type: list[DocumentWithoutSegments]
        """

        self._document = document

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
        if not isinstance(other, Project):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Project):
            return True

        return self.to_dict() != other.to_dict()
