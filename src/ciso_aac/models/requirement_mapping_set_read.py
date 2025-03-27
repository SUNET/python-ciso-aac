import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RequirementMappingSetRead")


@_attrs_define
class RequirementMappingSetRead:
    """
    Attributes:
        id (UUID):
        source_framework (str):
        target_framework (str):
        library (str):
        folder (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        is_published (Union[Unset, bool]):
        urn (Union[None, Unset, str]):
        ref_id (Union[None, Unset, str]):
        provider (Union[None, Unset, str]):
        name (Union[None, Unset, str]):
        description (Union[None, Unset, str]):
        annotation (Union[None, Unset, str]):
        translations (Union[Unset, Any]):
    """

    id: UUID
    source_framework: str
    target_framework: str
    library: str
    folder: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    is_published: Union[Unset, bool] = UNSET
    urn: Union[None, Unset, str] = UNSET
    ref_id: Union[None, Unset, str] = UNSET
    provider: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    annotation: Union[None, Unset, str] = UNSET
    translations: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        source_framework = self.source_framework

        target_framework = self.target_framework

        library = self.library

        folder = self.folder

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        is_published = self.is_published

        urn: Union[None, Unset, str]
        if isinstance(self.urn, Unset):
            urn = UNSET
        else:
            urn = self.urn

        ref_id: Union[None, Unset, str]
        if isinstance(self.ref_id, Unset):
            ref_id = UNSET
        else:
            ref_id = self.ref_id

        provider: Union[None, Unset, str]
        if isinstance(self.provider, Unset):
            provider = UNSET
        else:
            provider = self.provider

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        annotation: Union[None, Unset, str]
        if isinstance(self.annotation, Unset):
            annotation = UNSET
        else:
            annotation = self.annotation

        translations = self.translations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "source_framework": source_framework,
                "target_framework": target_framework,
                "library": library,
                "folder": folder,
                "created_at": created_at,
                "updated_at": updated_at,
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
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if annotation is not UNSET:
            field_dict["annotation"] = annotation
        if translations is not UNSET:
            field_dict["translations"] = translations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        source_framework = d.pop("source_framework")

        target_framework = d.pop("target_framework")

        library = d.pop("library")

        folder = d.pop("folder")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        is_published = d.pop("is_published", UNSET)

        def _parse_urn(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        urn = _parse_urn(d.pop("urn", UNSET))

        def _parse_ref_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ref_id = _parse_ref_id(d.pop("ref_id", UNSET))

        def _parse_provider(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        provider = _parse_provider(d.pop("provider", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_annotation(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        annotation = _parse_annotation(d.pop("annotation", UNSET))

        translations = d.pop("translations", UNSET)

        requirement_mapping_set_read = cls(
            id=id,
            source_framework=source_framework,
            target_framework=target_framework,
            library=library,
            folder=folder,
            created_at=created_at,
            updated_at=updated_at,
            is_published=is_published,
            urn=urn,
            ref_id=ref_id,
            provider=provider,
            name=name,
            description=description,
            annotation=annotation,
            translations=translations,
        )

        requirement_mapping_set_read.additional_properties = d
        return requirement_mapping_set_read

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
