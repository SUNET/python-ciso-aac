import datetime
import json
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedRequirementNodeWrite")


@_attrs_define
class PatchedRequirementNodeWrite:
    """
    Attributes:
        id (Union[Unset, UUID]):
        name (Union[Unset, str]):
        description (Union[None, Unset, str]):
        annotation (Union[None, Unset, str]):
        reference_controls (Union[Unset, list[str]]):
        threats (Union[Unset, list[str]]):
        display_short (Union[Unset, str]):
        display_long (Union[Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
        is_published (Union[Unset, bool]):
        urn (Union[None, Unset, str]):
        ref_id (Union[None, Unset, str]):
        provider (Union[None, Unset, str]):
        locale (Union[Unset, str]):
        default_locale (Union[Unset, bool]):
        parent_urn (Union[None, Unset, str]):
        order_id (Union[None, Unset, int]):
        implementation_groups (Union[Unset, Any]):
        assessable (Union[Unset, bool]):
        typical_evidence (Union[None, Unset, str]):
        question (Union[Unset, Any]):
        folder (Union[Unset, UUID]):
        framework (Union[None, UUID, Unset]):
    """

    id: Unset | UUID = UNSET
    name: Unset | str = UNSET
    description: None | Unset | str = UNSET
    annotation: None | Unset | str = UNSET
    reference_controls: Unset | list[str] = UNSET
    threats: Unset | list[str] = UNSET
    display_short: Unset | str = UNSET
    display_long: Unset | str = UNSET
    created_at: Unset | datetime.datetime = UNSET
    updated_at: Unset | datetime.datetime = UNSET
    is_published: Unset | bool = UNSET
    urn: None | Unset | str = UNSET
    ref_id: None | Unset | str = UNSET
    provider: None | Unset | str = UNSET
    locale: Unset | str = UNSET
    default_locale: Unset | bool = UNSET
    parent_urn: None | Unset | str = UNSET
    order_id: None | Unset | int = UNSET
    implementation_groups: Unset | Any = UNSET
    assessable: Unset | bool = UNSET
    typical_evidence: None | Unset | str = UNSET
    question: Unset | Any = UNSET
    folder: Unset | UUID = UNSET
    framework: None | UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: Unset | str = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name = self.name

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        annotation: None | Unset | str
        if isinstance(self.annotation, Unset):
            annotation = UNSET
        else:
            annotation = self.annotation

        reference_controls: Unset | list[str] = UNSET
        if not isinstance(self.reference_controls, Unset):
            reference_controls = self.reference_controls

        threats: Unset | list[str] = UNSET
        if not isinstance(self.threats, Unset):
            threats = self.threats

        display_short = self.display_short

        display_long = self.display_long

        created_at: Unset | str = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Unset | str = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        is_published = self.is_published

        urn: None | Unset | str
        if isinstance(self.urn, Unset):
            urn = UNSET
        else:
            urn = self.urn

        ref_id: None | Unset | str
        if isinstance(self.ref_id, Unset):
            ref_id = UNSET
        else:
            ref_id = self.ref_id

        provider: None | Unset | str
        if isinstance(self.provider, Unset):
            provider = UNSET
        else:
            provider = self.provider

        locale = self.locale

        default_locale = self.default_locale

        parent_urn: None | Unset | str
        if isinstance(self.parent_urn, Unset):
            parent_urn = UNSET
        else:
            parent_urn = self.parent_urn

        order_id: None | Unset | int
        if isinstance(self.order_id, Unset):
            order_id = UNSET
        else:
            order_id = self.order_id

        implementation_groups = self.implementation_groups

        assessable = self.assessable

        typical_evidence: None | Unset | str
        if isinstance(self.typical_evidence, Unset):
            typical_evidence = UNSET
        else:
            typical_evidence = self.typical_evidence

        question = self.question

        folder: Unset | str = UNSET
        if not isinstance(self.folder, Unset):
            folder = str(self.folder)

        framework: None | Unset | str
        if isinstance(self.framework, Unset):
            framework = UNSET
        elif isinstance(self.framework, UUID):
            framework = str(self.framework)
        else:
            framework = self.framework

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if annotation is not UNSET:
            field_dict["annotation"] = annotation
        if reference_controls is not UNSET:
            field_dict["reference_controls"] = reference_controls
        if threats is not UNSET:
            field_dict["threats"] = threats
        if display_short is not UNSET:
            field_dict["display_short"] = display_short
        if display_long is not UNSET:
            field_dict["display_long"] = display_long
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if urn is not UNSET:
            field_dict["urn"] = urn
        if ref_id is not UNSET:
            field_dict["ref_id"] = ref_id
        if provider is not UNSET:
            field_dict["provider"] = provider
        if locale is not UNSET:
            field_dict["locale"] = locale
        if default_locale is not UNSET:
            field_dict["default_locale"] = default_locale
        if parent_urn is not UNSET:
            field_dict["parent_urn"] = parent_urn
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if implementation_groups is not UNSET:
            field_dict["implementation_groups"] = implementation_groups
        if assessable is not UNSET:
            field_dict["assessable"] = assessable
        if typical_evidence is not UNSET:
            field_dict["typical_evidence"] = typical_evidence
        if question is not UNSET:
            field_dict["question"] = question
        if folder is not UNSET:
            field_dict["folder"] = folder
        if framework is not UNSET:
            field_dict["framework"] = framework

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        id: Unset | bytes = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

        description: Unset | tuple[None, bytes, str]

        if isinstance(self.description, Unset):
            description = UNSET
        elif isinstance(self.description, str):
            description = (None, str(self.description).encode(), "text/plain")
        else:
            description = (None, str(self.description).encode(), "text/plain")

        annotation: Unset | tuple[None, bytes, str]

        if isinstance(self.annotation, Unset):
            annotation = UNSET
        elif isinstance(self.annotation, str):
            annotation = (None, str(self.annotation).encode(), "text/plain")
        else:
            annotation = (None, str(self.annotation).encode(), "text/plain")

        reference_controls: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.reference_controls, Unset):
            _temp_reference_controls = self.reference_controls
            reference_controls = (None, json.dumps(_temp_reference_controls).encode(), "application/json")

        threats: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.threats, Unset):
            _temp_threats = self.threats
            threats = (None, json.dumps(_temp_threats).encode(), "application/json")

        display_short = (
            self.display_short
            if isinstance(self.display_short, Unset)
            else (None, str(self.display_short).encode(), "text/plain")
        )

        display_long = (
            self.display_long
            if isinstance(self.display_long, Unset)
            else (None, str(self.display_long).encode(), "text/plain")
        )

        created_at: Unset | bytes = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat().encode()

        updated_at: Unset | bytes = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat().encode()

        is_published = (
            self.is_published
            if isinstance(self.is_published, Unset)
            else (None, str(self.is_published).encode(), "text/plain")
        )

        urn: Unset | tuple[None, bytes, str]

        if isinstance(self.urn, Unset):
            urn = UNSET
        elif isinstance(self.urn, str):
            urn = (None, str(self.urn).encode(), "text/plain")
        else:
            urn = (None, str(self.urn).encode(), "text/plain")

        ref_id: Unset | tuple[None, bytes, str]

        if isinstance(self.ref_id, Unset):
            ref_id = UNSET
        elif isinstance(self.ref_id, str):
            ref_id = (None, str(self.ref_id).encode(), "text/plain")
        else:
            ref_id = (None, str(self.ref_id).encode(), "text/plain")

        provider: Unset | tuple[None, bytes, str]

        if isinstance(self.provider, Unset):
            provider = UNSET
        elif isinstance(self.provider, str):
            provider = (None, str(self.provider).encode(), "text/plain")
        else:
            provider = (None, str(self.provider).encode(), "text/plain")

        locale = self.locale if isinstance(self.locale, Unset) else (None, str(self.locale).encode(), "text/plain")

        default_locale = (
            self.default_locale
            if isinstance(self.default_locale, Unset)
            else (None, str(self.default_locale).encode(), "text/plain")
        )

        parent_urn: Unset | tuple[None, bytes, str]

        if isinstance(self.parent_urn, Unset):
            parent_urn = UNSET
        elif isinstance(self.parent_urn, str):
            parent_urn = (None, str(self.parent_urn).encode(), "text/plain")
        else:
            parent_urn = (None, str(self.parent_urn).encode(), "text/plain")

        order_id: Unset | tuple[None, bytes, str]

        if isinstance(self.order_id, Unset):
            order_id = UNSET
        elif isinstance(self.order_id, int):
            order_id = (None, str(self.order_id).encode(), "text/plain")
        else:
            order_id = (None, str(self.order_id).encode(), "text/plain")

        implementation_groups = (
            self.implementation_groups
            if isinstance(self.implementation_groups, Unset)
            else (None, str(self.implementation_groups).encode(), "text/plain")
        )

        assessable = (
            self.assessable
            if isinstance(self.assessable, Unset)
            else (None, str(self.assessable).encode(), "text/plain")
        )

        typical_evidence: Unset | tuple[None, bytes, str]

        if isinstance(self.typical_evidence, Unset):
            typical_evidence = UNSET
        elif isinstance(self.typical_evidence, str):
            typical_evidence = (None, str(self.typical_evidence).encode(), "text/plain")
        else:
            typical_evidence = (None, str(self.typical_evidence).encode(), "text/plain")

        question = (
            self.question if isinstance(self.question, Unset) else (None, str(self.question).encode(), "text/plain")
        )

        folder: Unset | bytes = UNSET
        if not isinstance(self.folder, Unset):
            folder = str(self.folder)

        framework: Unset | tuple[None, bytes, str]

        if isinstance(self.framework, Unset):
            framework = UNSET
        elif isinstance(self.framework, UUID):
            framework = str(self.framework)
        else:
            framework = (None, str(self.framework).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if annotation is not UNSET:
            field_dict["annotation"] = annotation
        if reference_controls is not UNSET:
            field_dict["reference_controls"] = reference_controls
        if threats is not UNSET:
            field_dict["threats"] = threats
        if display_short is not UNSET:
            field_dict["display_short"] = display_short
        if display_long is not UNSET:
            field_dict["display_long"] = display_long
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if urn is not UNSET:
            field_dict["urn"] = urn
        if ref_id is not UNSET:
            field_dict["ref_id"] = ref_id
        if provider is not UNSET:
            field_dict["provider"] = provider
        if locale is not UNSET:
            field_dict["locale"] = locale
        if default_locale is not UNSET:
            field_dict["default_locale"] = default_locale
        if parent_urn is not UNSET:
            field_dict["parent_urn"] = parent_urn
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if implementation_groups is not UNSET:
            field_dict["implementation_groups"] = implementation_groups
        if assessable is not UNSET:
            field_dict["assessable"] = assessable
        if typical_evidence is not UNSET:
            field_dict["typical_evidence"] = typical_evidence
        if question is not UNSET:
            field_dict["question"] = question
        if folder is not UNSET:
            field_dict["folder"] = folder
        if framework is not UNSET:
            field_dict["framework"] = framework

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: Unset | UUID
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_annotation(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        annotation = _parse_annotation(d.pop("annotation", UNSET))

        reference_controls = cast(list[str], d.pop("reference_controls", UNSET))

        threats = cast(list[str], d.pop("threats", UNSET))

        display_short = d.pop("display_short", UNSET)

        display_long = d.pop("display_long", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Unset | datetime.datetime
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Unset | datetime.datetime
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        is_published = d.pop("is_published", UNSET)

        def _parse_urn(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        urn = _parse_urn(d.pop("urn", UNSET))

        def _parse_ref_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        ref_id = _parse_ref_id(d.pop("ref_id", UNSET))

        def _parse_provider(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        provider = _parse_provider(d.pop("provider", UNSET))

        locale = d.pop("locale", UNSET)

        default_locale = d.pop("default_locale", UNSET)

        def _parse_parent_urn(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        parent_urn = _parse_parent_urn(d.pop("parent_urn", UNSET))

        def _parse_order_id(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        order_id = _parse_order_id(d.pop("order_id", UNSET))

        implementation_groups = d.pop("implementation_groups", UNSET)

        assessable = d.pop("assessable", UNSET)

        def _parse_typical_evidence(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        typical_evidence = _parse_typical_evidence(d.pop("typical_evidence", UNSET))

        question = d.pop("question", UNSET)

        _folder = d.pop("folder", UNSET)
        folder: Unset | UUID
        if isinstance(_folder, Unset):
            folder = UNSET
        else:
            folder = UUID(_folder)

        def _parse_framework(data: object) -> None | UUID | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                framework_type_0 = UUID(data)

                return framework_type_0
            except:  # noqa: E722
                pass
            return cast(None | UUID | Unset, data)

        framework = _parse_framework(d.pop("framework", UNSET))

        patched_requirement_node_write = cls(
            id=id,
            name=name,
            description=description,
            annotation=annotation,
            reference_controls=reference_controls,
            threats=threats,
            display_short=display_short,
            display_long=display_long,
            created_at=created_at,
            updated_at=updated_at,
            is_published=is_published,
            urn=urn,
            ref_id=ref_id,
            provider=provider,
            locale=locale,
            default_locale=default_locale,
            parent_urn=parent_urn,
            order_id=order_id,
            implementation_groups=implementation_groups,
            assessable=assessable,
            typical_evidence=typical_evidence,
            question=question,
            folder=folder,
            framework=framework,
        )

        patched_requirement_node_write.additional_properties = d
        return patched_requirement_node_write

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
