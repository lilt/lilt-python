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


class ProjectCreateParameters(object):
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
        'memory_id': 'int',
        'job_id': 'int',
        'due_date': 'int',
        'metadata': 'object',
        'workflow_template_id': 'int'
    }

    attribute_map = {
        'name': 'name',
        'memory_id': 'memory_id',
        'job_id': 'job_id',
        'due_date': 'due_date',
        'metadata': 'metadata',
        'workflow_template_id': 'workflowTemplateId'
    }

    def __init__(self, name=None, memory_id=None, job_id=None, due_date=None, metadata=None, workflow_template_id=None, local_vars_configuration=None):  # noqa: E501
        """ProjectCreateParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._memory_id = None
        self._job_id = None
        self._due_date = None
        self._metadata = None
        self._workflow_template_id = None
        self.discriminator = None

        self.name = name
        self.memory_id = memory_id
        if job_id is not None:
            self.job_id = job_id
        if due_date is not None:
            self.due_date = due_date
        if metadata is not None:
            self.metadata = metadata
        if workflow_template_id is not None:
            self.workflow_template_id = workflow_template_id

    @property
    def name(self):
        """Gets the name of this ProjectCreateParameters.  # noqa: E501

        A name for the Project.  # noqa: E501

        :return: The name of this ProjectCreateParameters.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectCreateParameters.

        A name for the Project.  # noqa: E501

        :param name: The name of this ProjectCreateParameters.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def memory_id(self):
        """Gets the memory_id of this ProjectCreateParameters.  # noqa: E501

        The Memory to associate with this new Project.  # noqa: E501

        :return: The memory_id of this ProjectCreateParameters.  # noqa: E501
        :rtype: int
        """
        return self._memory_id

    @memory_id.setter
    def memory_id(self, memory_id):
        """Sets the memory_id of this ProjectCreateParameters.

        The Memory to associate with this new Project.  # noqa: E501

        :param memory_id: The memory_id of this ProjectCreateParameters.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and memory_id is None:  # noqa: E501
            raise ValueError("Invalid value for `memory_id`, must not be `None`")  # noqa: E501

        self._memory_id = memory_id

    @property
    def job_id(self):
        """Gets the job_id of this ProjectCreateParameters.  # noqa: E501

        The Job to associate with this new Project. If a Job ID is not provided then a new Job will be created to contain the Project.   # noqa: E501

        :return: The job_id of this ProjectCreateParameters.  # noqa: E501
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ProjectCreateParameters.

        The Job to associate with this new Project. If a Job ID is not provided then a new Job will be created to contain the Project.   # noqa: E501

        :param job_id: The job_id of this ProjectCreateParameters.  # noqa: E501
        :type: int
        """

        self._job_id = job_id

    @property
    def due_date(self):
        """Gets the due_date of this ProjectCreateParameters.  # noqa: E501

        The due date. Measured in seconds since the Unix epoch.  # noqa: E501

        :return: The due_date of this ProjectCreateParameters.  # noqa: E501
        :rtype: int
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this ProjectCreateParameters.

        The due date. Measured in seconds since the Unix epoch.  # noqa: E501

        :param due_date: The due_date of this ProjectCreateParameters.  # noqa: E501
        :type: int
        """

        self._due_date = due_date

    @property
    def metadata(self):
        """Gets the metadata of this ProjectCreateParameters.  # noqa: E501

        A JSON object of key/value string pairs. Stores custom project information.  # noqa: E501

        :return: The metadata of this ProjectCreateParameters.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ProjectCreateParameters.

        A JSON object of key/value string pairs. Stores custom project information.  # noqa: E501

        :param metadata: The metadata of this ProjectCreateParameters.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

    @property
    def workflow_template_id(self):
        """Gets the workflow_template_id of this ProjectCreateParameters.  # noqa: E501

        The workflow template used to create this project. WorkflowTemplateIds can be retrieved via the /workflows/templates endpoint. If not specified then the organization default workflowTemplateId will be used.  # noqa: E501

        :return: The workflow_template_id of this ProjectCreateParameters.  # noqa: E501
        :rtype: int
        """
        return self._workflow_template_id

    @workflow_template_id.setter
    def workflow_template_id(self, workflow_template_id):
        """Sets the workflow_template_id of this ProjectCreateParameters.

        The workflow template used to create this project. WorkflowTemplateIds can be retrieved via the /workflows/templates endpoint. If not specified then the organization default workflowTemplateId will be used.  # noqa: E501

        :param workflow_template_id: The workflow_template_id of this ProjectCreateParameters.  # noqa: E501
        :type: int
        """

        self._workflow_template_id = workflow_template_id

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
        if not isinstance(other, ProjectCreateParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectCreateParameters):
            return True

        return self.to_dict() != other.to_dict()
