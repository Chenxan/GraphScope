# coding: utf-8

"""
    GraphScope FLEX HTTP SERVICE API

    This is a specification for GraphScope FLEX HTTP service based on the OpenAPI 3.0 specification. You can find out more details about specification at [doc](https://swagger.io/specification/v3/).  Some useful links: - [GraphScope Repository](https://github.com/alibaba/GraphScope) - [The Source API definition for GraphScope Interactive](https://github.com/GraphScope/portal/tree/main/httpservice)

    The version of the OpenAPI document: 1.0.0
    Contact: graphscope@alibaba-inc.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from graphscope.flex.rest.models.dataloading_job_config_edges_inner import DataloadingJobConfigEdgesInner
from graphscope.flex.rest.models.dataloading_job_config_loading_config import DataloadingJobConfigLoadingConfig
from graphscope.flex.rest.models.dataloading_job_config_vertices_inner import DataloadingJobConfigVerticesInner
from typing import Optional, Set
from typing_extensions import Self

class DataloadingJobConfig(BaseModel):
    """
    DataloadingJobConfig
    """ # noqa: E501
    loading_config: DataloadingJobConfigLoadingConfig
    vertices: List[DataloadingJobConfigVerticesInner]
    edges: List[DataloadingJobConfigEdgesInner]
    schedule: Optional[StrictStr] = Field(default=None, description="format with '2023-02-21 11:56:30'")
    repeat: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["loading_config", "vertices", "edges", "schedule", "repeat"]

    @field_validator('repeat')
    def repeat_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['once', 'day', 'week']):
            raise ValueError("must be one of enum values ('once', 'day', 'week')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DataloadingJobConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of loading_config
        if self.loading_config:
            _dict['loading_config'] = self.loading_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in vertices (list)
        _items = []
        if self.vertices:
            for _item in self.vertices:
                if _item:
                    _items.append(_item.to_dict())
            _dict['vertices'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in edges (list)
        _items = []
        if self.edges:
            for _item in self.edges:
                if _item:
                    _items.append(_item.to_dict())
            _dict['edges'] = _items
        # set to None if schedule (nullable) is None
        # and model_fields_set contains the field
        if self.schedule is None and "schedule" in self.model_fields_set:
            _dict['schedule'] = None

        # set to None if repeat (nullable) is None
        # and model_fields_set contains the field
        if self.repeat is None and "repeat" in self.model_fields_set:
            _dict['repeat'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataloadingJobConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "loading_config": DataloadingJobConfigLoadingConfig.from_dict(obj["loading_config"]) if obj.get("loading_config") is not None else None,
            "vertices": [DataloadingJobConfigVerticesInner.from_dict(_item) for _item in obj["vertices"]] if obj.get("vertices") is not None else None,
            "edges": [DataloadingJobConfigEdgesInner.from_dict(_item) for _item in obj["edges"]] if obj.get("edges") is not None else None,
            "schedule": obj.get("schedule"),
            "repeat": obj.get("repeat")
        })
        return _obj


