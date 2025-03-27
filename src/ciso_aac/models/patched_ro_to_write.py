import json
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activity_enum import ActivityEnum
from ..models.motivation_enum import MotivationEnum
from ..models.resources_enum import ResourcesEnum
from ..models.risk_origin_enum import RiskOriginEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedRoToWrite")


@_attrs_define
class PatchedRoToWrite:
    """
    Attributes:
        id (Union[Unset, UUID]):
        is_published (Union[Unset, bool]):
        risk_origin (Union[Unset, RiskOriginEnum]): * `state` - State
            * `organized_crime` - Organized crime
            * `terrorist` - Terrorist
            * `activist` - Activist
            * `competitor` - Competitor
            * `amateur` - Amateur
            * `avenger` - Avenger
            * `pathological` - Pathological
        target_objective (Union[Unset, str]):
        motivation (Union[Unset, MotivationEnum]): * `0` - undefined
            * `1` - very_low
            * `2` - low
            * `3` - significant
            * `4` - strong
        resources (Union[Unset, ResourcesEnum]): * `0` - undefined
            * `1` - limited
            * `2` - significant
            * `3` - important
            * `4` - unlimited
        activity (Union[Unset, ActivityEnum]): * `0` - undefined
            * `1` - very_low
            * `2` - low
            * `3` - moderate
            * `4` - important
        is_selected (Union[Unset, bool]):
        justification (Union[Unset, str]):
        ebios_rm_study (Union[Unset, UUID]):
        feared_events (Union[Unset, list[UUID]]):
    """

    id: Union[Unset, UUID] = UNSET
    is_published: Union[Unset, bool] = UNSET
    risk_origin: Union[Unset, RiskOriginEnum] = UNSET
    target_objective: Union[Unset, str] = UNSET
    motivation: Union[Unset, MotivationEnum] = UNSET
    resources: Union[Unset, ResourcesEnum] = UNSET
    activity: Union[Unset, ActivityEnum] = UNSET
    is_selected: Union[Unset, bool] = UNSET
    justification: Union[Unset, str] = UNSET
    ebios_rm_study: Union[Unset, UUID] = UNSET
    feared_events: Union[Unset, list[UUID]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_published = self.is_published

        risk_origin: Union[Unset, str] = UNSET
        if not isinstance(self.risk_origin, Unset):
            risk_origin = self.risk_origin.value

        target_objective = self.target_objective

        motivation: Union[Unset, int] = UNSET
        if not isinstance(self.motivation, Unset):
            motivation = self.motivation.value

        resources: Union[Unset, int] = UNSET
        if not isinstance(self.resources, Unset):
            resources = self.resources.value

        activity: Union[Unset, int] = UNSET
        if not isinstance(self.activity, Unset):
            activity = self.activity.value

        is_selected = self.is_selected

        justification = self.justification

        ebios_rm_study: Union[Unset, str] = UNSET
        if not isinstance(self.ebios_rm_study, Unset):
            ebios_rm_study = str(self.ebios_rm_study)

        feared_events: Union[Unset, list[str]] = UNSET
        if not isinstance(self.feared_events, Unset):
            feared_events = []
            for feared_events_item_data in self.feared_events:
                feared_events_item = str(feared_events_item_data)
                feared_events.append(feared_events_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if risk_origin is not UNSET:
            field_dict["risk_origin"] = risk_origin
        if target_objective is not UNSET:
            field_dict["target_objective"] = target_objective
        if motivation is not UNSET:
            field_dict["motivation"] = motivation
        if resources is not UNSET:
            field_dict["resources"] = resources
        if activity is not UNSET:
            field_dict["activity"] = activity
        if is_selected is not UNSET:
            field_dict["is_selected"] = is_selected
        if justification is not UNSET:
            field_dict["justification"] = justification
        if ebios_rm_study is not UNSET:
            field_dict["ebios_rm_study"] = ebios_rm_study
        if feared_events is not UNSET:
            field_dict["feared_events"] = feared_events

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        id: Union[Unset, bytes] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_published = (
            self.is_published
            if isinstance(self.is_published, Unset)
            else (None, str(self.is_published).encode(), "text/plain")
        )

        risk_origin: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.risk_origin, Unset):
            risk_origin = (None, str(self.risk_origin.value).encode(), "text/plain")

        target_objective = (
            self.target_objective
            if isinstance(self.target_objective, Unset)
            else (None, str(self.target_objective).encode(), "text/plain")
        )

        motivation: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.motivation, Unset):
            motivation = (None, str(self.motivation.value).encode(), "text/plain")

        resources: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.resources, Unset):
            resources = (None, str(self.resources.value).encode(), "text/plain")

        activity: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.activity, Unset):
            activity = (None, str(self.activity.value).encode(), "text/plain")

        is_selected = (
            self.is_selected
            if isinstance(self.is_selected, Unset)
            else (None, str(self.is_selected).encode(), "text/plain")
        )

        justification = (
            self.justification
            if isinstance(self.justification, Unset)
            else (None, str(self.justification).encode(), "text/plain")
        )

        ebios_rm_study: Union[Unset, bytes] = UNSET
        if not isinstance(self.ebios_rm_study, Unset):
            ebios_rm_study = str(self.ebios_rm_study)

        feared_events: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.feared_events, Unset):
            _temp_feared_events = []
            for feared_events_item_data in self.feared_events:
                feared_events_item = str(feared_events_item_data)
                _temp_feared_events.append(feared_events_item)
            feared_events = (None, json.dumps(_temp_feared_events).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if risk_origin is not UNSET:
            field_dict["risk_origin"] = risk_origin
        if target_objective is not UNSET:
            field_dict["target_objective"] = target_objective
        if motivation is not UNSET:
            field_dict["motivation"] = motivation
        if resources is not UNSET:
            field_dict["resources"] = resources
        if activity is not UNSET:
            field_dict["activity"] = activity
        if is_selected is not UNSET:
            field_dict["is_selected"] = is_selected
        if justification is not UNSET:
            field_dict["justification"] = justification
        if ebios_rm_study is not UNSET:
            field_dict["ebios_rm_study"] = ebios_rm_study
        if feared_events is not UNSET:
            field_dict["feared_events"] = feared_events

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: Union[Unset, UUID]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        is_published = d.pop("is_published", UNSET)

        _risk_origin = d.pop("risk_origin", UNSET)
        risk_origin: Union[Unset, RiskOriginEnum]
        if isinstance(_risk_origin, Unset):
            risk_origin = UNSET
        else:
            risk_origin = RiskOriginEnum(_risk_origin)

        target_objective = d.pop("target_objective", UNSET)

        _motivation = d.pop("motivation", UNSET)
        motivation: Union[Unset, MotivationEnum]
        if isinstance(_motivation, Unset):
            motivation = UNSET
        else:
            motivation = MotivationEnum(_motivation)

        _resources = d.pop("resources", UNSET)
        resources: Union[Unset, ResourcesEnum]
        if isinstance(_resources, Unset):
            resources = UNSET
        else:
            resources = ResourcesEnum(_resources)

        _activity = d.pop("activity", UNSET)
        activity: Union[Unset, ActivityEnum]
        if isinstance(_activity, Unset):
            activity = UNSET
        else:
            activity = ActivityEnum(_activity)

        is_selected = d.pop("is_selected", UNSET)

        justification = d.pop("justification", UNSET)

        _ebios_rm_study = d.pop("ebios_rm_study", UNSET)
        ebios_rm_study: Union[Unset, UUID]
        if isinstance(_ebios_rm_study, Unset):
            ebios_rm_study = UNSET
        else:
            ebios_rm_study = UUID(_ebios_rm_study)

        feared_events = []
        _feared_events = d.pop("feared_events", UNSET)
        for feared_events_item_data in _feared_events or []:
            feared_events_item = UUID(feared_events_item_data)

            feared_events.append(feared_events_item)

        patched_ro_to_write = cls(
            id=id,
            is_published=is_published,
            risk_origin=risk_origin,
            target_objective=target_objective,
            motivation=motivation,
            resources=resources,
            activity=activity,
            is_selected=is_selected,
            justification=justification,
            ebios_rm_study=ebios_rm_study,
            feared_events=feared_events,
        )

        patched_ro_to_write.additional_properties = d
        return patched_ro_to_write

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
