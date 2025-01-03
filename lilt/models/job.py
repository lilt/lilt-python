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


class Job(object):
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
        'creation_status': 'str',
        'delivered_at': 'datetime',
        'status': 'str',
        'due': 'datetime',
        'id': 'int',
        'is_processing': 'int',
        'stats': 'JobStats'
    }

    attribute_map = {
        'name': 'name',
        'creation_status': 'creationStatus',
        'delivered_at': 'deliveredAt',
        'status': 'status',
        'due': 'due',
        'id': 'id',
        'is_processing': 'isProcessing',
        'stats': 'stats'
    }

    def __init__(self, name=None, creation_status=None, delivered_at=None, status=None, due=None, id=None, is_processing=None, stats=None, local_vars_configuration=None):  # noqa: E501
        """Job - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._creation_status = None
        self._delivered_at = None
        self._status = None
        self._due = None
        self._id = None
        self._is_processing = None
        self._stats = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if creation_status is not None:
            self.creation_status = creation_status
        if delivered_at is not None:
            self.delivered_at = delivered_at
        if status is not None:
            self.status = status
        if due is not None:
            self.due = due
        if id is not None:
            self.id = id
        if is_processing is not None:
            self.is_processing = is_processing
        if stats is not None:
            self.stats = stats

    @property
    def name(self):
        """Gets the name of this Job.  # noqa: E501

        A name for the job.  # noqa: E501

        :return: The name of this Job.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Job.

        A name for the job.  # noqa: E501

        :param name: The name of this Job.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def creation_status(self):
        """Gets the creation_status of this Job.  # noqa: E501

        Status of job creation process that includes PENDING, COMPLETE, and FAILED.  # noqa: E501

        :return: The creation_status of this Job.  # noqa: E501
        :rtype: str
        """
        return self._creation_status

    @creation_status.setter
    def creation_status(self, creation_status):
        """Sets the creation_status of this Job.

        Status of job creation process that includes PENDING, COMPLETE, and FAILED.  # noqa: E501

        :param creation_status: The creation_status of this Job.  # noqa: E501
        :type: str
        """

        self._creation_status = creation_status

    @property
    def delivered_at(self):
        """Gets the delivered_at of this Job.  # noqa: E501


        :return: The delivered_at of this Job.  # noqa: E501
        :rtype: datetime
        """
        return self._delivered_at

    @delivered_at.setter
    def delivered_at(self, delivered_at):
        """Sets the delivered_at of this Job.


        :param delivered_at: The delivered_at of this Job.  # noqa: E501
        :type: datetime
        """

        self._delivered_at = delivered_at

    @property
    def status(self):
        """Gets the status of this Job.  # noqa: E501

        Current status of job that includes archived, delivered, and active.  # noqa: E501

        :return: The status of this Job.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Job.

        Current status of job that includes archived, delivered, and active.  # noqa: E501

        :param status: The status of this Job.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def due(self):
        """Gets the due of this Job.  # noqa: E501

        An ISO string date.  # noqa: E501

        :return: The due of this Job.  # noqa: E501
        :rtype: datetime
        """
        return self._due

    @due.setter
    def due(self, due):
        """Sets the due of this Job.

        An ISO string date.  # noqa: E501

        :param due: The due of this Job.  # noqa: E501
        :type: datetime
        """

        self._due = due

    @property
    def id(self):
        """Gets the id of this Job.  # noqa: E501

        An id for the job.  # noqa: E501

        :return: The id of this Job.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Job.

        An id for the job.  # noqa: E501

        :param id: The id of this Job.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def is_processing(self):
        """Gets the is_processing of this Job.  # noqa: E501

        Values include `1` while in progress, `0` when idle and `-2` when processing failed.  # noqa: E501

        :return: The is_processing of this Job.  # noqa: E501
        :rtype: int
        """
        return self._is_processing

    @is_processing.setter
    def is_processing(self, is_processing):
        """Sets the is_processing of this Job.

        Values include `1` while in progress, `0` when idle and `-2` when processing failed.  # noqa: E501

        :param is_processing: The is_processing of this Job.  # noqa: E501
        :type: int
        """

        self._is_processing = is_processing

    @property
    def stats(self):
        """Gets the stats of this Job.  # noqa: E501


        :return: The stats of this Job.  # noqa: E501
        :rtype: JobStats
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this Job.


        :param stats: The stats of this Job.  # noqa: E501
        :type: JobStats
        """

        self._stats = stats

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
        if not isinstance(other, Job):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Job):
            return True

        return self.to_dict() != other.to_dict()
