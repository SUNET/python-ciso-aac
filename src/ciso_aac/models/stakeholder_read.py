import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define, field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="StakeholderRead")


@_attrs_define
class StakeholderRead:
    """
    Attributes:
        id (UUID):
        str_ (str):
        ebios_rm_study (str):
        folder (str):
        entity (str):
        applied_controls (list[str]):
        category (str):
        current_criticality (str):
        residual_criticality (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        is_published (Union[Unset, bool]):
        current_dependency (Union[Unset, int]):
        current_penetration (Union[Unset, int]):
        current_maturity (Union[Unset, int]):
        current_trust (Union[Unset, int]):
        residual_dependency (Union[Unset, int]):
        residual_penetration (Union[Unset, int]):
        residual_maturity (Union[Unset, int]):
        residual_trust (Union[Unset, int]):
        is_selected (Union[Unset, bool]):
        justification (Union[Unset, str]):
    """

    id: UUID
    str_: str
    ebios_rm_study: str
    folder: str
    entity: str
    applied_controls: list[str]
    category: str
    current_criticality: str
    residual_criticality: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    is_published: Unset | bool = UNSET
    current_dependency: Unset | int = UNSET
    current_penetration: Unset | int = UNSET
    current_maturity: Unset | int = UNSET
    current_trust: Unset | int = UNSET
    residual_dependency: Unset | int = UNSET
    residual_penetration: Unset | int = UNSET
    residual_maturity: Unset | int = UNSET
    residual_trust: Unset | int = UNSET
    is_selected: Unset | bool = UNSET
    justification: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        str_ = self.str_

        ebios_rm_study = self.ebios_rm_study

        folder = self.folder

        entity = self.entity

        applied_controls = self.applied_controls

        category = self.category

        current_criticality = self.current_criticality

        residual_criticality = self.residual_criticality

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        is_published = self.is_published

        current_dependency = self.current_dependency

        current_penetration = self.current_penetration

        current_maturity = self.current_maturity

        current_trust = self.current_trust

        residual_dependency = self.residual_dependency

        residual_penetration = self.residual_penetration

        residual_maturity = self.residual_maturity

        residual_trust = self.residual_trust

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
                "entity": entity,
                "applied_controls": applied_controls,
                "category": category,
                "current_criticality": current_criticality,
                "residual_criticality": residual_criticality,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if current_dependency is not UNSET:
            field_dict["current_dependency"] = current_dependency
        if current_penetration is not UNSET:
            field_dict["current_penetration"] = current_penetration
        if current_maturity is not UNSET:
            field_dict["current_maturity"] = current_maturity
        if current_trust is not UNSET:
            field_dict["current_trust"] = current_trust
        if residual_dependency is not UNSET:
            field_dict["residual_dependency"] = residual_dependency
        if residual_penetration is not UNSET:
            field_dict["residual_penetration"] = residual_penetration
        if residual_maturity is not UNSET:
            field_dict["residual_maturity"] = residual_maturity
        if residual_trust is not UNSET:
            field_dict["residual_trust"] = residual_trust
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

        entity = d.pop("entity")

        applied_controls = cast(list[str], d.pop("applied_controls"))

        category = d.pop("category")

        current_criticality = d.pop("current_criticality")

        residual_criticality = d.pop("residual_criticality")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        is_published = d.pop("is_published", UNSET)

        current_dependency = d.pop("current_dependency", UNSET)

        current_penetration = d.pop("current_penetration", UNSET)

        current_maturity = d.pop("current_maturity", UNSET)

        current_trust = d.pop("current_trust", UNSET)

        residual_dependency = d.pop("residual_dependency", UNSET)

        residual_penetration = d.pop("residual_penetration", UNSET)

        residual_maturity = d.pop("residual_maturity", UNSET)

        residual_trust = d.pop("residual_trust", UNSET)

        is_selected = d.pop("is_selected", UNSET)

        justification = d.pop("justification", UNSET)

        stakeholder_read = cls(
            id=id,
            str_=str_,
            ebios_rm_study=ebios_rm_study,
            folder=folder,
            entity=entity,
            applied_controls=applied_controls,
            category=category,
            current_criticality=current_criticality,
            residual_criticality=residual_criticality,
            created_at=created_at,
            updated_at=updated_at,
            is_published=is_published,
            current_dependency=current_dependency,
            current_penetration=current_penetration,
            current_maturity=current_maturity,
            current_trust=current_trust,
            residual_dependency=residual_dependency,
            residual_penetration=residual_penetration,
            residual_maturity=residual_maturity,
            residual_trust=residual_trust,
            is_selected=is_selected,
            justification=justification,
        )

        stakeholder_read.additional_properties = d
        return stakeholder_read

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
