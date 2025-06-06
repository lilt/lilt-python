# coding: utf-8

"""
    Lilt REST API

    Lilt REST API Support: https://lilt.atlassian.net/servicedesk/customer/portals    The Lilt REST API enables programmatic access to the full-range of Lilt backend services including:   * Training of and translating with interactive, adaptive machine translation   * Large-scale translation memory   * The Lexicon (a large-scale termbase)   * Programmatic control of the Lilt CAT environment   * Translation memory synchronization  Requests and responses are in JSON format. The REST API only responds to HTTPS / SSL requests.  The base url for this REST API is `https://api.lilt.com/`.  ## Authentication  Requests are authenticated via REST API key, which requires the Business plan.  Requests are authenticated using [HTTP Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication). Add your REST API key as both the `username` and `password`.  For development, you may also pass the REST API key via the `key` query parameter. This is less secure than HTTP Basic Auth, and is not recommended for production use.  ## Quotas  Our services have a general quota of 4000 requests per minute. Should you hit the maximum requests per minute, you will need to wait 60 seconds before you can send another request. 

    The version of the OpenAPI document: v3.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Optional
from lilt.models.webhooks_update_request_any_of import WebhooksUpdateRequestAnyOf
from lilt.models.webhooks_update_request_any_of1 import WebhooksUpdateRequestAnyOf1
from lilt.models.webhooks_update_request_any_of2 import WebhooksUpdateRequestAnyOf2
from typing import Union, Any, List, Set, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field

WEBHOOKSUPDATEREQUEST_ANY_OF_SCHEMAS = ["WebhooksUpdateRequestAnyOf", "WebhooksUpdateRequestAnyOf1", "WebhooksUpdateRequestAnyOf2"]

class WebhooksUpdateRequest(BaseModel):
    """
    WebhooksUpdateRequest
    """

    # data type: WebhooksUpdateRequestAnyOf
    anyof_schema_1_validator: Optional[WebhooksUpdateRequestAnyOf] = None
    # data type: WebhooksUpdateRequestAnyOf1
    anyof_schema_2_validator: Optional[WebhooksUpdateRequestAnyOf1] = None
    # data type: WebhooksUpdateRequestAnyOf2
    anyof_schema_3_validator: Optional[WebhooksUpdateRequestAnyOf2] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[WebhooksUpdateRequestAnyOf, WebhooksUpdateRequestAnyOf1, WebhooksUpdateRequestAnyOf2]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: Set[str] = { "WebhooksUpdateRequestAnyOf", "WebhooksUpdateRequestAnyOf1", "WebhooksUpdateRequestAnyOf2" }

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        instance = WebhooksUpdateRequest.model_construct()
        error_messages = []
        # validate data type: WebhooksUpdateRequestAnyOf
        if not isinstance(v, WebhooksUpdateRequestAnyOf):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WebhooksUpdateRequestAnyOf`")
        else:
            return v

        # validate data type: WebhooksUpdateRequestAnyOf1
        if not isinstance(v, WebhooksUpdateRequestAnyOf1):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WebhooksUpdateRequestAnyOf1`")
        else:
            return v

        # validate data type: WebhooksUpdateRequestAnyOf2
        if not isinstance(v, WebhooksUpdateRequestAnyOf2):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WebhooksUpdateRequestAnyOf2`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in WebhooksUpdateRequest with anyOf schemas: WebhooksUpdateRequestAnyOf, WebhooksUpdateRequestAnyOf1, WebhooksUpdateRequestAnyOf2. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[WebhooksUpdateRequestAnyOf] = None
        try:
            instance.actual_instance = WebhooksUpdateRequestAnyOf.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[WebhooksUpdateRequestAnyOf1] = None
        try:
            instance.actual_instance = WebhooksUpdateRequestAnyOf1.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_3_validator: Optional[WebhooksUpdateRequestAnyOf2] = None
        try:
            instance.actual_instance = WebhooksUpdateRequestAnyOf2.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into WebhooksUpdateRequest with anyOf schemas: WebhooksUpdateRequestAnyOf, WebhooksUpdateRequestAnyOf1, WebhooksUpdateRequestAnyOf2. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], WebhooksUpdateRequestAnyOf, WebhooksUpdateRequestAnyOf1, WebhooksUpdateRequestAnyOf2]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


