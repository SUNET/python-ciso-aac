from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FilteredNode")


@_attrs_define
class FilteredNode:
    """
    Attributes:
        id (UUID):
        annotation (Union[None, str]):
        name (str):
        description (Union[None, str]):
        associated_reference_controls (str):
        associated_threats (str):
        parent_requirement (str):
        urn (Union[None, Unset, str]):
        typical_evidence (Union[None, Unset, str]):
        ref_id (Union[None, Unset, str]):
    """

    id: UUID
    annotation: None | str
    name: str
    description: None | str
    associated_reference_controls: str
    associated_threats: str
    parent_requirement: str
    urn: None | Unset | str = UNSET
    typical_evidence: None | Unset | str = UNSET
    ref_id: None | Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        annotation: None | str
        annotation = self.annotation

        name = self.name

        description: None | str
        description = self.description

        associated_reference_controls = self.associated_reference_controls

        associated_threats = self.associated_threats

        parent_requirement = self.parent_requirement

        urn: None | Unset | str
        if isinstance(self.urn, Unset):
            urn = UNSET
        else:
            urn = self.urn

        typical_evidence: None | Unset | str
        if isinstance(self.typical_evidence, Unset):
            typical_evidence = UNSET
        else:
            typical_evidence = self.typical_evidence

        ref_id: None | Unset | str
        if isinstance(self.ref_id, Unset):
            ref_id = UNSET
        else:
            ref_id = self.ref_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "annotation": annotation,
                "name": name,
                "description": description,
                "associated_reference_controls": associated_reference_controls,
                "associated_threats": associated_threats,
                "parent_requirement": parent_requirement,
            }
        )
        if urn is not UNSET:
            field_dict["urn"] = urn
        if typical_evidence is not UNSET:
            field_dict["typical_evidence"] = typical_evidence
        if ref_id is not UNSET:
            field_dict["ref_id"] = ref_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        def _parse_annotation(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        annotation = _parse_annotation(d.pop("annotation"))

        name = d.pop("name")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        associated_reference_controls = d.pop("associated_reference_controls")

        associated_threats = d.pop("associated_threats")

        parent_requirement = d.pop("parent_requirement")

        def _parse_urn(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        urn = _parse_urn(d.pop("urn", UNSET))

        def _parse_typical_evidence(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        typical_evidence = _parse_typical_evidence(d.pop("typical_evidence", UNSET))

        def _parse_ref_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        ref_id = _parse_ref_id(d.pop("ref_id", UNSET))

        filtered_node = cls(
            id=id,
            annotation=annotation,
            name=name,
            description=description,
            associated_reference_controls=associated_reference_controls,
            associated_threats=associated_threats,
            parent_requirement=parent_requirement,
            urn=urn,
            typical_evidence=typical_evidence,
            ref_id=ref_id,
        )

        filtered_node.additional_properties = d
        return filtered_node

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
