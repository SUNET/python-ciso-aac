import datetime
import json
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RiskAcceptanceWrite")


@_attrs_define
class RiskAcceptanceWrite:
    """
    Attributes:
        id (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        name (str):
        risk_scenarios (list[UUID]): Select the risk scenarios to be accepted, attention they must be part of the chosen
            domain
        is_published (Union[Unset, bool]):
        description (Union[None, Unset, str]):
        expiry_date (Union[None, Unset, datetime.date]): Specify when the risk acceptance will no longer apply
        justification (Union[None, Unset, str]):
        folder (Union[Unset, UUID]):
        approver (Union[None, UUID, Unset]): Risk owner and approver identity
    """

    id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: str
    risk_scenarios: list[UUID]
    is_published: Union[Unset, bool] = UNSET
    description: Union[None, Unset, str] = UNSET
    expiry_date: Union[None, Unset, datetime.date] = UNSET
    justification: Union[None, Unset, str] = UNSET
    folder: Union[Unset, UUID] = UNSET
    approver: Union[None, UUID, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        name = self.name

        risk_scenarios = []
        for risk_scenarios_item_data in self.risk_scenarios:
            risk_scenarios_item = str(risk_scenarios_item_data)
            risk_scenarios.append(risk_scenarios_item)

        is_published = self.is_published

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        expiry_date: Union[None, Unset, str]
        if isinstance(self.expiry_date, Unset):
            expiry_date = UNSET
        elif isinstance(self.expiry_date, datetime.date):
            expiry_date = self.expiry_date.isoformat()
        else:
            expiry_date = self.expiry_date

        justification: Union[None, Unset, str]
        if isinstance(self.justification, Unset):
            justification = UNSET
        else:
            justification = self.justification

        folder: Union[Unset, str] = UNSET
        if not isinstance(self.folder, Unset):
            folder = str(self.folder)

        approver: Union[None, Unset, str]
        if isinstance(self.approver, Unset):
            approver = UNSET
        elif isinstance(self.approver, UUID):
            approver = str(self.approver)
        else:
            approver = self.approver

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "updated_at": updated_at,
                "name": name,
                "risk_scenarios": risk_scenarios,
            }
        )
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if description is not UNSET:
            field_dict["description"] = description
        if expiry_date is not UNSET:
            field_dict["expiry_date"] = expiry_date
        if justification is not UNSET:
            field_dict["justification"] = justification
        if folder is not UNSET:
            field_dict["folder"] = folder
        if approver is not UNSET:
            field_dict["approver"] = approver

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        id = str(self.id)

        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        name = (None, str(self.name).encode(), "text/plain")

        _temp_risk_scenarios = []
        for risk_scenarios_item_data in self.risk_scenarios:
            risk_scenarios_item = str(risk_scenarios_item_data)
            _temp_risk_scenarios.append(risk_scenarios_item)
        risk_scenarios = (None, json.dumps(_temp_risk_scenarios).encode(), "application/json")

        is_published = (
            self.is_published
            if isinstance(self.is_published, Unset)
            else (None, str(self.is_published).encode(), "text/plain")
        )

        description: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.description, Unset):
            description = UNSET
        elif isinstance(self.description, str):
            description = (None, str(self.description).encode(), "text/plain")
        else:
            description = (None, str(self.description).encode(), "text/plain")

        expiry_date: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.expiry_date, Unset):
            expiry_date = UNSET
        elif isinstance(self.expiry_date, datetime.date):
            expiry_date = self.expiry_date.isoformat().encode()
        else:
            expiry_date = (None, str(self.expiry_date).encode(), "text/plain")

        justification: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.justification, Unset):
            justification = UNSET
        elif isinstance(self.justification, str):
            justification = (None, str(self.justification).encode(), "text/plain")
        else:
            justification = (None, str(self.justification).encode(), "text/plain")

        folder: Union[Unset, bytes] = UNSET
        if not isinstance(self.folder, Unset):
            folder = str(self.folder)

        approver: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.approver, Unset):
            approver = UNSET
        elif isinstance(self.approver, UUID):
            approver = str(self.approver)
        else:
            approver = (None, str(self.approver).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "updated_at": updated_at,
                "name": name,
                "risk_scenarios": risk_scenarios,
            }
        )
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if description is not UNSET:
            field_dict["description"] = description
        if expiry_date is not UNSET:
            field_dict["expiry_date"] = expiry_date
        if justification is not UNSET:
            field_dict["justification"] = justification
        if folder is not UNSET:
            field_dict["folder"] = folder
        if approver is not UNSET:
            field_dict["approver"] = approver

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        name = d.pop("name")

        risk_scenarios = []
        _risk_scenarios = d.pop("risk_scenarios")
        for risk_scenarios_item_data in _risk_scenarios:
            risk_scenarios_item = UUID(risk_scenarios_item_data)

            risk_scenarios.append(risk_scenarios_item)

        is_published = d.pop("is_published", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_expiry_date(data: object) -> Union[None, Unset, datetime.date]:
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
            return cast(Union[None, Unset, datetime.date], data)

        expiry_date = _parse_expiry_date(d.pop("expiry_date", UNSET))

        def _parse_justification(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        justification = _parse_justification(d.pop("justification", UNSET))

        _folder = d.pop("folder", UNSET)
        folder: Union[Unset, UUID]
        if isinstance(_folder, Unset):
            folder = UNSET
        else:
            folder = UUID(_folder)

        def _parse_approver(data: object) -> Union[None, UUID, Unset]:
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
            return cast(Union[None, UUID, Unset], data)

        approver = _parse_approver(d.pop("approver", UNSET))

        risk_acceptance_write = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            risk_scenarios=risk_scenarios,
            is_published=is_published,
            description=description,
            expiry_date=expiry_date,
            justification=justification,
            folder=folder,
            approver=approver,
        )

        risk_acceptance_write.additional_properties = d
        return risk_acceptance_write

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
