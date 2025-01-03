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


class TranslateSegmentBody(object):
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
        'source': 'str',
        'memory_id': 'int',
        'source_hash': 'int',
        'n': 'int',
        'prefix': 'str',
        'rich': 'bool',
        'tm_matches': 'bool',
        'project_tags': 'bool',
        'contains_icu_data': 'bool'
    }

    attribute_map = {
        'source': 'source',
        'memory_id': 'memory_id',
        'source_hash': 'source_hash',
        'n': 'n',
        'prefix': 'prefix',
        'rich': 'rich',
        'tm_matches': 'tm_matches',
        'project_tags': 'project_tags',
        'contains_icu_data': 'containsICUData'
    }

    def __init__(self, source=None, memory_id=None, source_hash=None, n=None, prefix=None, rich=False, tm_matches=True, project_tags=False, contains_icu_data=False, local_vars_configuration=None):  # noqa: E501
        """TranslateSegmentBody - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._source = None
        self._memory_id = None
        self._source_hash = None
        self._n = None
        self._prefix = None
        self._rich = None
        self._tm_matches = None
        self._project_tags = None
        self._contains_icu_data = None
        self.discriminator = None

        if source is not None:
            self.source = source
        self.memory_id = memory_id
        if source_hash is not None:
            self.source_hash = source_hash
        if n is not None:
            self.n = n
        if prefix is not None:
            self.prefix = prefix
        if rich is not None:
            self.rich = rich
        if tm_matches is not None:
            self.tm_matches = tm_matches
        if project_tags is not None:
            self.project_tags = project_tags
        if contains_icu_data is not None:
            self.contains_icu_data = contains_icu_data

    @property
    def source(self):
        """Gets the source of this TranslateSegmentBody.  # noqa: E501

        A unique Segment identifier.  # noqa: E501

        :return: The source of this TranslateSegmentBody.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this TranslateSegmentBody.

        A unique Segment identifier.  # noqa: E501

        :param source: The source of this TranslateSegmentBody.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def memory_id(self):
        """Gets the memory_id of this TranslateSegmentBody.  # noqa: E501

        A unique Memory identifier.  # noqa: E501

        :return: The memory_id of this TranslateSegmentBody.  # noqa: E501
        :rtype: int
        """
        return self._memory_id

    @memory_id.setter
    def memory_id(self, memory_id):
        """Sets the memory_id of this TranslateSegmentBody.

        A unique Memory identifier.  # noqa: E501

        :param memory_id: The memory_id of this TranslateSegmentBody.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and memory_id is None:  # noqa: E501
            raise ValueError("Invalid value for `memory_id`, must not be `None`")  # noqa: E501

        self._memory_id = memory_id

    @property
    def source_hash(self):
        """Gets the source_hash of this TranslateSegmentBody.  # noqa: E501

        A source hash code.  # noqa: E501

        :return: The source_hash of this TranslateSegmentBody.  # noqa: E501
        :rtype: int
        """
        return self._source_hash

    @source_hash.setter
    def source_hash(self, source_hash):
        """Sets the source_hash of this TranslateSegmentBody.

        A source hash code.  # noqa: E501

        :param source_hash: The source_hash of this TranslateSegmentBody.  # noqa: E501
        :type: int
        """

        self._source_hash = source_hash

    @property
    def n(self):
        """Gets the n of this TranslateSegmentBody.  # noqa: E501

        Return top n translations (deprecated).  # noqa: E501

        :return: The n of this TranslateSegmentBody.  # noqa: E501
        :rtype: int
        """
        return self._n

    @n.setter
    def n(self, n):
        """Sets the n of this TranslateSegmentBody.

        Return top n translations (deprecated).  # noqa: E501

        :param n: The n of this TranslateSegmentBody.  # noqa: E501
        :type: int
        """

        self._n = n

    @property
    def prefix(self):
        """Gets the prefix of this TranslateSegmentBody.  # noqa: E501

        A target prefix  # noqa: E501

        :return: The prefix of this TranslateSegmentBody.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this TranslateSegmentBody.

        A target prefix  # noqa: E501

        :param prefix: The prefix of this TranslateSegmentBody.  # noqa: E501
        :type: str
        """

        self._prefix = prefix

    @property
    def rich(self):
        """Gets the rich of this TranslateSegmentBody.  # noqa: E501

        Returns rich translation information (e.g., with word alignments).  # noqa: E501

        :return: The rich of this TranslateSegmentBody.  # noqa: E501
        :rtype: bool
        """
        return self._rich

    @rich.setter
    def rich(self, rich):
        """Sets the rich of this TranslateSegmentBody.

        Returns rich translation information (e.g., with word alignments).  # noqa: E501

        :param rich: The rich of this TranslateSegmentBody.  # noqa: E501
        :type: bool
        """

        self._rich = rich

    @property
    def tm_matches(self):
        """Gets the tm_matches of this TranslateSegmentBody.  # noqa: E501

        Include translation memory fuzzy matches.  # noqa: E501

        :return: The tm_matches of this TranslateSegmentBody.  # noqa: E501
        :rtype: bool
        """
        return self._tm_matches

    @tm_matches.setter
    def tm_matches(self, tm_matches):
        """Sets the tm_matches of this TranslateSegmentBody.

        Include translation memory fuzzy matches.  # noqa: E501

        :param tm_matches: The tm_matches of this TranslateSegmentBody.  # noqa: E501
        :type: bool
        """

        self._tm_matches = tm_matches

    @property
    def project_tags(self):
        """Gets the project_tags of this TranslateSegmentBody.  # noqa: E501

        Project tags. Projects tags in source to target if set to true.  # noqa: E501

        :return: The project_tags of this TranslateSegmentBody.  # noqa: E501
        :rtype: bool
        """
        return self._project_tags

    @project_tags.setter
    def project_tags(self, project_tags):
        """Sets the project_tags of this TranslateSegmentBody.

        Project tags. Projects tags in source to target if set to true.  # noqa: E501

        :param project_tags: The project_tags of this TranslateSegmentBody.  # noqa: E501
        :type: bool
        """

        self._project_tags = project_tags

    @property
    def contains_icu_data(self):
        """Gets the contains_icu_data of this TranslateSegmentBody.  # noqa: E501

        Contains ICU data. If true then tags in the source following the ICU standard will be parsed and retained.  # noqa: E501

        :return: The contains_icu_data of this TranslateSegmentBody.  # noqa: E501
        :rtype: bool
        """
        return self._contains_icu_data

    @contains_icu_data.setter
    def contains_icu_data(self, contains_icu_data):
        """Sets the contains_icu_data of this TranslateSegmentBody.

        Contains ICU data. If true then tags in the source following the ICU standard will be parsed and retained.  # noqa: E501

        :param contains_icu_data: The contains_icu_data of this TranslateSegmentBody.  # noqa: E501
        :type: bool
        """

        self._contains_icu_data = contains_icu_data

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
        if not isinstance(other, TranslateSegmentBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TranslateSegmentBody):
            return True

        return self.to_dict() != other.to_dict()
