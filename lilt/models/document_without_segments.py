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


class DocumentWithoutSegments(object):
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
        'project_id': 'int',
        'srclang': 'str',
        'trglang': 'str',
        'name': 'str',
        'import_in_progress': 'bool',
        'import_succeeded': 'bool',
        'import_error_message': 'str',
        'export_in_progress': 'bool',
        'export_succeeded': 'bool',
        'export_error_message': 'str',
        'is_pretranslating': 'bool',
        'status': 'DocumentWithoutSegmentsStatus',
        'translator_email': 'str',
        'reviewer_email': 'str',
        'created_at': 'int',
        'updated_at': 'int',
        'is_review_complete': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'srclang': 'srclang',
        'trglang': 'trglang',
        'name': 'name',
        'import_in_progress': 'import_in_progress',
        'import_succeeded': 'import_succeeded',
        'import_error_message': 'import_error_message',
        'export_in_progress': 'export_in_progress',
        'export_succeeded': 'export_succeeded',
        'export_error_message': 'export_error_message',
        'is_pretranslating': 'is_pretranslating',
        'status': 'status',
        'translator_email': 'translator_email',
        'reviewer_email': 'reviewer_email',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'is_review_complete': 'is_review_complete'
    }

    def __init__(self, id=None, project_id=None, srclang=None, trglang=None, name=None, import_in_progress=None, import_succeeded=None, import_error_message=None, export_in_progress=None, export_succeeded=None, export_error_message=None, is_pretranslating=None, status=None, translator_email=None, reviewer_email=None, created_at=None, updated_at=None, is_review_complete=None, local_vars_configuration=None):  # noqa: E501
        """DocumentWithoutSegments - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._project_id = None
        self._srclang = None
        self._trglang = None
        self._name = None
        self._import_in_progress = None
        self._import_succeeded = None
        self._import_error_message = None
        self._export_in_progress = None
        self._export_succeeded = None
        self._export_error_message = None
        self._is_pretranslating = None
        self._status = None
        self._translator_email = None
        self._reviewer_email = None
        self._created_at = None
        self._updated_at = None
        self._is_review_complete = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if srclang is not None:
            self.srclang = srclang
        if trglang is not None:
            self.trglang = trglang
        if name is not None:
            self.name = name
        if import_in_progress is not None:
            self.import_in_progress = import_in_progress
        if import_succeeded is not None:
            self.import_succeeded = import_succeeded
        if import_error_message is not None:
            self.import_error_message = import_error_message
        if export_in_progress is not None:
            self.export_in_progress = export_in_progress
        if export_succeeded is not None:
            self.export_succeeded = export_succeeded
        if export_error_message is not None:
            self.export_error_message = export_error_message
        if is_pretranslating is not None:
            self.is_pretranslating = is_pretranslating
        if status is not None:
            self.status = status
        if translator_email is not None:
            self.translator_email = translator_email
        if reviewer_email is not None:
            self.reviewer_email = reviewer_email
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if is_review_complete is not None:
            self.is_review_complete = is_review_complete

    @property
    def id(self):
        """Gets the id of this DocumentWithoutSegments.  # noqa: E501

        A unique number identifying the Document.  # noqa: E501

        :return: The id of this DocumentWithoutSegments.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DocumentWithoutSegments.

        A unique number identifying the Document.  # noqa: E501

        :param id: The id of this DocumentWithoutSegments.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this DocumentWithoutSegments.  # noqa: E501

        A unique number identifying the Project.  # noqa: E501

        :return: The project_id of this DocumentWithoutSegments.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this DocumentWithoutSegments.

        A unique number identifying the Project.  # noqa: E501

        :param project_id: The project_id of this DocumentWithoutSegments.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def srclang(self):
        """Gets the srclang of this DocumentWithoutSegments.  # noqa: E501

        An ISO 639-1 language identifier.  # noqa: E501

        :return: The srclang of this DocumentWithoutSegments.  # noqa: E501
        :rtype: str
        """
        return self._srclang

    @srclang.setter
    def srclang(self, srclang):
        """Sets the srclang of this DocumentWithoutSegments.

        An ISO 639-1 language identifier.  # noqa: E501

        :param srclang: The srclang of this DocumentWithoutSegments.  # noqa: E501
        :type: str
        """

        self._srclang = srclang

    @property
    def trglang(self):
        """Gets the trglang of this DocumentWithoutSegments.  # noqa: E501

        An ISO 639-1 language identifier.  # noqa: E501

        :return: The trglang of this DocumentWithoutSegments.  # noqa: E501
        :rtype: str
        """
        return self._trglang

    @trglang.setter
    def trglang(self, trglang):
        """Sets the trglang of this DocumentWithoutSegments.

        An ISO 639-1 language identifier.  # noqa: E501

        :param trglang: The trglang of this DocumentWithoutSegments.  # noqa: E501
        :type: str
        """

        self._trglang = trglang

    @property
    def name(self):
        """Gets the name of this DocumentWithoutSegments.  # noqa: E501

        The document name.  # noqa: E501

        :return: The name of this DocumentWithoutSegments.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DocumentWithoutSegments.

        The document name.  # noqa: E501

        :param name: The name of this DocumentWithoutSegments.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def import_in_progress(self):
        """Gets the import_in_progress of this DocumentWithoutSegments.  # noqa: E501

        True if the document is currently being imported  # noqa: E501

        :return: The import_in_progress of this DocumentWithoutSegments.  # noqa: E501
        :rtype: bool
        """
        return self._import_in_progress

    @import_in_progress.setter
    def import_in_progress(self, import_in_progress):
        """Sets the import_in_progress of this DocumentWithoutSegments.

        True if the document is currently being imported  # noqa: E501

        :param import_in_progress: The import_in_progress of this DocumentWithoutSegments.  # noqa: E501
        :type: bool
        """

        self._import_in_progress = import_in_progress

    @property
    def import_succeeded(self):
        """Gets the import_succeeded of this DocumentWithoutSegments.  # noqa: E501

        True if the import process succeeded.  # noqa: E501

        :return: The import_succeeded of this DocumentWithoutSegments.  # noqa: E501
        :rtype: bool
        """
        return self._import_succeeded

    @import_succeeded.setter
    def import_succeeded(self, import_succeeded):
        """Sets the import_succeeded of this DocumentWithoutSegments.

        True if the import process succeeded.  # noqa: E501

        :param import_succeeded: The import_succeeded of this DocumentWithoutSegments.  # noqa: E501
        :type: bool
        """

        self._import_succeeded = import_succeeded

    @property
    def import_error_message(self):
        """Gets the import_error_message of this DocumentWithoutSegments.  # noqa: E501

        Error message if `import_succeeded=false`  # noqa: E501

        :return: The import_error_message of this DocumentWithoutSegments.  # noqa: E501
        :rtype: str
        """
        return self._import_error_message

    @import_error_message.setter
    def import_error_message(self, import_error_message):
        """Sets the import_error_message of this DocumentWithoutSegments.

        Error message if `import_succeeded=false`  # noqa: E501

        :param import_error_message: The import_error_message of this DocumentWithoutSegments.  # noqa: E501
        :type: str
        """

        self._import_error_message = import_error_message

    @property
    def export_in_progress(self):
        """Gets the export_in_progress of this DocumentWithoutSegments.  # noqa: E501

        True if the document is currently being exported for download  # noqa: E501

        :return: The export_in_progress of this DocumentWithoutSegments.  # noqa: E501
        :rtype: bool
        """
        return self._export_in_progress

    @export_in_progress.setter
    def export_in_progress(self, export_in_progress):
        """Sets the export_in_progress of this DocumentWithoutSegments.

        True if the document is currently being exported for download  # noqa: E501

        :param export_in_progress: The export_in_progress of this DocumentWithoutSegments.  # noqa: E501
        :type: bool
        """

        self._export_in_progress = export_in_progress

    @property
    def export_succeeded(self):
        """Gets the export_succeeded of this DocumentWithoutSegments.  # noqa: E501

        True if the export process succeeded.  # noqa: E501

        :return: The export_succeeded of this DocumentWithoutSegments.  # noqa: E501
        :rtype: bool
        """
        return self._export_succeeded

    @export_succeeded.setter
    def export_succeeded(self, export_succeeded):
        """Sets the export_succeeded of this DocumentWithoutSegments.

        True if the export process succeeded.  # noqa: E501

        :param export_succeeded: The export_succeeded of this DocumentWithoutSegments.  # noqa: E501
        :type: bool
        """

        self._export_succeeded = export_succeeded

    @property
    def export_error_message(self):
        """Gets the export_error_message of this DocumentWithoutSegments.  # noqa: E501

        Error message if `export_succeeded=false`  # noqa: E501

        :return: The export_error_message of this DocumentWithoutSegments.  # noqa: E501
        :rtype: str
        """
        return self._export_error_message

    @export_error_message.setter
    def export_error_message(self, export_error_message):
        """Sets the export_error_message of this DocumentWithoutSegments.

        Error message if `export_succeeded=false`  # noqa: E501

        :param export_error_message: The export_error_message of this DocumentWithoutSegments.  # noqa: E501
        :type: str
        """

        self._export_error_message = export_error_message

    @property
    def is_pretranslating(self):
        """Gets the is_pretranslating of this DocumentWithoutSegments.  # noqa: E501

        True if the document is currently being pretranslated.  # noqa: E501

        :return: The is_pretranslating of this DocumentWithoutSegments.  # noqa: E501
        :rtype: bool
        """
        return self._is_pretranslating

    @is_pretranslating.setter
    def is_pretranslating(self, is_pretranslating):
        """Sets the is_pretranslating of this DocumentWithoutSegments.

        True if the document is currently being pretranslated.  # noqa: E501

        :param is_pretranslating: The is_pretranslating of this DocumentWithoutSegments.  # noqa: E501
        :type: bool
        """

        self._is_pretranslating = is_pretranslating

    @property
    def status(self):
        """Gets the status of this DocumentWithoutSegments.  # noqa: E501


        :return: The status of this DocumentWithoutSegments.  # noqa: E501
        :rtype: DocumentWithoutSegmentsStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DocumentWithoutSegments.


        :param status: The status of this DocumentWithoutSegments.  # noqa: E501
        :type: DocumentWithoutSegmentsStatus
        """

        self._status = status

    @property
    def translator_email(self):
        """Gets the translator_email of this DocumentWithoutSegments.  # noqa: E501

        The email of the assigned translator.  # noqa: E501

        :return: The translator_email of this DocumentWithoutSegments.  # noqa: E501
        :rtype: str
        """
        return self._translator_email

    @translator_email.setter
    def translator_email(self, translator_email):
        """Sets the translator_email of this DocumentWithoutSegments.

        The email of the assigned translator.  # noqa: E501

        :param translator_email: The translator_email of this DocumentWithoutSegments.  # noqa: E501
        :type: str
        """

        self._translator_email = translator_email

    @property
    def reviewer_email(self):
        """Gets the reviewer_email of this DocumentWithoutSegments.  # noqa: E501

        The email of the assigned reviewer.  # noqa: E501

        :return: The reviewer_email of this DocumentWithoutSegments.  # noqa: E501
        :rtype: str
        """
        return self._reviewer_email

    @reviewer_email.setter
    def reviewer_email(self, reviewer_email):
        """Sets the reviewer_email of this DocumentWithoutSegments.

        The email of the assigned reviewer.  # noqa: E501

        :param reviewer_email: The reviewer_email of this DocumentWithoutSegments.  # noqa: E501
        :type: str
        """

        self._reviewer_email = reviewer_email

    @property
    def created_at(self):
        """Gets the created_at of this DocumentWithoutSegments.  # noqa: E501

        Time at which the object was created. Measured in seconds since the Unix epoch.  # noqa: E501

        :return: The created_at of this DocumentWithoutSegments.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DocumentWithoutSegments.

        Time at which the object was created. Measured in seconds since the Unix epoch.  # noqa: E501

        :param created_at: The created_at of this DocumentWithoutSegments.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this DocumentWithoutSegments.  # noqa: E501

        Time at which the object was created. Measured in seconds since the Unix epoch.  # noqa: E501

        :return: The updated_at of this DocumentWithoutSegments.  # noqa: E501
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this DocumentWithoutSegments.

        Time at which the object was created. Measured in seconds since the Unix epoch.  # noqa: E501

        :param updated_at: The updated_at of this DocumentWithoutSegments.  # noqa: E501
        :type: int
        """

        self._updated_at = updated_at

    @property
    def is_review_complete(self):
        """Gets the is_review_complete of this DocumentWithoutSegments.  # noqa: E501

        Document review status.  # noqa: E501

        :return: The is_review_complete of this DocumentWithoutSegments.  # noqa: E501
        :rtype: bool
        """
        return self._is_review_complete

    @is_review_complete.setter
    def is_review_complete(self, is_review_complete):
        """Sets the is_review_complete of this DocumentWithoutSegments.

        Document review status.  # noqa: E501

        :param is_review_complete: The is_review_complete of this DocumentWithoutSegments.  # noqa: E501
        :type: bool
        """

        self._is_review_complete = is_review_complete

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
        if not isinstance(other, DocumentWithoutSegments):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DocumentWithoutSegments):
            return True

        return self.to_dict() != other.to_dict()
