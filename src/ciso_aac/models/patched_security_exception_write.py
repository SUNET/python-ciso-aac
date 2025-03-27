import datetime
import json
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.severity_enum import SeverityEnum
from ..models.status_687_enum import Status687Enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedSecurityExceptionWrite")


@_attrs_define
class PatchedSecurityExceptionWrite:
    """
    Attributes:
        id (Union[Unset, UUID]):
        requirement_assessments (Union[Unset, list[UUID]]):
        applied_controls (Union[Unset, list[UUID]]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
        name (Union[Unset, str]):
        description (Union[None, Unset, str]):
        ref_id (Union[None, Unset, str]):
        severity (Union[Unset, SeverityEnum]): * `-1` - undefined
            * `0` - low
            * `1` - medium
            * `2` - high
            * `3` - critical
        status (Union[Unset, Status687Enum]): * `draft` - draft
            * `in_review` - in review
            * `approved` - approved
            * `resolved` - resolved
            * `expired` - expired
            * `deprecated` - deprecated
        expiration_date (Union[None, Unset, datetime.date]): Specify when the security exception will no longer apply
        is_published (Union[Unset, bool]):
        folder (Union[Unset, UUID]):
        approver (Union[None, UUID, Unset]):
        owners (Union[Unset, list[UUID]]):
    """

    id: Unset | UUID = UNSET
    requirement_assessments: Unset | list[UUID] = UNSET
    applied_controls: Unset | list[UUID] = UNSET
    created_at: Unset | datetime.datetime = UNSET
    updated_at: Unset | datetime.datetime = UNSET
    name: Unset | str = UNSET
    description: None | Unset | str = UNSET
    ref_id: None | Unset | str = UNSET
    severity: Unset | SeverityEnum = UNSET
    status: Unset | Status687Enum = UNSET
    expiration_date: None | Unset | datetime.date = UNSET
    is_published: Unset | bool = UNSET
    folder: Unset | UUID = UNSET
    approver: None | UUID | Unset = UNSET
    owners: Unset | list[UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: Unset | str = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        requirement_assessments: Unset | list[str] = UNSET
        if not isinstance(self.requirement_assessments, Unset):
            requirement_assessments = []
            for requirement_assessments_item_data in self.requirement_assessments:
                requirement_assessments_item = str(requirement_assessments_item_data)
                requirement_assessments.append(requirement_assessments_item)

        applied_controls: Unset | list[str] = UNSET
        if not isinstance(self.applied_controls, Unset):
            applied_controls = []
            for applied_controls_item_data in self.applied_controls:
                applied_controls_item = str(applied_controls_item_data)
                applied_controls.append(applied_controls_item)

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

        ref_id: None | Unset | str
        if isinstance(self.ref_id, Unset):
            ref_id = UNSET
        else:
            ref_id = self.ref_id

        severity: Unset | int = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        status: Unset | str = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        expiration_date: None | Unset | str
        if isinstance(self.expiration_date, Unset):
            expiration_date = UNSET
        elif isinstance(self.expiration_date, datetime.date):
            expiration_date = self.expiration_date.isoformat()
        else:
            expiration_date = self.expiration_date

        is_published = self.is_published

        folder: Unset | str = UNSET
        if not isinstance(self.folder, Unset):
            folder = str(self.folder)

        approver: None | Unset | str
        if isinstance(self.approver, Unset):
            approver = UNSET
        elif isinstance(self.approver, UUID):
            approver = str(self.approver)
        else:
            approver = self.approver

        owners: Unset | list[str] = UNSET
        if not isinstance(self.owners, Unset):
            owners = []
            for owners_item_data in self.owners:
                owners_item = str(owners_item_data)
                owners.append(owners_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if requirement_assessments is not UNSET:
            field_dict["requirement_assessments"] = requirement_assessments
        if applied_controls is not UNSET:
            field_dict["applied_controls"] = applied_controls
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if ref_id is not UNSET:
            field_dict["ref_id"] = ref_id
        if severity is not UNSET:
            field_dict["severity"] = severity
        if status is not UNSET:
            field_dict["status"] = status
        if expiration_date is not UNSET:
            field_dict["expiration_date"] = expiration_date
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if folder is not UNSET:
            field_dict["folder"] = folder
        if approver is not UNSET:
            field_dict["approver"] = approver
        if owners is not UNSET:
            field_dict["owners"] = owners

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        id: Unset | bytes = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        requirement_assessments: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.requirement_assessments, Unset):
            _temp_requirement_assessments = []
            for requirement_assessments_item_data in self.requirement_assessments:
                requirement_assessments_item = str(requirement_assessments_item_data)
                _temp_requirement_assessments.append(requirement_assessments_item)
            requirement_assessments = (None, json.dumps(_temp_requirement_assessments).encode(), "application/json")

        applied_controls: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.applied_controls, Unset):
            _temp_applied_controls = []
            for applied_controls_item_data in self.applied_controls:
                applied_controls_item = str(applied_controls_item_data)
                _temp_applied_controls.append(applied_controls_item)
            applied_controls = (None, json.dumps(_temp_applied_controls).encode(), "application/json")

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

        ref_id: Unset | tuple[None, bytes, str]

        if isinstance(self.ref_id, Unset):
            ref_id = UNSET
        elif isinstance(self.ref_id, str):
            ref_id = (None, str(self.ref_id).encode(), "text/plain")
        else:
            ref_id = (None, str(self.ref_id).encode(), "text/plain")

        severity: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.severity, Unset):
            severity = (None, str(self.severity.value).encode(), "text/plain")

        status: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.status, Unset):
            status = (None, str(self.status.value).encode(), "text/plain")

        expiration_date: Unset | tuple[None, bytes, str]

        if isinstance(self.expiration_date, Unset):
            expiration_date = UNSET
        elif isinstance(self.expiration_date, datetime.date):
            expiration_date = self.expiration_date.isoformat().encode()
        else:
            expiration_date = (None, str(self.expiration_date).encode(), "text/plain")

        is_published = (
            self.is_published
            if isinstance(self.is_published, Unset)
            else (None, str(self.is_published).encode(), "text/plain")
        )

        folder: Unset | bytes = UNSET
        if not isinstance(self.folder, Unset):
            folder = str(self.folder)

        approver: Unset | tuple[None, bytes, str]

        if isinstance(self.approver, Unset):
            approver = UNSET
        elif isinstance(self.approver, UUID):
            approver = str(self.approver)
        else:
            approver = (None, str(self.approver).encode(), "text/plain")

        owners: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.owners, Unset):
            _temp_owners = []
            for owners_item_data in self.owners:
                owners_item = str(owners_item_data)
                _temp_owners.append(owners_item)
            owners = (None, json.dumps(_temp_owners).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if requirement_assessments is not UNSET:
            field_dict["requirement_assessments"] = requirement_assessments
        if applied_controls is not UNSET:
            field_dict["applied_controls"] = applied_controls
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if ref_id is not UNSET:
            field_dict["ref_id"] = ref_id
        if severity is not UNSET:
            field_dict["severity"] = severity
        if status is not UNSET:
            field_dict["status"] = status
        if expiration_date is not UNSET:
            field_dict["expiration_date"] = expiration_date
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if folder is not UNSET:
            field_dict["folder"] = folder
        if approver is not UNSET:
            field_dict["approver"] = approver
        if owners is not UNSET:
            field_dict["owners"] = owners

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

        requirement_assessments = []
        _requirement_assessments = d.pop("requirement_assessments", UNSET)
        for requirement_assessments_item_data in _requirement_assessments or []:
            requirement_assessments_item = UUID(requirement_assessments_item_data)

            requirement_assessments.append(requirement_assessments_item)

        applied_controls = []
        _applied_controls = d.pop("applied_controls", UNSET)
        for applied_controls_item_data in _applied_controls or []:
            applied_controls_item = UUID(applied_controls_item_data)

            applied_controls.append(applied_controls_item)

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

        def _parse_ref_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        ref_id = _parse_ref_id(d.pop("ref_id", UNSET))

        _severity = d.pop("severity", UNSET)
        severity: Unset | SeverityEnum
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = SeverityEnum(_severity)

        _status = d.pop("status", UNSET)
        status: Unset | Status687Enum
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = Status687Enum(_status)

        def _parse_expiration_date(data: object) -> None | Unset | datetime.date:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expiration_date_type_0 = isoparse(data).date()

                return expiration_date_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | datetime.date, data)

        expiration_date = _parse_expiration_date(d.pop("expiration_date", UNSET))

        is_published = d.pop("is_published", UNSET)

        _folder = d.pop("folder", UNSET)
        folder: Unset | UUID
        if isinstance(_folder, Unset):
            folder = UNSET
        else:
            folder = UUID(_folder)

        def _parse_approver(data: object) -> None | UUID | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approver_type_0 = UUID(data)

                return approver_type_0
            except:  # noqa: E722
                pass
            return cast(None | UUID | Unset, data)

        approver = _parse_approver(d.pop("approver", UNSET))

        owners = []
        _owners = d.pop("owners", UNSET)
        for owners_item_data in _owners or []:
            owners_item = UUID(owners_item_data)

            owners.append(owners_item)

        patched_security_exception_write = cls(
            id=id,
            requirement_assessments=requirement_assessments,
            applied_controls=applied_controls,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            description=description,
            ref_id=ref_id,
            severity=severity,
            status=status,
            expiration_date=expiration_date,
            is_published=is_published,
            folder=folder,
            approver=approver,
            owners=owners,
        )

        patched_security_exception_write.additional_properties = d
        return patched_security_exception_write

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
