import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.status_687_enum import Status687Enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="SecurityExceptionRead")


@_attrs_define
class SecurityExceptionRead:
    """
    Attributes:
        id (UUID):
        folder (str):
        owners (list[str]):
        approver (str):
        severity (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        name (str):
        description (Union[None, Unset, str]):
        ref_id (Union[None, Unset, str]):
        status (Union[Unset, Status687Enum]): * `draft` - draft
            * `in_review` - in review
            * `approved` - approved
            * `resolved` - resolved
            * `expired` - expired
            * `deprecated` - deprecated
        expiration_date (Union[None, Unset, datetime.date]): Specify when the security exception will no longer apply
        is_published (Union[Unset, bool]):
    """

    id: UUID
    folder: str
    owners: list[str]
    approver: str
    severity: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: str
    description: Union[None, Unset, str] = UNSET
    ref_id: Union[None, Unset, str] = UNSET
    status: Union[Unset, Status687Enum] = UNSET
    expiration_date: Union[None, Unset, datetime.date] = UNSET
    is_published: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        folder = self.folder

        owners = self.owners

        approver = self.approver

        severity = self.severity

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        ref_id: Union[None, Unset, str]
        if isinstance(self.ref_id, Unset):
            ref_id = UNSET
        else:
            ref_id = self.ref_id

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        expiration_date: Union[None, Unset, str]
        if isinstance(self.expiration_date, Unset):
            expiration_date = UNSET
        elif isinstance(self.expiration_date, datetime.date):
            expiration_date = self.expiration_date.isoformat()
        else:
            expiration_date = self.expiration_date

        is_published = self.is_published

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "folder": folder,
                "owners": owners,
                "approver": approver,
                "severity": severity,
                "created_at": created_at,
                "updated_at": updated_at,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if ref_id is not UNSET:
            field_dict["ref_id"] = ref_id
        if status is not UNSET:
            field_dict["status"] = status
        if expiration_date is not UNSET:
            field_dict["expiration_date"] = expiration_date
        if is_published is not UNSET:
            field_dict["is_published"] = is_published

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        folder = d.pop("folder")

        owners = cast(list[str], d.pop("owners"))

        approver = d.pop("approver")

        severity = d.pop("severity")

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

        def _parse_ref_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ref_id = _parse_ref_id(d.pop("ref_id", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, Status687Enum]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = Status687Enum(_status)

        def _parse_expiration_date(data: object) -> Union[None, Unset, datetime.date]:
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
            return cast(Union[None, Unset, datetime.date], data)

        expiration_date = _parse_expiration_date(d.pop("expiration_date", UNSET))

        is_published = d.pop("is_published", UNSET)

        security_exception_read = cls(
            id=id,
            folder=folder,
            owners=owners,
            approver=approver,
            severity=severity,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            description=description,
            ref_id=ref_id,
            status=status,
            expiration_date=expiration_date,
            is_published=is_published,
        )

        security_exception_read.additional_properties = d
        return security_exception_read

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
