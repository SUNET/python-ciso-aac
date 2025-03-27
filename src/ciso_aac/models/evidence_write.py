import datetime
import json
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="EvidenceWrite")


@_attrs_define
class EvidenceWrite:
    """
    Attributes:
        id (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        name (str):
        applied_controls (Union[Unset, list[UUID]]):
        requirement_assessments (Union[Unset, list[UUID]]):
        description (Union[None, Unset, str]):
        attachment (Union[None, Unset, str]): Attachment for evidence (eg. screenshot, log file, etc.)
        link (Union[None, Unset, str]): Link to the evidence (eg. Jira ticket, etc.)
        is_published (Union[Unset, bool]):
        folder (Union[Unset, UUID]):
    """

    id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: str
    applied_controls: Unset | list[UUID] = UNSET
    requirement_assessments: Unset | list[UUID] = UNSET
    description: None | Unset | str = UNSET
    attachment: None | Unset | str = UNSET
    link: None | Unset | str = UNSET
    is_published: Unset | bool = UNSET
    folder: Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        name = self.name

        applied_controls: Unset | list[str] = UNSET
        if not isinstance(self.applied_controls, Unset):
            applied_controls = []
            for applied_controls_item_data in self.applied_controls:
                applied_controls_item = str(applied_controls_item_data)
                applied_controls.append(applied_controls_item)

        requirement_assessments: Unset | list[str] = UNSET
        if not isinstance(self.requirement_assessments, Unset):
            requirement_assessments = []
            for requirement_assessments_item_data in self.requirement_assessments:
                requirement_assessments_item = str(requirement_assessments_item_data)
                requirement_assessments.append(requirement_assessments_item)

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        attachment: None | Unset | str
        if isinstance(self.attachment, Unset):
            attachment = UNSET
        else:
            attachment = self.attachment

        link: None | Unset | str
        if isinstance(self.link, Unset):
            link = UNSET
        else:
            link = self.link

        is_published = self.is_published

        folder: Unset | str = UNSET
        if not isinstance(self.folder, Unset):
            folder = str(self.folder)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "updated_at": updated_at,
                "name": name,
            }
        )
        if applied_controls is not UNSET:
            field_dict["applied_controls"] = applied_controls
        if requirement_assessments is not UNSET:
            field_dict["requirement_assessments"] = requirement_assessments
        if description is not UNSET:
            field_dict["description"] = description
        if attachment is not UNSET:
            field_dict["attachment"] = attachment
        if link is not UNSET:
            field_dict["link"] = link
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if folder is not UNSET:
            field_dict["folder"] = folder

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        id = str(self.id)

        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        name = (None, str(self.name).encode(), "text/plain")

        applied_controls: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.applied_controls, Unset):
            _temp_applied_controls = []
            for applied_controls_item_data in self.applied_controls:
                applied_controls_item = str(applied_controls_item_data)
                _temp_applied_controls.append(applied_controls_item)
            applied_controls = (None, json.dumps(_temp_applied_controls).encode(), "application/json")

        requirement_assessments: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.requirement_assessments, Unset):
            _temp_requirement_assessments = []
            for requirement_assessments_item_data in self.requirement_assessments:
                requirement_assessments_item = str(requirement_assessments_item_data)
                _temp_requirement_assessments.append(requirement_assessments_item)
            requirement_assessments = (None, json.dumps(_temp_requirement_assessments).encode(), "application/json")

        description: Unset | tuple[None, bytes, str]

        if isinstance(self.description, Unset):
            description = UNSET
        elif isinstance(self.description, str):
            description = (None, str(self.description).encode(), "text/plain")
        else:
            description = (None, str(self.description).encode(), "text/plain")

        attachment: Unset | tuple[None, bytes, str]

        if isinstance(self.attachment, Unset):
            attachment = UNSET
        elif isinstance(self.attachment, str):
            attachment = (None, str(self.attachment).encode(), "text/plain")
        else:
            attachment = (None, str(self.attachment).encode(), "text/plain")

        link: Unset | tuple[None, bytes, str]

        if isinstance(self.link, Unset):
            link = UNSET
        elif isinstance(self.link, str):
            link = (None, str(self.link).encode(), "text/plain")
        else:
            link = (None, str(self.link).encode(), "text/plain")

        is_published = (
            self.is_published
            if isinstance(self.is_published, Unset)
            else (None, str(self.is_published).encode(), "text/plain")
        )

        folder: Unset | bytes = UNSET
        if not isinstance(self.folder, Unset):
            folder = str(self.folder)

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "updated_at": updated_at,
                "name": name,
            }
        )
        if applied_controls is not UNSET:
            field_dict["applied_controls"] = applied_controls
        if requirement_assessments is not UNSET:
            field_dict["requirement_assessments"] = requirement_assessments
        if description is not UNSET:
            field_dict["description"] = description
        if attachment is not UNSET:
            field_dict["attachment"] = attachment
        if link is not UNSET:
            field_dict["link"] = link
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if folder is not UNSET:
            field_dict["folder"] = folder

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        name = d.pop("name")

        applied_controls = []
        _applied_controls = d.pop("applied_controls", UNSET)
        for applied_controls_item_data in _applied_controls or []:
            applied_controls_item = UUID(applied_controls_item_data)

            applied_controls.append(applied_controls_item)

        requirement_assessments = []
        _requirement_assessments = d.pop("requirement_assessments", UNSET)
        for requirement_assessments_item_data in _requirement_assessments or []:
            requirement_assessments_item = UUID(requirement_assessments_item_data)

            requirement_assessments.append(requirement_assessments_item)

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_attachment(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        attachment = _parse_attachment(d.pop("attachment", UNSET))

        def _parse_link(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        link = _parse_link(d.pop("link", UNSET))

        is_published = d.pop("is_published", UNSET)

        _folder = d.pop("folder", UNSET)
        folder: Unset | UUID
        if isinstance(_folder, Unset):
            folder = UNSET
        else:
            folder = UUID(_folder)

        evidence_write = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            applied_controls=applied_controls,
            requirement_assessments=requirement_assessments,
            description=description,
            attachment=attachment,
            link=link,
            is_published=is_published,
            folder=folder,
        )

        evidence_write.additional_properties = d
        return evidence_write

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
