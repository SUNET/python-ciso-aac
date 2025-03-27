import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.risk_origin_enum import RiskOriginEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="RoToRead")


@_attrs_define
class RoToRead:
    """
    Attributes:
        id (UUID):
        str_ (str):
        ebios_rm_study (str):
        folder (str):
        feared_events (list[str]):
        motivation (str):
        resources (str):
        activity (str):
        pertinence (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        risk_origin (RiskOriginEnum): * `state` - State
            * `organized_crime` - Organized crime
            * `terrorist` - Terrorist
            * `activist` - Activist
            * `competitor` - Competitor
            * `amateur` - Amateur
            * `avenger` - Avenger
            * `pathological` - Pathological
        target_objective (str):
        is_published (Union[Unset, bool]):
        is_selected (Union[Unset, bool]):
        justification (Union[Unset, str]):
    """

    id: UUID
    str_: str
    ebios_rm_study: str
    folder: str
    feared_events: list[str]
    motivation: str
    resources: str
    activity: str
    pertinence: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    risk_origin: RiskOriginEnum
    target_objective: str
    is_published: Union[Unset, bool] = UNSET
    is_selected: Union[Unset, bool] = UNSET
    justification: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        str_ = self.str_

        ebios_rm_study = self.ebios_rm_study

        folder = self.folder

        feared_events = self.feared_events

        motivation = self.motivation

        resources = self.resources

        activity = self.activity

        pertinence = self.pertinence

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        risk_origin = self.risk_origin.value

        target_objective = self.target_objective

        is_published = self.is_published

        is_selected = self.is_selected

        justification = self.justification

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "str": str_,
                "ebios_rm_study": ebios_rm_study,
                "folder": folder,
                "feared_events": feared_events,
                "motivation": motivation,
                "resources": resources,
                "activity": activity,
                "pertinence": pertinence,
                "created_at": created_at,
                "updated_at": updated_at,
                "risk_origin": risk_origin,
                "target_objective": target_objective,
            }
        )
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if is_selected is not UNSET:
            field_dict["is_selected"] = is_selected
        if justification is not UNSET:
            field_dict["justification"] = justification

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        str_ = d.pop("str")

        ebios_rm_study = d.pop("ebios_rm_study")

        folder = d.pop("folder")

        feared_events = cast(list[str], d.pop("feared_events"))

        motivation = d.pop("motivation")

        resources = d.pop("resources")

        activity = d.pop("activity")

        pertinence = d.pop("pertinence")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        risk_origin = RiskOriginEnum(d.pop("risk_origin"))

        target_objective = d.pop("target_objective")

        is_published = d.pop("is_published", UNSET)

        is_selected = d.pop("is_selected", UNSET)

        justification = d.pop("justification", UNSET)

        ro_to_read = cls(
            id=id,
            str_=str_,
            ebios_rm_study=ebios_rm_study,
            folder=folder,
            feared_events=feared_events,
            motivation=motivation,
            resources=resources,
            activity=activity,
            pertinence=pertinence,
            created_at=created_at,
            updated_at=updated_at,
            risk_origin=risk_origin,
            target_objective=target_objective,
            is_published=is_published,
            is_selected=is_selected,
            justification=justification,
        )

        ro_to_read.additional_properties = d
        return ro_to_read

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
