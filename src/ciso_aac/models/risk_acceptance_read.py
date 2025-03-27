import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RiskAcceptanceRead")


@_attrs_define
class RiskAcceptanceRead:
    """
    Attributes:
        id (UUID):
        folder (str):
        risk_scenarios (list[str]):
        approver (str):
        state (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        name (str):
        is_published (Union[Unset, bool]):
        description (Union[None, Unset, str]):
        expiry_date (Union[None, Unset, datetime.date]): Specify when the risk acceptance will no longer apply
        accepted_at (Union[None, Unset, datetime.datetime]):
        rejected_at (Union[None, Unset, datetime.datetime]):
        revoked_at (Union[None, Unset, datetime.datetime]):
        justification (Union[None, Unset, str]):
    """

    id: UUID
    folder: str
    risk_scenarios: list[str]
    approver: str
    state: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: str
    is_published: Unset | bool = UNSET
    description: None | Unset | str = UNSET
    expiry_date: None | Unset | datetime.date = UNSET
    accepted_at: None | Unset | datetime.datetime = UNSET
    rejected_at: None | Unset | datetime.datetime = UNSET
    revoked_at: None | Unset | datetime.datetime = UNSET
    justification: None | Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        folder = self.folder

        risk_scenarios = self.risk_scenarios

        approver = self.approver

        state = self.state

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        name = self.name

        is_published = self.is_published

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        expiry_date: None | Unset | str
        if isinstance(self.expiry_date, Unset):
            expiry_date = UNSET
        elif isinstance(self.expiry_date, datetime.date):
            expiry_date = self.expiry_date.isoformat()
        else:
            expiry_date = self.expiry_date

        accepted_at: None | Unset | str
        if isinstance(self.accepted_at, Unset):
            accepted_at = UNSET
        elif isinstance(self.accepted_at, datetime.datetime):
            accepted_at = self.accepted_at.isoformat()
        else:
            accepted_at = self.accepted_at

        rejected_at: None | Unset | str
        if isinstance(self.rejected_at, Unset):
            rejected_at = UNSET
        elif isinstance(self.rejected_at, datetime.datetime):
            rejected_at = self.rejected_at.isoformat()
        else:
            rejected_at = self.rejected_at

        revoked_at: None | Unset | str
        if isinstance(self.revoked_at, Unset):
            revoked_at = UNSET
        elif isinstance(self.revoked_at, datetime.datetime):
            revoked_at = self.revoked_at.isoformat()
        else:
            revoked_at = self.revoked_at

        justification: None | Unset | str
        if isinstance(self.justification, Unset):
            justification = UNSET
        else:
            justification = self.justification

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "folder": folder,
                "risk_scenarios": risk_scenarios,
                "approver": approver,
                "state": state,
                "created_at": created_at,
                "updated_at": updated_at,
                "name": name,
            }
        )
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if description is not UNSET:
            field_dict["description"] = description
        if expiry_date is not UNSET:
            field_dict["expiry_date"] = expiry_date
        if accepted_at is not UNSET:
            field_dict["accepted_at"] = accepted_at
        if rejected_at is not UNSET:
            field_dict["rejected_at"] = rejected_at
        if revoked_at is not UNSET:
            field_dict["revoked_at"] = revoked_at
        if justification is not UNSET:
            field_dict["justification"] = justification

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        folder = d.pop("folder")

        risk_scenarios = cast(list[str], d.pop("risk_scenarios"))

        approver = d.pop("approver")

        state = d.pop("state")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        name = d.pop("name")

        is_published = d.pop("is_published", UNSET)

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_expiry_date(data: object) -> None | Unset | datetime.date:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expiry_date_type_0 = isoparse(data).date()

                return expiry_date_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | datetime.date, data)

        expiry_date = _parse_expiry_date(d.pop("expiry_date", UNSET))

        def _parse_accepted_at(data: object) -> None | Unset | datetime.datetime:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                accepted_at_type_0 = isoparse(data)

                return accepted_at_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | datetime.datetime, data)

        accepted_at = _parse_accepted_at(d.pop("accepted_at", UNSET))

        def _parse_rejected_at(data: object) -> None | Unset | datetime.datetime:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rejected_at_type_0 = isoparse(data)

                return rejected_at_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | datetime.datetime, data)

        rejected_at = _parse_rejected_at(d.pop("rejected_at", UNSET))

        def _parse_revoked_at(data: object) -> None | Unset | datetime.datetime:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                revoked_at_type_0 = isoparse(data)

                return revoked_at_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | datetime.datetime, data)

        revoked_at = _parse_revoked_at(d.pop("revoked_at", UNSET))

        def _parse_justification(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        justification = _parse_justification(d.pop("justification", UNSET))

        risk_acceptance_read = cls(
            id=id,
            folder=folder,
            risk_scenarios=risk_scenarios,
            approver=approver,
            state=state,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            is_published=is_published,
            description=description,
            expiry_date=expiry_date,
            accepted_at=accepted_at,
            rejected_at=rejected_at,
            revoked_at=revoked_at,
            justification=justification,
        )

        risk_acceptance_read.additional_properties = d
        return risk_acceptance_read

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
