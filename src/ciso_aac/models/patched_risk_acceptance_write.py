import datetime
import json
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define, field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedRiskAcceptanceWrite")


@_attrs_define
class PatchedRiskAcceptanceWrite:
    """
    Attributes:
        id (Union[Unset, UUID]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
        is_published (Union[Unset, bool]):
        name (Union[Unset, str]):
        description (Union[None, Unset, str]):
        expiry_date (Union[None, Unset, datetime.date]): Specify when the risk acceptance will no longer apply
        justification (Union[None, Unset, str]):
        folder (Union[Unset, UUID]):
        approver (Union[None, UUID, Unset]): Risk owner and approver identity
        risk_scenarios (Union[Unset, list[UUID]]): Select the risk scenarios to be accepted, attention they must be part
            of the chosen domain
    """

    id: Unset | UUID = UNSET
    created_at: Unset | datetime.datetime = UNSET
    updated_at: Unset | datetime.datetime = UNSET
    is_published: Unset | bool = UNSET
    name: Unset | str = UNSET
    description: None | Unset | str = UNSET
    expiry_date: None | Unset | datetime.date = UNSET
    justification: None | Unset | str = UNSET
    folder: Unset | UUID = UNSET
    approver: None | UUID | Unset = UNSET
    risk_scenarios: Unset | list[UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: Unset | str = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        created_at: Unset | str = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Unset | str = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        is_published = self.is_published

        name = self.name

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

        justification: None | Unset | str
        if isinstance(self.justification, Unset):
            justification = UNSET
        else:
            justification = self.justification

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

        risk_scenarios: Unset | list[str] = UNSET
        if not isinstance(self.risk_scenarios, Unset):
            risk_scenarios = []
            for risk_scenarios_item_data in self.risk_scenarios:
                risk_scenarios_item = str(risk_scenarios_item_data)
                risk_scenarios.append(risk_scenarios_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if name is not UNSET:
            field_dict["name"] = name
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
        if risk_scenarios is not UNSET:
            field_dict["risk_scenarios"] = risk_scenarios

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        id: Unset | bytes = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        created_at: Unset | bytes = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat().encode()

        updated_at: Unset | bytes = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat().encode()

        is_published = (
            self.is_published
            if isinstance(self.is_published, Unset)
            else (None, str(self.is_published).encode(), "text/plain")
        )

        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

        description: Unset | tuple[None, bytes, str]

        if isinstance(self.description, Unset):
            description = UNSET
        elif isinstance(self.description, str):
            description = (None, str(self.description).encode(), "text/plain")
        else:
            description = (None, str(self.description).encode(), "text/plain")

        expiry_date: Unset | tuple[None, bytes, str]

        if isinstance(self.expiry_date, Unset):
            expiry_date = UNSET
        elif isinstance(self.expiry_date, datetime.date):
            expiry_date = self.expiry_date.isoformat().encode()
        else:
            expiry_date = (None, str(self.expiry_date).encode(), "text/plain")

        justification: Unset | tuple[None, bytes, str]

        if isinstance(self.justification, Unset):
            justification = UNSET
        elif isinstance(self.justification, str):
            justification = (None, str(self.justification).encode(), "text/plain")
        else:
            justification = (None, str(self.justification).encode(), "text/plain")

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

        risk_scenarios: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.risk_scenarios, Unset):
            _temp_risk_scenarios = []
            for risk_scenarios_item_data in self.risk_scenarios:
                risk_scenarios_item = str(risk_scenarios_item_data)
                _temp_risk_scenarios.append(risk_scenarios_item)
            risk_scenarios = (None, json.dumps(_temp_risk_scenarios).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if name is not UNSET:
            field_dict["name"] = name
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
        if risk_scenarios is not UNSET:
            field_dict["risk_scenarios"] = risk_scenarios

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

        is_published = d.pop("is_published", UNSET)

        name = d.pop("name", UNSET)

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

        def _parse_justification(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        justification = _parse_justification(d.pop("justification", UNSET))

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

        risk_scenarios = []
        _risk_scenarios = d.pop("risk_scenarios", UNSET)
        for risk_scenarios_item_data in _risk_scenarios or []:
            risk_scenarios_item = UUID(risk_scenarios_item_data)

            risk_scenarios.append(risk_scenarios_item)

        patched_risk_acceptance_write = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            is_published=is_published,
            name=name,
            description=description,
            expiry_date=expiry_date,
            justification=justification,
            folder=folder,
            approver=approver,
            risk_scenarios=risk_scenarios,
        )

        patched_risk_acceptance_write.additional_properties = d
        return patched_risk_acceptance_write

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
