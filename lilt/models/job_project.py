# coding: utf-8

"""
    Lilt REST API

    Lilt REST API Support: https://lilt.atlassian.net/servicedesk/customer/portals    The Lilt REST API enables programmatic access to the full-range of Lilt backend services including:   * Training of and translating with interactive, adaptive machine translation   * Large-scale translation memory   * The Lexicon (a large-scale termbase)   * Programmatic control of the Lilt CAT environment   * Translation memory synchronization  Requests and responses are in JSON format. The REST API only responds to HTTPS / SSL requests.  The base url for this REST API is `https://api.lilt.com/`.  ## Authentication  Requests are authenticated via REST API key, which requires the Business plan.  Requests are authenticated using [HTTP Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication). Add your REST API key as both the `username` and `password`.  For development, you may also pass the REST API key via the `key` query parameter. This is less secure than HTTP Basic Auth, and is not recommended for production use.  ## Quotas  Our services have a general quota of 4000 requests per minute. Should you hit the maximum requests per minute, you will need to wait 60 seconds before you can send another request. 

    The version of the OpenAPI document: v3.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class JobProject(BaseModel):
    """
    A job project contains project statistical data that belongs to a specific job. 
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="An id for the project.")
    src_lang: Optional[StrictStr] = Field(default=None, description="Source language, an ISO 639-1 language identifier.", alias="srcLang")
    src_locale: Optional[StrictStr] = Field(default=None, description="A locale identifier, supported for source language.", alias="srcLocale")
    trg_lang: Optional[StrictStr] = Field(default=None, description="Target language, an ISO 639-1 language identifier.", alias="trgLang")
    trg_locale: Optional[StrictStr] = Field(default=None, description="A locale identifier, supported for target language.", alias="trgLocale")
    name: Optional[StrictStr] = Field(default=None, description="A name for the project.")
    due: Optional[StrictStr] = Field(default=None, description="An ISO date.")
    is_complete: Optional[StrictBool] = Field(default=None, description="A state that checks project was completed.", alias="isComplete")
    is_archived: Optional[StrictBool] = Field(default=None, description="The archived state of the project.", alias="isArchived")
    state: Optional[StrictStr] = Field(default=None, description="Current state of the project. Example, backlog, inProgress, inReview, done.")
    num_source_tokens: Optional[StrictInt] = Field(default=None, description="Total number of source tokens.", alias="numSourceTokens")
    created_at: Optional[StrictStr] = Field(default=None, description="Time at which the object was created.", alias="createdAt")
    updated_at: Optional[StrictStr] = Field(default=None, description="Time at which the object was updated.", alias="updatedAt")
    is_deleted: Optional[StrictBool] = Field(default=None, description="A state that checks project was deleted.", alias="isDeleted")
    memory_id: Optional[StrictInt] = Field(default=None, description="A unique number identifying the associated Memory.", alias="memoryId")
    workflow_status: Optional[StrictStr] = Field(default=None, description="The status of the Workflow for the current project.", alias="workflowStatus")
    workflow_name: Optional[StrictStr] = Field(default=None, description="Human readable name of the workflow associated with the current project.", alias="workflowName")
    __properties: ClassVar[List[str]] = ["id", "srcLang", "srcLocale", "trgLang", "trgLocale", "name", "due", "isComplete", "isArchived", "state", "numSourceTokens", "createdAt", "updatedAt", "isDeleted", "memoryId", "workflowStatus", "workflowName"]

    @field_validator('workflow_status')
    def workflow_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['READY_TO_START', 'IN_PROGRESS', 'DONE']):
            raise ValueError("must be one of enum values ('READY_TO_START', 'IN_PROGRESS', 'DONE')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of JobProject from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of JobProject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "srcLang": obj.get("srcLang"),
            "srcLocale": obj.get("srcLocale"),
            "trgLang": obj.get("trgLang"),
            "trgLocale": obj.get("trgLocale"),
            "name": obj.get("name"),
            "due": obj.get("due"),
            "isComplete": obj.get("isComplete"),
            "isArchived": obj.get("isArchived"),
            "state": obj.get("state"),
            "numSourceTokens": obj.get("numSourceTokens"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "isDeleted": obj.get("isDeleted"),
            "memoryId": obj.get("memoryId"),
            "workflowStatus": obj.get("workflowStatus"),
            "workflowName": obj.get("workflowName")
        })
        return _obj


