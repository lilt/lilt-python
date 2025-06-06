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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from lilt.models.job_project import JobProject
from typing import Optional, Set
from typing_extensions import Self

class JobStats(BaseModel):
    """
    A job stats shows an overview of job's statistical data including total number of exact words, fuzzy words, language pairs, projects, etc. 
    """ # noqa: E501
    exact_words: Optional[StrictInt] = Field(default=None, description="Total number of exact words.", alias="exactWords")
    fuzzy_words: Optional[StrictInt] = Field(default=None, description="Total number of fuzzy words.", alias="fuzzyWords")
    new_words: Optional[StrictInt] = Field(default=None, description="Total number of fuzzy words.", alias="newWords")
    num_delivered_projects: Optional[StrictInt] = Field(default=None, description="Total number of delivered projects.", alias="numDeliveredProjects")
    num_language_pairs: Optional[StrictInt] = Field(default=None, description="Total number of delivered projects.", alias="numLanguagePairs")
    num_projects: Optional[StrictInt] = Field(default=None, description="Total number of projects.", alias="numProjects")
    percent_reviewed: Optional[StrictInt] = Field(default=None, description="Overall percentage of documents reviewed.", alias="percentReviewed")
    percent_translated: Optional[StrictInt] = Field(default=None, description="Overall percentage of documents translated.", alias="percentTranslated")
    projects: Optional[List[JobProject]] = None
    source_words: Optional[StrictInt] = Field(default=None, description="Total number of source words.", alias="sourceWords")
    unique_language_pairs: Optional[StrictInt] = Field(default=None, description="Number of unique language pairs.", alias="uniqueLanguagePairs")
    unique_linguists: Optional[StrictInt] = Field(default=None, description="Number of unique linguists.", alias="uniqueLinguists")
    workflow_status: Optional[StrictStr] = Field(default=None, description="The status of the Workflow for the current job.", alias="workflowStatus")
    __properties: ClassVar[List[str]] = ["exactWords", "fuzzyWords", "newWords", "numDeliveredProjects", "numLanguagePairs", "numProjects", "percentReviewed", "percentTranslated", "projects", "sourceWords", "uniqueLanguagePairs", "uniqueLinguists", "workflowStatus"]

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
        """Create an instance of JobStats from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in projects (list)
        _items = []
        if self.projects:
            for _item_projects in self.projects:
                if _item_projects:
                    _items.append(_item_projects.to_dict())
            _dict['projects'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of JobStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "exactWords": obj.get("exactWords"),
            "fuzzyWords": obj.get("fuzzyWords"),
            "newWords": obj.get("newWords"),
            "numDeliveredProjects": obj.get("numDeliveredProjects"),
            "numLanguagePairs": obj.get("numLanguagePairs"),
            "numProjects": obj.get("numProjects"),
            "percentReviewed": obj.get("percentReviewed"),
            "percentTranslated": obj.get("percentTranslated"),
            "projects": [JobProject.from_dict(_item) for _item in obj["projects"]] if obj.get("projects") is not None else None,
            "sourceWords": obj.get("sourceWords"),
            "uniqueLanguagePairs": obj.get("uniqueLanguagePairs"),
            "uniqueLinguists": obj.get("uniqueLinguists"),
            "workflowStatus": obj.get("workflowStatus")
        })
        return _obj


