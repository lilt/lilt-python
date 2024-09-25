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


class JobStats(object):
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
        'exact_words': 'int',
        'fuzzy_words': 'int',
        'new_words': 'int',
        'num_delivered_projects': 'int',
        'num_language_pairs': 'int',
        'num_projects': 'int',
        'percent_reviewed': 'int',
        'percent_translated': 'int',
        'projects': 'list[JobProject]',
        'source_words': 'int',
        'unique_language_pairs': 'int',
        'unique_linguists': 'int',
        'workflow_status': 'str'
    }

    attribute_map = {
        'exact_words': 'exactWords',
        'fuzzy_words': 'fuzzyWords',
        'new_words': 'newWords',
        'num_delivered_projects': 'numDeliveredProjects',
        'num_language_pairs': 'numLanguagePairs',
        'num_projects': 'numProjects',
        'percent_reviewed': 'percentReviewed',
        'percent_translated': 'percentTranslated',
        'projects': 'projects',
        'source_words': 'sourceWords',
        'unique_language_pairs': 'uniqueLanguagePairs',
        'unique_linguists': 'uniqueLinguists',
        'workflow_status': 'workflowStatus'
    }

    def __init__(self, exact_words=None, fuzzy_words=None, new_words=None, num_delivered_projects=None, num_language_pairs=None, num_projects=None, percent_reviewed=None, percent_translated=None, projects=None, source_words=None, unique_language_pairs=None, unique_linguists=None, workflow_status=None, local_vars_configuration=None):  # noqa: E501
        """JobStats - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._exact_words = None
        self._fuzzy_words = None
        self._new_words = None
        self._num_delivered_projects = None
        self._num_language_pairs = None
        self._num_projects = None
        self._percent_reviewed = None
        self._percent_translated = None
        self._projects = None
        self._source_words = None
        self._unique_language_pairs = None
        self._unique_linguists = None
        self._workflow_status = None
        self.discriminator = None

        if exact_words is not None:
            self.exact_words = exact_words
        if fuzzy_words is not None:
            self.fuzzy_words = fuzzy_words
        if new_words is not None:
            self.new_words = new_words
        if num_delivered_projects is not None:
            self.num_delivered_projects = num_delivered_projects
        if num_language_pairs is not None:
            self.num_language_pairs = num_language_pairs
        if num_projects is not None:
            self.num_projects = num_projects
        if percent_reviewed is not None:
            self.percent_reviewed = percent_reviewed
        if percent_translated is not None:
            self.percent_translated = percent_translated
        if projects is not None:
            self.projects = projects
        if source_words is not None:
            self.source_words = source_words
        if unique_language_pairs is not None:
            self.unique_language_pairs = unique_language_pairs
        if unique_linguists is not None:
            self.unique_linguists = unique_linguists
        if workflow_status is not None:
            self.workflow_status = workflow_status

    @property
    def exact_words(self):
        """Gets the exact_words of this JobStats.  # noqa: E501

        Total number of exact words.  # noqa: E501

        :return: The exact_words of this JobStats.  # noqa: E501
        :rtype: int
        """
        return self._exact_words

    @exact_words.setter
    def exact_words(self, exact_words):
        """Sets the exact_words of this JobStats.

        Total number of exact words.  # noqa: E501

        :param exact_words: The exact_words of this JobStats.  # noqa: E501
        :type: int
        """

        self._exact_words = exact_words

    @property
    def fuzzy_words(self):
        """Gets the fuzzy_words of this JobStats.  # noqa: E501

        Total number of fuzzy words.  # noqa: E501

        :return: The fuzzy_words of this JobStats.  # noqa: E501
        :rtype: int
        """
        return self._fuzzy_words

    @fuzzy_words.setter
    def fuzzy_words(self, fuzzy_words):
        """Sets the fuzzy_words of this JobStats.

        Total number of fuzzy words.  # noqa: E501

        :param fuzzy_words: The fuzzy_words of this JobStats.  # noqa: E501
        :type: int
        """

        self._fuzzy_words = fuzzy_words

    @property
    def new_words(self):
        """Gets the new_words of this JobStats.  # noqa: E501

        Total number of fuzzy words.  # noqa: E501

        :return: The new_words of this JobStats.  # noqa: E501
        :rtype: int
        """
        return self._new_words

    @new_words.setter
    def new_words(self, new_words):
        """Sets the new_words of this JobStats.

        Total number of fuzzy words.  # noqa: E501

        :param new_words: The new_words of this JobStats.  # noqa: E501
        :type: int
        """

        self._new_words = new_words

    @property
    def num_delivered_projects(self):
        """Gets the num_delivered_projects of this JobStats.  # noqa: E501

        Total number of delivered projects.  # noqa: E501

        :return: The num_delivered_projects of this JobStats.  # noqa: E501
        :rtype: int
        """
        return self._num_delivered_projects

    @num_delivered_projects.setter
    def num_delivered_projects(self, num_delivered_projects):
        """Sets the num_delivered_projects of this JobStats.

        Total number of delivered projects.  # noqa: E501

        :param num_delivered_projects: The num_delivered_projects of this JobStats.  # noqa: E501
        :type: int
        """

        self._num_delivered_projects = num_delivered_projects

    @property
    def num_language_pairs(self):
        """Gets the num_language_pairs of this JobStats.  # noqa: E501

        Total number of delivered projects.  # noqa: E501

        :return: The num_language_pairs of this JobStats.  # noqa: E501
        :rtype: int
        """
        return self._num_language_pairs

    @num_language_pairs.setter
    def num_language_pairs(self, num_language_pairs):
        """Sets the num_language_pairs of this JobStats.

        Total number of delivered projects.  # noqa: E501

        :param num_language_pairs: The num_language_pairs of this JobStats.  # noqa: E501
        :type: int
        """

        self._num_language_pairs = num_language_pairs

    @property
    def num_projects(self):
        """Gets the num_projects of this JobStats.  # noqa: E501

        Total number of projects.  # noqa: E501

        :return: The num_projects of this JobStats.  # noqa: E501
        :rtype: int
        """
        return self._num_projects

    @num_projects.setter
    def num_projects(self, num_projects):
        """Sets the num_projects of this JobStats.

        Total number of projects.  # noqa: E501

        :param num_projects: The num_projects of this JobStats.  # noqa: E501
        :type: int
        """

        self._num_projects = num_projects

    @property
    def percent_reviewed(self):
        """Gets the percent_reviewed of this JobStats.  # noqa: E501

        Overall percentage of documents reviewed.  # noqa: E501

        :return: The percent_reviewed of this JobStats.  # noqa: E501
        :rtype: int
        """
        return self._percent_reviewed

    @percent_reviewed.setter
    def percent_reviewed(self, percent_reviewed):
        """Sets the percent_reviewed of this JobStats.

        Overall percentage of documents reviewed.  # noqa: E501

        :param percent_reviewed: The percent_reviewed of this JobStats.  # noqa: E501
        :type: int
        """

        self._percent_reviewed = percent_reviewed

    @property
    def percent_translated(self):
        """Gets the percent_translated of this JobStats.  # noqa: E501

        Overall percentage of documents translated.  # noqa: E501

        :return: The percent_translated of this JobStats.  # noqa: E501
        :rtype: int
        """
        return self._percent_translated

    @percent_translated.setter
    def percent_translated(self, percent_translated):
        """Sets the percent_translated of this JobStats.

        Overall percentage of documents translated.  # noqa: E501

        :param percent_translated: The percent_translated of this JobStats.  # noqa: E501
        :type: int
        """

        self._percent_translated = percent_translated

    @property
    def projects(self):
        """Gets the projects of this JobStats.  # noqa: E501


        :return: The projects of this JobStats.  # noqa: E501
        :rtype: list[JobProject]
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        """Sets the projects of this JobStats.


        :param projects: The projects of this JobStats.  # noqa: E501
        :type: list[JobProject]
        """

        self._projects = projects

    @property
    def source_words(self):
        """Gets the source_words of this JobStats.  # noqa: E501

        Total number of source words.  # noqa: E501

        :return: The source_words of this JobStats.  # noqa: E501
        :rtype: int
        """
        return self._source_words

    @source_words.setter
    def source_words(self, source_words):
        """Sets the source_words of this JobStats.

        Total number of source words.  # noqa: E501

        :param source_words: The source_words of this JobStats.  # noqa: E501
        :type: int
        """

        self._source_words = source_words

    @property
    def unique_language_pairs(self):
        """Gets the unique_language_pairs of this JobStats.  # noqa: E501

        Number of unique language pairs.  # noqa: E501

        :return: The unique_language_pairs of this JobStats.  # noqa: E501
        :rtype: int
        """
        return self._unique_language_pairs

    @unique_language_pairs.setter
    def unique_language_pairs(self, unique_language_pairs):
        """Sets the unique_language_pairs of this JobStats.

        Number of unique language pairs.  # noqa: E501

        :param unique_language_pairs: The unique_language_pairs of this JobStats.  # noqa: E501
        :type: int
        """

        self._unique_language_pairs = unique_language_pairs

    @property
    def unique_linguists(self):
        """Gets the unique_linguists of this JobStats.  # noqa: E501

        Number of unique linguists.  # noqa: E501

        :return: The unique_linguists of this JobStats.  # noqa: E501
        :rtype: int
        """
        return self._unique_linguists

    @unique_linguists.setter
    def unique_linguists(self, unique_linguists):
        """Sets the unique_linguists of this JobStats.

        Number of unique linguists.  # noqa: E501

        :param unique_linguists: The unique_linguists of this JobStats.  # noqa: E501
        :type: int
        """

        self._unique_linguists = unique_linguists

    @property
    def workflow_status(self):
        """Gets the workflow_status of this JobStats.  # noqa: E501

        The status of the Workflow for the current job.  # noqa: E501

        :return: The workflow_status of this JobStats.  # noqa: E501
        :rtype: str
        """
        return self._workflow_status

    @workflow_status.setter
    def workflow_status(self, workflow_status):
        """Sets the workflow_status of this JobStats.

        The status of the Workflow for the current job.  # noqa: E501

        :param workflow_status: The workflow_status of this JobStats.  # noqa: E501
        :type: str
        """
        allowed_values = ["READY_TO_START", "IN_PROGRESS", "DONE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and workflow_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `workflow_status` ({0}), must be one of {1}"  # noqa: E501
                .format(workflow_status, allowed_values)
            )

        self._workflow_status = workflow_status

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
        if not isinstance(other, JobStats):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JobStats):
            return True

        return self.to_dict() != other.to_dict()
