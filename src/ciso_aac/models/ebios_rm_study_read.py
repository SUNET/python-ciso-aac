import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.blank_enum import BlankEnum
from ..models.status_72a_enum import Status72AEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="EbiosRMStudyRead")


@_attrs_define
class EbiosRMStudyRead:
    """
    Attributes:
        id (UUID):
        str_ (str):
        perimeter (str):
        folder (str):
        risk_matrix (str):
        reference_entity (str):
        assets (list[str]):
        compliance_assessments (list[str]):
        risk_assessments (list[str]):
        authors (list[str]):
        reviewers (list[str]):
        roto_count (int):
        selected_roto_count (int):
        selected_attack_path_count (int):
        operational_scenario_count (int):
        applied_control_count (int):
        last_risk_assessment (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        name (str):
        is_published (Union[Unset, bool]):
        description (Union[None, Unset, str]):
        eta (Union[None, Unset, datetime.date]):
        due_date (Union[None, Unset, datetime.date]):
        ref_id (Union[Unset, str]):
        version (Union[None, Unset, str]): Version of the Ebios RM study (eg. 1.0, 2.0, etc.)
        status (Union[BlankEnum, None, Status72AEnum, Unset]):
        observation (Union[None, Unset, str]):
        meta (Union[Unset, Any]):
    """

    id: UUID
    str_: str
    perimeter: str
    folder: str
    risk_matrix: str
    reference_entity: str
    assets: list[str]
    compliance_assessments: list[str]
    risk_assessments: list[str]
    authors: list[str]
    reviewers: list[str]
    roto_count: int
    selected_roto_count: int
    selected_attack_path_count: int
    operational_scenario_count: int
    applied_control_count: int
    last_risk_assessment: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: str
    is_published: Union[Unset, bool] = UNSET
    description: Union[None, Unset, str] = UNSET
    eta: Union[None, Unset, datetime.date] = UNSET
    due_date: Union[None, Unset, datetime.date] = UNSET
    ref_id: Union[Unset, str] = UNSET
    version: Union[None, Unset, str] = UNSET
    status: Union[BlankEnum, None, Status72AEnum, Unset] = UNSET
    observation: Union[None, Unset, str] = UNSET
    meta: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        str_ = self.str_

        perimeter = self.perimeter

        folder = self.folder

        risk_matrix = self.risk_matrix

        reference_entity = self.reference_entity

        assets = self.assets

        compliance_assessments = self.compliance_assessments

        risk_assessments = self.risk_assessments

        authors = self.authors

        reviewers = self.reviewers

        roto_count = self.roto_count

        selected_roto_count = self.selected_roto_count

        selected_attack_path_count = self.selected_attack_path_count

        operational_scenario_count = self.operational_scenario_count

        applied_control_count = self.applied_control_count

        last_risk_assessment = self.last_risk_assessment

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        name = self.name

        is_published = self.is_published

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        eta: Union[None, Unset, str]
        if isinstance(self.eta, Unset):
            eta = UNSET
        elif isinstance(self.eta, datetime.date):
            eta = self.eta.isoformat()
        else:
            eta = self.eta

        due_date: Union[None, Unset, str]
        if isinstance(self.due_date, Unset):
            due_date = UNSET
        elif isinstance(self.due_date, datetime.date):
            due_date = self.due_date.isoformat()
        else:
            due_date = self.due_date

        ref_id = self.ref_id

        version: Union[None, Unset, str]
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        status: Union[None, Unset, str]
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, Status72AEnum):
            status = self.status.value
        elif isinstance(self.status, BlankEnum):
            status = self.status.value
        else:
            status = self.status

        observation: Union[None, Unset, str]
        if isinstance(self.observation, Unset):
            observation = UNSET
        else:
            observation = self.observation

        meta = self.meta

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "str": str_,
                "perimeter": perimeter,
                "folder": folder,
                "risk_matrix": risk_matrix,
                "reference_entity": reference_entity,
                "assets": assets,
                "compliance_assessments": compliance_assessments,
                "risk_assessments": risk_assessments,
                "authors": authors,
                "reviewers": reviewers,
                "roto_count": roto_count,
                "selected_roto_count": selected_roto_count,
                "selected_attack_path_count": selected_attack_path_count,
                "operational_scenario_count": operational_scenario_count,
                "applied_control_count": applied_control_count,
                "last_risk_assessment": last_risk_assessment,
                "created_at": created_at,
                "updated_at": updated_at,
                "name": name,
            }
        )
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if description is not UNSET:
            field_dict["description"] = description
        if eta is not UNSET:
            field_dict["eta"] = eta
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if ref_id is not UNSET:
            field_dict["ref_id"] = ref_id
        if version is not UNSET:
            field_dict["version"] = version
        if status is not UNSET:
            field_dict["status"] = status
        if observation is not UNSET:
            field_dict["observation"] = observation
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        str_ = d.pop("str")

        perimeter = d.pop("perimeter")

        folder = d.pop("folder")

        risk_matrix = d.pop("risk_matrix")

        reference_entity = d.pop("reference_entity")

        assets = cast(list[str], d.pop("assets"))

        compliance_assessments = cast(list[str], d.pop("compliance_assessments"))

        risk_assessments = cast(list[str], d.pop("risk_assessments"))

        authors = cast(list[str], d.pop("authors"))

        reviewers = cast(list[str], d.pop("reviewers"))

        roto_count = d.pop("roto_count")

        selected_roto_count = d.pop("selected_roto_count")

        selected_attack_path_count = d.pop("selected_attack_path_count")

        operational_scenario_count = d.pop("operational_scenario_count")

        applied_control_count = d.pop("applied_control_count")

        last_risk_assessment = d.pop("last_risk_assessment")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        name = d.pop("name")

        is_published = d.pop("is_published", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_eta(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                eta_type_0 = isoparse(data).date()

                return eta_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        eta = _parse_eta(d.pop("eta", UNSET))

        def _parse_due_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_date_type_0 = isoparse(data).date()

                return due_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        due_date = _parse_due_date(d.pop("due_date", UNSET))

        ref_id = d.pop("ref_id", UNSET)

        def _parse_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_status(data: object) -> Union[BlankEnum, None, Status72AEnum, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = Status72AEnum(data)

                return status_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = BlankEnum(data)

                return status_type_1
            except:  # noqa: E722
                pass
            return cast(Union[BlankEnum, None, Status72AEnum, Unset], data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_observation(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        observation = _parse_observation(d.pop("observation", UNSET))

        meta = d.pop("meta", UNSET)

        ebios_rm_study_read = cls(
            id=id,
            str_=str_,
            perimeter=perimeter,
            folder=folder,
            risk_matrix=risk_matrix,
            reference_entity=reference_entity,
            assets=assets,
            compliance_assessments=compliance_assessments,
            risk_assessments=risk_assessments,
            authors=authors,
            reviewers=reviewers,
            roto_count=roto_count,
            selected_roto_count=selected_roto_count,
            selected_attack_path_count=selected_attack_path_count,
            operational_scenario_count=operational_scenario_count,
            applied_control_count=applied_control_count,
            last_risk_assessment=last_risk_assessment,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            is_published=is_published,
            description=description,
            eta=eta,
            due_date=due_date,
            ref_id=ref_id,
            version=version,
            status=status,
            observation=observation,
            meta=meta,
        )

        ebios_rm_study_read.additional_properties = d
        return ebios_rm_study_read

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
