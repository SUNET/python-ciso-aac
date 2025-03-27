import datetime
import json
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.blank_enum import BlankEnum
from ..models.status_72a_enum import Status72AEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="EbiosRMStudyWrite")


@_attrs_define
class EbiosRMStudyWrite:
    """
    Attributes:
        id (UUID):
        name (str):
        risk_matrix (Union[Unset, UUID]):
        is_published (Union[Unset, bool]):
        description (Union[None, Unset, str]):
        eta (Union[None, Unset, datetime.date]):
        due_date (Union[None, Unset, datetime.date]):
        ref_id (Union[Unset, str]):
        version (Union[None, Unset, str]): Version of the Ebios RM study (eg. 1.0, 2.0, etc.)
        status (Union[BlankEnum, None, Status72AEnum, Unset]):
        observation (Union[None, Unset, str]):
        meta (Union[Unset, Any]):
        folder (Union[Unset, UUID]):
        reference_entity (Union[Unset, UUID]): Entity that is the focus of the study
        assets (Union[Unset, list[UUID]]): Assets that are pertinent to the study
        compliance_assessments (Union[Unset, list[UUID]]): Compliance assessments established as security baseline
            during workshop 1.4
        authors (Union[Unset, list[UUID]]):
        reviewers (Union[Unset, list[UUID]]):
    """

    id: UUID
    name: str
    risk_matrix: Union[Unset, UUID] = UNSET
    is_published: Union[Unset, bool] = UNSET
    description: Union[None, Unset, str] = UNSET
    eta: Union[None, Unset, datetime.date] = UNSET
    due_date: Union[None, Unset, datetime.date] = UNSET
    ref_id: Union[Unset, str] = UNSET
    version: Union[None, Unset, str] = UNSET
    status: Union[BlankEnum, None, Status72AEnum, Unset] = UNSET
    observation: Union[None, Unset, str] = UNSET
    meta: Union[Unset, Any] = UNSET
    folder: Union[Unset, UUID] = UNSET
    reference_entity: Union[Unset, UUID] = UNSET
    assets: Union[Unset, list[UUID]] = UNSET
    compliance_assessments: Union[Unset, list[UUID]] = UNSET
    authors: Union[Unset, list[UUID]] = UNSET
    reviewers: Union[Unset, list[UUID]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        risk_matrix: Union[Unset, str] = UNSET
        if not isinstance(self.risk_matrix, Unset):
            risk_matrix = str(self.risk_matrix)

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

        folder: Union[Unset, str] = UNSET
        if not isinstance(self.folder, Unset):
            folder = str(self.folder)

        reference_entity: Union[Unset, str] = UNSET
        if not isinstance(self.reference_entity, Unset):
            reference_entity = str(self.reference_entity)

        assets: Union[Unset, list[str]] = UNSET
        if not isinstance(self.assets, Unset):
            assets = []
            for assets_item_data in self.assets:
                assets_item = str(assets_item_data)
                assets.append(assets_item)

        compliance_assessments: Union[Unset, list[str]] = UNSET
        if not isinstance(self.compliance_assessments, Unset):
            compliance_assessments = []
            for compliance_assessments_item_data in self.compliance_assessments:
                compliance_assessments_item = str(compliance_assessments_item_data)
                compliance_assessments.append(compliance_assessments_item)

        authors: Union[Unset, list[str]] = UNSET
        if not isinstance(self.authors, Unset):
            authors = []
            for authors_item_data in self.authors:
                authors_item = str(authors_item_data)
                authors.append(authors_item)

        reviewers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.reviewers, Unset):
            reviewers = []
            for reviewers_item_data in self.reviewers:
                reviewers_item = str(reviewers_item_data)
                reviewers.append(reviewers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if risk_matrix is not UNSET:
            field_dict["risk_matrix"] = risk_matrix
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
        if folder is not UNSET:
            field_dict["folder"] = folder
        if reference_entity is not UNSET:
            field_dict["reference_entity"] = reference_entity
        if assets is not UNSET:
            field_dict["assets"] = assets
        if compliance_assessments is not UNSET:
            field_dict["compliance_assessments"] = compliance_assessments
        if authors is not UNSET:
            field_dict["authors"] = authors
        if reviewers is not UNSET:
            field_dict["reviewers"] = reviewers

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        id = str(self.id)

        name = (None, str(self.name).encode(), "text/plain")

        risk_matrix: Union[Unset, bytes] = UNSET
        if not isinstance(self.risk_matrix, Unset):
            risk_matrix = str(self.risk_matrix)

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

        eta: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.eta, Unset):
            eta = UNSET
        elif isinstance(self.eta, datetime.date):
            eta = self.eta.isoformat().encode()
        else:
            eta = (None, str(self.eta).encode(), "text/plain")

        due_date: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.due_date, Unset):
            due_date = UNSET
        elif isinstance(self.due_date, datetime.date):
            due_date = self.due_date.isoformat().encode()
        else:
            due_date = (None, str(self.due_date).encode(), "text/plain")

        ref_id = self.ref_id if isinstance(self.ref_id, Unset) else (None, str(self.ref_id).encode(), "text/plain")

        version: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.version, Unset):
            version = UNSET
        elif isinstance(self.version, str):
            version = (None, str(self.version).encode(), "text/plain")
        else:
            version = (None, str(self.version).encode(), "text/plain")

        status: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, Status72AEnum):
            status = (None, str(self.status.value).encode(), "text/plain")
        elif isinstance(self.status, BlankEnum):
            status = (None, str(self.status.value).encode(), "text/plain")
        elif isinstance(self.status, None):
            status = (None, str(self.status).encode(), "text/plain")
        else:
            status = (None, str(self.status).encode(), "text/plain")

        observation: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.observation, Unset):
            observation = UNSET
        elif isinstance(self.observation, str):
            observation = (None, str(self.observation).encode(), "text/plain")
        else:
            observation = (None, str(self.observation).encode(), "text/plain")

        meta = self.meta if isinstance(self.meta, Unset) else (None, str(self.meta).encode(), "text/plain")

        folder: Union[Unset, bytes] = UNSET
        if not isinstance(self.folder, Unset):
            folder = str(self.folder)

        reference_entity: Union[Unset, bytes] = UNSET
        if not isinstance(self.reference_entity, Unset):
            reference_entity = str(self.reference_entity)

        assets: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.assets, Unset):
            _temp_assets = []
            for assets_item_data in self.assets:
                assets_item = str(assets_item_data)
                _temp_assets.append(assets_item)
            assets = (None, json.dumps(_temp_assets).encode(), "application/json")

        compliance_assessments: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.compliance_assessments, Unset):
            _temp_compliance_assessments = []
            for compliance_assessments_item_data in self.compliance_assessments:
                compliance_assessments_item = str(compliance_assessments_item_data)
                _temp_compliance_assessments.append(compliance_assessments_item)
            compliance_assessments = (None, json.dumps(_temp_compliance_assessments).encode(), "application/json")

        authors: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.authors, Unset):
            _temp_authors = []
            for authors_item_data in self.authors:
                authors_item = str(authors_item_data)
                _temp_authors.append(authors_item)
            authors = (None, json.dumps(_temp_authors).encode(), "application/json")

        reviewers: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.reviewers, Unset):
            _temp_reviewers = []
            for reviewers_item_data in self.reviewers:
                reviewers_item = str(reviewers_item_data)
                _temp_reviewers.append(reviewers_item)
            reviewers = (None, json.dumps(_temp_reviewers).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if risk_matrix is not UNSET:
            field_dict["risk_matrix"] = risk_matrix
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
        if folder is not UNSET:
            field_dict["folder"] = folder
        if reference_entity is not UNSET:
            field_dict["reference_entity"] = reference_entity
        if assets is not UNSET:
            field_dict["assets"] = assets
        if compliance_assessments is not UNSET:
            field_dict["compliance_assessments"] = compliance_assessments
        if authors is not UNSET:
            field_dict["authors"] = authors
        if reviewers is not UNSET:
            field_dict["reviewers"] = reviewers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        _risk_matrix = d.pop("risk_matrix", UNSET)
        risk_matrix: Union[Unset, UUID]
        if isinstance(_risk_matrix, Unset):
            risk_matrix = UNSET
        else:
            risk_matrix = UUID(_risk_matrix)

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

        _folder = d.pop("folder", UNSET)
        folder: Union[Unset, UUID]
        if isinstance(_folder, Unset):
            folder = UNSET
        else:
            folder = UUID(_folder)

        _reference_entity = d.pop("reference_entity", UNSET)
        reference_entity: Union[Unset, UUID]
        if isinstance(_reference_entity, Unset):
            reference_entity = UNSET
        else:
            reference_entity = UUID(_reference_entity)

        assets = []
        _assets = d.pop("assets", UNSET)
        for assets_item_data in _assets or []:
            assets_item = UUID(assets_item_data)

            assets.append(assets_item)

        compliance_assessments = []
        _compliance_assessments = d.pop("compliance_assessments", UNSET)
        for compliance_assessments_item_data in _compliance_assessments or []:
            compliance_assessments_item = UUID(compliance_assessments_item_data)

            compliance_assessments.append(compliance_assessments_item)

        authors = []
        _authors = d.pop("authors", UNSET)
        for authors_item_data in _authors or []:
            authors_item = UUID(authors_item_data)

            authors.append(authors_item)

        reviewers = []
        _reviewers = d.pop("reviewers", UNSET)
        for reviewers_item_data in _reviewers or []:
            reviewers_item = UUID(reviewers_item_data)

            reviewers.append(reviewers_item)

        ebios_rm_study_write = cls(
            id=id,
            name=name,
            risk_matrix=risk_matrix,
            is_published=is_published,
            description=description,
            eta=eta,
            due_date=due_date,
            ref_id=ref_id,
            version=version,
            status=status,
            observation=observation,
            meta=meta,
            folder=folder,
            reference_entity=reference_entity,
            assets=assets,
            compliance_assessments=compliance_assessments,
            authors=authors,
            reviewers=reviewers,
        )

        ebios_rm_study_write.additional_properties = d
        return ebios_rm_study_write

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
