import datetime
import json
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedEvidenceWrite")


@_attrs_define
class PatchedEvidenceWrite:
    """
    Attributes:
        id (Union[Unset, UUID]):
        applied_controls (Union[Unset, list[UUID]]):
        requirement_assessments (Union[Unset, list[UUID]]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
        name (Union[Unset, str]):
        description (Union[None, Unset, str]):
        attachment (Union[None, Unset, str]): Attachment for evidence (eg. screenshot, log file, etc.)
        link (Union[None, Unset, str]): Link to the evidence (eg. Jira ticket, etc.)
        is_published (Union[Unset, bool]):
        folder (Union[Unset, UUID]):
    """

    id: Unset | UUID = UNSET
    applied_controls: Unset | list[UUID] = UNSET
    requirement_assessments: Unset | list[UUID] = UNSET
    created_at: Unset | datetime.datetime = UNSET
    updated_at: Unset | datetime.datetime = UNSET
    name: Unset | str = UNSET
    description: None | Unset | str = UNSET
    attachment: None | Unset | str = UNSET
    link: None | Unset | str = UNSET
    is_published: Unset | bool = UNSET
    folder: Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: Unset | str = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

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

        created_at: Unset | str = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Unset | str = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        name = self.name

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
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if applied_controls is not UNSET:
            field_dict["applied_controls"] = applied_controls
        if requirement_assessments is not UNSET:
            field_dict["requirement_assessments"] = requirement_assessments
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if name is not UNSET:
            field_dict["name"] = name
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
        id: Unset | bytes = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

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

        created_at: Unset | bytes = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat().encode()

        updated_at: Unset | bytes = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat().encode()

        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

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

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if applied_controls is not UNSET:
            field_dict["applied_controls"] = applied_controls
        if requirement_assessments is not UNSET:
            field_dict["requirement_assessments"] = requirement_assessments
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if name is not UNSET:
            field_dict["name"] = name
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
        _id = d.pop("id", UNSET)
        id: Unset | UUID
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

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

        name = d.pop("name", UNSET)

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

        patched_evidence_write = cls(
            id=id,
            applied_controls=applied_controls,
            requirement_assessments=requirement_assessments,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            description=description,
            attachment=attachment,
            link=link,
            is_published=is_published,
            folder=folder,
        )

        patched_evidence_write.additional_properties = d
        return patched_evidence_write

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
