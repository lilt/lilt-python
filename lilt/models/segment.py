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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Segment(BaseModel):
    """
    A Segment is a source string and, optionally, its translation. A Segment can be associated with both a Memory and a Document. The Segment object contains additional metadata about the source and target strings. 
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="A unique number identifying the Segment.")
    created_at: Optional[StrictInt] = Field(default=None, description="Time at which the object was created. Measured in seconds since the Unix epoch.")
    updated_at: Optional[StrictInt] = Field(default=None, description="Time at which the object was created. Measured in seconds since the Unix epoch.")
    document_id: Optional[StrictInt] = Field(default=None, description="A unique Document identifier.")
    memory_id: Optional[StrictInt] = Field(default=None, description="The Memory with which this Segment is associated.")
    source: Optional[StrictStr] = Field(default=None, description="The source string.")
    srclang: Optional[StrictStr] = Field(default=None, description="An ISO 639-1 language code.")
    target: Optional[StrictStr] = Field(default=None, description="The target string.")
    trglang: Optional[StrictStr] = Field(default=None, description="An ISO 639-1 language code.")
    is_confirmed: Optional[StrictBool] = Field(default=None, description="The confirmation status.")
    is_reviewed: Optional[StrictBool] = Field(default=None, description="The review status.")
    __properties: ClassVar[List[str]] = ["id", "created_at", "updated_at", "document_id", "memory_id", "source", "srclang", "target", "trglang", "is_confirmed", "is_reviewed"]

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
        """Create an instance of Segment from a JSON string"""
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
        """Create an instance of Segment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "document_id": obj.get("document_id"),
            "memory_id": obj.get("memory_id"),
            "source": obj.get("source"),
            "srclang": obj.get("srclang"),
            "target": obj.get("target"),
            "trglang": obj.get("trglang"),
            "is_confirmed": obj.get("is_confirmed"),
            "is_reviewed": obj.get("is_reviewed")
        })
        return _obj


