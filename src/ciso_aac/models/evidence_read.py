import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="EvidenceRead")


@_attrs_define
class EvidenceRead:
    """
    Attributes:
        id (UUID):
        attachment (str):
        size (str):
        folder (str):
        applied_controls (list[str]):
        requirement_assessments (list[str]):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        name (str):
        description (Union[None, Unset, str]):
        link (Union[None, Unset, str]): Link to the evidence (eg. Jira ticket, etc.)
        is_published (Union[Unset, bool]):
    """

    id: UUID
    attachment: str
    size: str
    folder: str
    applied_controls: list[str]
    requirement_assessments: list[str]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: str
    description: Union[None, Unset, str] = UNSET
    link: Union[None, Unset, str] = UNSET
    is_published: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        attachment = self.attachment

        size = self.size

        folder = self.folder

        applied_controls = self.applied_controls

        requirement_assessments = self.requirement_assessments

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        link: Union[None, Unset, str]
        if isinstance(self.link, Unset):
            link = UNSET
        else:
            link = self.link

        is_published = self.is_published

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "attachment": attachment,
                "size": size,
                "folder": folder,
                "applied_controls": applied_controls,
                "requirement_assessments": requirement_assessments,
                "created_at": created_at,
                "updated_at": updated_at,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if link is not UNSET:
            field_dict["link"] = link
        if is_published is not UNSET:
            field_dict["is_published"] = is_published

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        attachment = d.pop("attachment")

        size = d.pop("size")

        folder = d.pop("folder")

        applied_controls = cast(list[str], d.pop("applied_controls"))

        requirement_assessments = cast(list[str], d.pop("requirement_assessments"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        name = d.pop("name")

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_link(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        link = _parse_link(d.pop("link", UNSET))

        is_published = d.pop("is_published", UNSET)

        evidence_read = cls(
            id=id,
            attachment=attachment,
            size=size,
            folder=folder,
            applied_controls=applied_controls,
            requirement_assessments=requirement_assessments,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            description=description,
            link=link,
            is_published=is_published,
        )

        evidence_read.additional_properties = d
        return evidence_read

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
