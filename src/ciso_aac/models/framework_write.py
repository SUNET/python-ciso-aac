import datetime
import json
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="FrameworkWrite")


@_attrs_define
class FrameworkWrite:
    """
    Attributes:
        id (UUID):
        name (str):
        description (Union[None, str]):
        annotation (Union[None, str]):
        folder (str):
        library (str):
        reference_controls (list[str]):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        is_published (Union[Unset, bool]):
        urn (Union[None, Unset, str]):
        ref_id (Union[None, Unset, str]):
        provider (Union[None, Unset, str]):
        locale (Union[Unset, str]):
        default_locale (Union[Unset, bool]):
        min_score (Union[Unset, int]):
        max_score (Union[Unset, int]):
        scores_definition (Union[Unset, Any]):
        implementation_groups_definition (Union[Unset, Any]):
    """

    id: UUID
    name: str
    description: None | str
    annotation: None | str
    folder: str
    library: str
    reference_controls: list[str]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    is_published: Unset | bool = UNSET
    urn: None | Unset | str = UNSET
    ref_id: None | Unset | str = UNSET
    provider: None | Unset | str = UNSET
    locale: Unset | str = UNSET
    default_locale: Unset | bool = UNSET
    min_score: Unset | int = UNSET
    max_score: Unset | int = UNSET
    scores_definition: Unset | Any = UNSET
    implementation_groups_definition: Unset | Any = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        description: None | str
        description = self.description

        annotation: None | str
        annotation = self.annotation

        folder = self.folder

        library = self.library

        reference_controls = self.reference_controls

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

        provider: None | Unset | str
        if isinstance(self.provider, Unset):
            provider = UNSET
        else:
            provider = self.provider

        locale = self.locale

        default_locale = self.default_locale

        min_score = self.min_score

        max_score = self.max_score

        scores_definition = self.scores_definition

        implementation_groups_definition = self.implementation_groups_definition

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "annotation": annotation,
                "folder": folder,
                "library": library,
                "reference_controls": reference_controls,
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
        if locale is not UNSET:
            field_dict["locale"] = locale
        if default_locale is not UNSET:
            field_dict["default_locale"] = default_locale
        if min_score is not UNSET:
            field_dict["min_score"] = min_score
        if max_score is not UNSET:
            field_dict["max_score"] = max_score
        if scores_definition is not UNSET:
            field_dict["scores_definition"] = scores_definition
        if implementation_groups_definition is not UNSET:
            field_dict["implementation_groups_definition"] = implementation_groups_definition

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        id = str(self.id)

        name = (None, str(self.name).encode(), "text/plain")

        description: tuple[None, bytes, str]

        if isinstance(self.description, str):
            description = (None, str(self.description).encode(), "text/plain")
        else:
            description = (None, str(self.description).encode(), "text/plain")

        annotation: tuple[None, bytes, str]

        if isinstance(self.annotation, str):
            annotation = (None, str(self.annotation).encode(), "text/plain")
        else:
            annotation = (None, str(self.annotation).encode(), "text/plain")

        folder = (None, str(self.folder).encode(), "text/plain")

        library = (None, str(self.library).encode(), "text/plain")

        _temp_reference_controls = self.reference_controls
        reference_controls = (None, json.dumps(_temp_reference_controls).encode(), "application/json")

        created_at = self.created_at.isoformat().encode()

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

        min_score = (
            self.min_score if isinstance(self.min_score, Unset) else (None, str(self.min_score).encode(), "text/plain")
        )

        max_score = (
            self.max_score if isinstance(self.max_score, Unset) else (None, str(self.max_score).encode(), "text/plain")
        )

        scores_definition = (
            self.scores_definition
            if isinstance(self.scores_definition, Unset)
            else (None, str(self.scores_definition).encode(), "text/plain")
        )

        implementation_groups_definition = (
            self.implementation_groups_definition
            if isinstance(self.implementation_groups_definition, Unset)
            else (None, str(self.implementation_groups_definition).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "annotation": annotation,
                "folder": folder,
                "library": library,
                "reference_controls": reference_controls,
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
        if locale is not UNSET:
            field_dict["locale"] = locale
        if default_locale is not UNSET:
            field_dict["default_locale"] = default_locale
        if min_score is not UNSET:
            field_dict["min_score"] = min_score
        if max_score is not UNSET:
            field_dict["max_score"] = max_score
        if scores_definition is not UNSET:
            field_dict["scores_definition"] = scores_definition
        if implementation_groups_definition is not UNSET:
            field_dict["implementation_groups_definition"] = implementation_groups_definition

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

        library = d.pop("library")

        reference_controls = cast(list[str], d.pop("reference_controls"))

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

        def _parse_provider(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        provider = _parse_provider(d.pop("provider", UNSET))

        locale = d.pop("locale", UNSET)

        default_locale = d.pop("default_locale", UNSET)

        min_score = d.pop("min_score", UNSET)

        max_score = d.pop("max_score", UNSET)

        scores_definition = d.pop("scores_definition", UNSET)

        implementation_groups_definition = d.pop("implementation_groups_definition", UNSET)

        framework_write = cls(
            id=id,
            name=name,
            description=description,
            annotation=annotation,
            folder=folder,
            library=library,
            reference_controls=reference_controls,
            created_at=created_at,
            updated_at=updated_at,
            is_published=is_published,
            urn=urn,
            ref_id=ref_id,
            provider=provider,
            locale=locale,
            default_locale=default_locale,
            min_score=min_score,
            max_score=max_score,
            scores_definition=scores_definition,
            implementation_groups_definition=implementation_groups_definition,
        )

        framework_write.additional_properties = d
        return framework_write

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
