import json
from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.stakeholder_write_category_enum import StakeholderWriteCategoryEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedStakeholderWrite")


@_attrs_define
class PatchedStakeholderWrite:
    """
    Attributes:
        id (Union[Unset, UUID]):
        current_criticality (Union[Unset, int]):
        residual_criticality (Union[Unset, int]):
        is_published (Union[Unset, bool]):
        category (Union[Unset, StakeholderWriteCategoryEnum]): * `client` - Client
            * `partner` - Partner
            * `supplier` - Supplier
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
        ebios_rm_study (Union[Unset, UUID]): EBIOS RM study that the stakeholder is part of
        entity (Union[Unset, UUID]): Entity qualified by the stakeholder
        applied_controls (Union[Unset, list[UUID]]): Controls applied to lower stakeholder criticality
    """

    id: Union[Unset, UUID] = UNSET
    current_criticality: Union[Unset, int] = UNSET
    residual_criticality: Union[Unset, int] = UNSET
    is_published: Union[Unset, bool] = UNSET
    category: Union[Unset, StakeholderWriteCategoryEnum] = UNSET
    current_dependency: Union[Unset, int] = UNSET
    current_penetration: Union[Unset, int] = UNSET
    current_maturity: Union[Unset, int] = UNSET
    current_trust: Union[Unset, int] = UNSET
    residual_dependency: Union[Unset, int] = UNSET
    residual_penetration: Union[Unset, int] = UNSET
    residual_maturity: Union[Unset, int] = UNSET
    residual_trust: Union[Unset, int] = UNSET
    is_selected: Union[Unset, bool] = UNSET
    justification: Union[Unset, str] = UNSET
    ebios_rm_study: Union[Unset, UUID] = UNSET
    entity: Union[Unset, UUID] = UNSET
    applied_controls: Union[Unset, list[UUID]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        current_criticality = self.current_criticality

        residual_criticality = self.residual_criticality

        is_published = self.is_published

        category: Union[Unset, str] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

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

        ebios_rm_study: Union[Unset, str] = UNSET
        if not isinstance(self.ebios_rm_study, Unset):
            ebios_rm_study = str(self.ebios_rm_study)

        entity: Union[Unset, str] = UNSET
        if not isinstance(self.entity, Unset):
            entity = str(self.entity)

        applied_controls: Union[Unset, list[str]] = UNSET
        if not isinstance(self.applied_controls, Unset):
            applied_controls = []
            for applied_controls_item_data in self.applied_controls:
                applied_controls_item = str(applied_controls_item_data)
                applied_controls.append(applied_controls_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if current_criticality is not UNSET:
            field_dict["current_criticality"] = current_criticality
        if residual_criticality is not UNSET:
            field_dict["residual_criticality"] = residual_criticality
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if category is not UNSET:
            field_dict["category"] = category
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
        if ebios_rm_study is not UNSET:
            field_dict["ebios_rm_study"] = ebios_rm_study
        if entity is not UNSET:
            field_dict["entity"] = entity
        if applied_controls is not UNSET:
            field_dict["applied_controls"] = applied_controls

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        id: Union[Unset, bytes] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        current_criticality = (
            self.current_criticality
            if isinstance(self.current_criticality, Unset)
            else (None, str(self.current_criticality).encode(), "text/plain")
        )

        residual_criticality = (
            self.residual_criticality
            if isinstance(self.residual_criticality, Unset)
            else (None, str(self.residual_criticality).encode(), "text/plain")
        )

        is_published = (
            self.is_published
            if isinstance(self.is_published, Unset)
            else (None, str(self.is_published).encode(), "text/plain")
        )

        category: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.category, Unset):
            category = (None, str(self.category.value).encode(), "text/plain")

        current_dependency = (
            self.current_dependency
            if isinstance(self.current_dependency, Unset)
            else (None, str(self.current_dependency).encode(), "text/plain")
        )

        current_penetration = (
            self.current_penetration
            if isinstance(self.current_penetration, Unset)
            else (None, str(self.current_penetration).encode(), "text/plain")
        )

        current_maturity = (
            self.current_maturity
            if isinstance(self.current_maturity, Unset)
            else (None, str(self.current_maturity).encode(), "text/plain")
        )

        current_trust = (
            self.current_trust
            if isinstance(self.current_trust, Unset)
            else (None, str(self.current_trust).encode(), "text/plain")
        )

        residual_dependency = (
            self.residual_dependency
            if isinstance(self.residual_dependency, Unset)
            else (None, str(self.residual_dependency).encode(), "text/plain")
        )

        residual_penetration = (
            self.residual_penetration
            if isinstance(self.residual_penetration, Unset)
            else (None, str(self.residual_penetration).encode(), "text/plain")
        )

        residual_maturity = (
            self.residual_maturity
            if isinstance(self.residual_maturity, Unset)
            else (None, str(self.residual_maturity).encode(), "text/plain")
        )

        residual_trust = (
            self.residual_trust
            if isinstance(self.residual_trust, Unset)
            else (None, str(self.residual_trust).encode(), "text/plain")
        )

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

        entity: Union[Unset, bytes] = UNSET
        if not isinstance(self.entity, Unset):
            entity = str(self.entity)

        applied_controls: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.applied_controls, Unset):
            _temp_applied_controls = []
            for applied_controls_item_data in self.applied_controls:
                applied_controls_item = str(applied_controls_item_data)
                _temp_applied_controls.append(applied_controls_item)
            applied_controls = (None, json.dumps(_temp_applied_controls).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if current_criticality is not UNSET:
            field_dict["current_criticality"] = current_criticality
        if residual_criticality is not UNSET:
            field_dict["residual_criticality"] = residual_criticality
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if category is not UNSET:
            field_dict["category"] = category
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
        if ebios_rm_study is not UNSET:
            field_dict["ebios_rm_study"] = ebios_rm_study
        if entity is not UNSET:
            field_dict["entity"] = entity
        if applied_controls is not UNSET:
            field_dict["applied_controls"] = applied_controls

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

        current_criticality = d.pop("current_criticality", UNSET)

        residual_criticality = d.pop("residual_criticality", UNSET)

        is_published = d.pop("is_published", UNSET)

        _category = d.pop("category", UNSET)
        category: Union[Unset, StakeholderWriteCategoryEnum]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = StakeholderWriteCategoryEnum(_category)

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

        _ebios_rm_study = d.pop("ebios_rm_study", UNSET)
        ebios_rm_study: Union[Unset, UUID]
        if isinstance(_ebios_rm_study, Unset):
            ebios_rm_study = UNSET
        else:
            ebios_rm_study = UUID(_ebios_rm_study)

        _entity = d.pop("entity", UNSET)
        entity: Union[Unset, UUID]
        if isinstance(_entity, Unset):
            entity = UNSET
        else:
            entity = UUID(_entity)

        applied_controls = []
        _applied_controls = d.pop("applied_controls", UNSET)
        for applied_controls_item_data in _applied_controls or []:
            applied_controls_item = UUID(applied_controls_item_data)

            applied_controls.append(applied_controls_item)

        patched_stakeholder_write = cls(
            id=id,
            current_criticality=current_criticality,
            residual_criticality=residual_criticality,
            is_published=is_published,
            category=category,
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
            ebios_rm_study=ebios_rm_study,
            entity=entity,
            applied_controls=applied_controls,
        )

        patched_stakeholder_write.additional_properties = d
        return patched_stakeholder_write

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
