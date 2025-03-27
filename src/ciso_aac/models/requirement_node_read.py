import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RequirementNodeRead")


@_attrs_define
class RequirementNodeRead:
    """
    Attributes:
        id (UUID):
        name (str):
        description (Union[None, str]):
        annotation (Union[None, str]):
        reference_controls (list[str]):
        threats (list[str]):
        display_short (str):
        display_long (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        assessable (bool):
        is_published (Union[Unset, bool]):
        urn (Union[None, Unset, str]):
        ref_id (Union[None, Unset, str]):
        provider (Union[None, Unset, str]):
        locale (Union[Unset, str]):
        default_locale (Union[Unset, bool]):
        parent_urn (Union[None, Unset, str]):
        order_id (Union[None, Unset, int]):
        implementation_groups (Union[Unset, Any]):
        typical_evidence (Union[None, Unset, str]):
        question (Union[Unset, Any]):
        folder (Union[Unset, UUID]):
        framework (Union[None, UUID, Unset]):
    """

    id: UUID
    name: str
    description: None | str
    annotation: None | str
    reference_controls: list[str]
    threats: list[str]
    display_short: str
    display_long: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    assessable: bool
    is_published: Unset | bool = UNSET
    urn: None | Unset | str = UNSET
    ref_id: None | Unset | str = UNSET
    provider: None | Unset | str = UNSET
    locale: Unset | str = UNSET
    default_locale: Unset | bool = UNSET
    parent_urn: None | Unset | str = UNSET
    order_id: None | Unset | int = UNSET
    implementation_groups: Unset | Any = UNSET
    typical_evidence: None | Unset | str = UNSET
    question: Unset | Any = UNSET
    folder: Unset | UUID = UNSET
    framework: None | UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        description: None | str
        description = self.description

        annotation: None | str
        annotation = self.annotation

        reference_controls = self.reference_controls

        threats = self.threats

        display_short = self.display_short

        display_long = self.display_long

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        assessable = self.assessable

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
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "annotation": annotation,
                "reference_controls": reference_controls,
                "threats": threats,
                "display_short": display_short,
                "display_long": display_long,
                "created_at": created_at,
                "updated_at": updated_at,
                "assessable": assessable,
            }
        )
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
        id = UUID(d.pop("id"))

        name = d.pop("name")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_annotation(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        annotation = _parse_annotation(d.pop("annotation"))

        reference_controls = cast(list[str], d.pop("reference_controls"))

        threats = cast(list[str], d.pop("threats"))

        display_short = d.pop("display_short")

        display_long = d.pop("display_long")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        assessable = d.pop("assessable")

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

        requirement_node_read = cls(
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
            assessable=assessable,
            is_published=is_published,
            urn=urn,
            ref_id=ref_id,
            provider=provider,
            locale=locale,
            default_locale=default_locale,
            parent_urn=parent_urn,
            order_id=order_id,
            implementation_groups=implementation_groups,
            typical_evidence=typical_evidence,
            question=question,
            folder=folder,
            framework=framework,
        )

        requirement_node_read.additional_properties = d
        return requirement_node_read

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
