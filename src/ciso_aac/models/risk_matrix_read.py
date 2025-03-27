import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define, field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RiskMatrixRead")


@_attrs_define
class RiskMatrixRead:
    """
    Attributes:
        id (UUID):
        name (str):
        description (Union[None, str]):
        annotation (Union[None, str]):
        folder (str):
        json_definition (Any):
        library (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        is_published (Union[Unset, bool]):
        urn (Union[None, Unset, str]):
        ref_id (Union[None, Unset, str]):
        locale (Union[Unset, str]):
        default_locale (Union[Unset, bool]):
        is_enabled (Union[Unset, bool]): If the risk matrix is set as disabled, it will not be available for selection
            for new risk assessments.
        provider (Union[None, Unset, str]):
    """

    id: UUID
    name: str
    description: None | str
    annotation: None | str
    folder: str
    json_definition: Any
    library: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    is_published: Unset | bool = UNSET
    urn: None | Unset | str = UNSET
    ref_id: None | Unset | str = UNSET
    locale: Unset | str = UNSET
    default_locale: Unset | bool = UNSET
    is_enabled: Unset | bool = UNSET
    provider: None | Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        description: None | str
        description = self.description

        annotation: None | str
        annotation = self.annotation

        folder = self.folder

        json_definition = self.json_definition

        library = self.library

        created_at = self.created_at.isoformat()

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

        locale = self.locale

        default_locale = self.default_locale

        is_enabled = self.is_enabled

        provider: None | Unset | str
        if isinstance(self.provider, Unset):
            provider = UNSET
        else:
            provider = self.provider

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "annotation": annotation,
                "folder": folder,
                "json_definition": json_definition,
                "library": library,
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
        if locale is not UNSET:
            field_dict["locale"] = locale
        if default_locale is not UNSET:
            field_dict["default_locale"] = default_locale
        if is_enabled is not UNSET:
            field_dict["is_enabled"] = is_enabled
        if provider is not UNSET:
            field_dict["provider"] = provider

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

        folder = d.pop("folder")

        json_definition = d.pop("json_definition")

        library = d.pop("library")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

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

        locale = d.pop("locale", UNSET)

        default_locale = d.pop("default_locale", UNSET)

        is_enabled = d.pop("is_enabled", UNSET)

        def _parse_provider(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        provider = _parse_provider(d.pop("provider", UNSET))

        risk_matrix_read = cls(
            id=id,
            name=name,
            description=description,
            annotation=annotation,
            folder=folder,
            json_definition=json_definition,
            library=library,
            created_at=created_at,
            updated_at=updated_at,
            is_published=is_published,
            urn=urn,
            ref_id=ref_id,
            locale=locale,
            default_locale=default_locale,
            is_enabled=is_enabled,
            provider=provider,
        )

        risk_matrix_read.additional_properties = d
        return risk_matrix_read

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
