import datetime
import json
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define, field as _attrs_field
from dateutil.parser import isoparse

from ..models.blank_enum import BlankEnum
from ..models.conclusion_enum import ConclusionEnum
from ..models.status_72a_enum import Status72AEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedEntityAssessmentWrite")


@_attrs_define
class PatchedEntityAssessmentWrite:
    """
    Attributes:
        id (Union[Unset, UUID]):
        create_audit (Union[Unset, bool]):  Default: False.
        framework (Union[Unset, UUID]):
        selected_implementation_groups (Union[Unset, list[str]]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
        is_published (Union[Unset, bool]):
        name (Union[Unset, str]):
        description (Union[None, Unset, str]):
        eta (Union[None, Unset, datetime.date]):
        due_date (Union[None, Unset, datetime.date]):
        version (Union[None, Unset, str]): Version of the compliance assessment (eg. 1.0, 2.0, etc.)
        status (Union[BlankEnum, None, Status72AEnum, Unset]):
        observation (Union[None, Unset, str]):
        criticality (Union[Unset, int]):
        penetration (Union[Unset, int]):
        dependency (Union[Unset, int]):
        maturity (Union[Unset, int]):
        trust (Union[Unset, int]):
        conclusion (Union[BlankEnum, ConclusionEnum, None, Unset]):
        folder (Union[Unset, UUID]):
        perimeter (Union[None, UUID, Unset]):
        entity (Union[Unset, UUID]):
        compliance_assessment (Union[None, UUID, Unset]):
        evidence (Union[None, UUID, Unset]):
        authors (Union[Unset, list[UUID]]):
        reviewers (Union[Unset, list[UUID]]):
        representatives (Union[Unset, list[UUID]]):
        solutions (Union[Unset, list[UUID]]):
    """

    id: Unset | UUID = UNSET
    create_audit: Unset | bool = False
    framework: Unset | UUID = UNSET
    selected_implementation_groups: Unset | list[str] = UNSET
    created_at: Unset | datetime.datetime = UNSET
    updated_at: Unset | datetime.datetime = UNSET
    is_published: Unset | bool = UNSET
    name: Unset | str = UNSET
    description: None | Unset | str = UNSET
    eta: None | Unset | datetime.date = UNSET
    due_date: None | Unset | datetime.date = UNSET
    version: None | Unset | str = UNSET
    status: BlankEnum | None | Status72AEnum | Unset = UNSET
    observation: None | Unset | str = UNSET
    criticality: Unset | int = UNSET
    penetration: Unset | int = UNSET
    dependency: Unset | int = UNSET
    maturity: Unset | int = UNSET
    trust: Unset | int = UNSET
    conclusion: BlankEnum | ConclusionEnum | None | Unset = UNSET
    folder: Unset | UUID = UNSET
    perimeter: None | UUID | Unset = UNSET
    entity: Unset | UUID = UNSET
    compliance_assessment: None | UUID | Unset = UNSET
    evidence: None | UUID | Unset = UNSET
    authors: Unset | list[UUID] = UNSET
    reviewers: Unset | list[UUID] = UNSET
    representatives: Unset | list[UUID] = UNSET
    solutions: Unset | list[UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: Unset | str = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        create_audit = self.create_audit

        framework: Unset | str = UNSET
        if not isinstance(self.framework, Unset):
            framework = str(self.framework)

        selected_implementation_groups: Unset | list[str] = UNSET
        if not isinstance(self.selected_implementation_groups, Unset):
            selected_implementation_groups = self.selected_implementation_groups

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

        eta: None | Unset | str
        if isinstance(self.eta, Unset):
            eta = UNSET
        elif isinstance(self.eta, datetime.date):
            eta = self.eta.isoformat()
        else:
            eta = self.eta

        due_date: None | Unset | str
        if isinstance(self.due_date, Unset):
            due_date = UNSET
        elif isinstance(self.due_date, datetime.date):
            due_date = self.due_date.isoformat()
        else:
            due_date = self.due_date

        version: None | Unset | str
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        status: None | Unset | str
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, Status72AEnum):
            status = self.status.value
        elif isinstance(self.status, BlankEnum):
            status = self.status.value
        else:
            status = self.status

        observation: None | Unset | str
        if isinstance(self.observation, Unset):
            observation = UNSET
        else:
            observation = self.observation

        criticality = self.criticality

        penetration = self.penetration

        dependency = self.dependency

        maturity = self.maturity

        trust = self.trust

        conclusion: None | Unset | str
        if isinstance(self.conclusion, Unset):
            conclusion = UNSET
        elif isinstance(self.conclusion, ConclusionEnum):
            conclusion = self.conclusion.value
        elif isinstance(self.conclusion, BlankEnum):
            conclusion = self.conclusion.value
        else:
            conclusion = self.conclusion

        folder: Unset | str = UNSET
        if not isinstance(self.folder, Unset):
            folder = str(self.folder)

        perimeter: None | Unset | str
        if isinstance(self.perimeter, Unset):
            perimeter = UNSET
        elif isinstance(self.perimeter, UUID):
            perimeter = str(self.perimeter)
        else:
            perimeter = self.perimeter

        entity: Unset | str = UNSET
        if not isinstance(self.entity, Unset):
            entity = str(self.entity)

        compliance_assessment: None | Unset | str
        if isinstance(self.compliance_assessment, Unset):
            compliance_assessment = UNSET
        elif isinstance(self.compliance_assessment, UUID):
            compliance_assessment = str(self.compliance_assessment)
        else:
            compliance_assessment = self.compliance_assessment

        evidence: None | Unset | str
        if isinstance(self.evidence, Unset):
            evidence = UNSET
        elif isinstance(self.evidence, UUID):
            evidence = str(self.evidence)
        else:
            evidence = self.evidence

        authors: Unset | list[str] = UNSET
        if not isinstance(self.authors, Unset):
            authors = []
            for authors_item_data in self.authors:
                authors_item = str(authors_item_data)
                authors.append(authors_item)

        reviewers: Unset | list[str] = UNSET
        if not isinstance(self.reviewers, Unset):
            reviewers = []
            for reviewers_item_data in self.reviewers:
                reviewers_item = str(reviewers_item_data)
                reviewers.append(reviewers_item)

        representatives: Unset | list[str] = UNSET
        if not isinstance(self.representatives, Unset):
            representatives = []
            for representatives_item_data in self.representatives:
                representatives_item = str(representatives_item_data)
                representatives.append(representatives_item)

        solutions: Unset | list[str] = UNSET
        if not isinstance(self.solutions, Unset):
            solutions = []
            for solutions_item_data in self.solutions:
                solutions_item = str(solutions_item_data)
                solutions.append(solutions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if create_audit is not UNSET:
            field_dict["create_audit"] = create_audit
        if framework is not UNSET:
            field_dict["framework"] = framework
        if selected_implementation_groups is not UNSET:
            field_dict["selected_implementation_groups"] = selected_implementation_groups
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
        if eta is not UNSET:
            field_dict["eta"] = eta
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if version is not UNSET:
            field_dict["version"] = version
        if status is not UNSET:
            field_dict["status"] = status
        if observation is not UNSET:
            field_dict["observation"] = observation
        if criticality is not UNSET:
            field_dict["criticality"] = criticality
        if penetration is not UNSET:
            field_dict["penetration"] = penetration
        if dependency is not UNSET:
            field_dict["dependency"] = dependency
        if maturity is not UNSET:
            field_dict["maturity"] = maturity
        if trust is not UNSET:
            field_dict["trust"] = trust
        if conclusion is not UNSET:
            field_dict["conclusion"] = conclusion
        if folder is not UNSET:
            field_dict["folder"] = folder
        if perimeter is not UNSET:
            field_dict["perimeter"] = perimeter
        if entity is not UNSET:
            field_dict["entity"] = entity
        if compliance_assessment is not UNSET:
            field_dict["compliance_assessment"] = compliance_assessment
        if evidence is not UNSET:
            field_dict["evidence"] = evidence
        if authors is not UNSET:
            field_dict["authors"] = authors
        if reviewers is not UNSET:
            field_dict["reviewers"] = reviewers
        if representatives is not UNSET:
            field_dict["representatives"] = representatives
        if solutions is not UNSET:
            field_dict["solutions"] = solutions

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        id: Unset | bytes = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        create_audit = (
            self.create_audit
            if isinstance(self.create_audit, Unset)
            else (None, str(self.create_audit).encode(), "text/plain")
        )

        framework: Unset | bytes = UNSET
        if not isinstance(self.framework, Unset):
            framework = str(self.framework)

        selected_implementation_groups: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.selected_implementation_groups, Unset):
            _temp_selected_implementation_groups = self.selected_implementation_groups
            selected_implementation_groups = (
                None,
                json.dumps(_temp_selected_implementation_groups).encode(),
                "application/json",
            )

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

        eta: Unset | tuple[None, bytes, str]

        if isinstance(self.eta, Unset):
            eta = UNSET
        elif isinstance(self.eta, datetime.date):
            eta = self.eta.isoformat().encode()
        else:
            eta = (None, str(self.eta).encode(), "text/plain")

        due_date: Unset | tuple[None, bytes, str]

        if isinstance(self.due_date, Unset):
            due_date = UNSET
        elif isinstance(self.due_date, datetime.date):
            due_date = self.due_date.isoformat().encode()
        else:
            due_date = (None, str(self.due_date).encode(), "text/plain")

        version: Unset | tuple[None, bytes, str]

        if isinstance(self.version, Unset):
            version = UNSET
        elif isinstance(self.version, str):
            version = (None, str(self.version).encode(), "text/plain")
        else:
            version = (None, str(self.version).encode(), "text/plain")

        status: Unset | tuple[None, bytes, str]

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

        observation: Unset | tuple[None, bytes, str]

        if isinstance(self.observation, Unset):
            observation = UNSET
        elif isinstance(self.observation, str):
            observation = (None, str(self.observation).encode(), "text/plain")
        else:
            observation = (None, str(self.observation).encode(), "text/plain")

        criticality = (
            self.criticality
            if isinstance(self.criticality, Unset)
            else (None, str(self.criticality).encode(), "text/plain")
        )

        penetration = (
            self.penetration
            if isinstance(self.penetration, Unset)
            else (None, str(self.penetration).encode(), "text/plain")
        )

        dependency = (
            self.dependency
            if isinstance(self.dependency, Unset)
            else (None, str(self.dependency).encode(), "text/plain")
        )

        maturity = (
            self.maturity if isinstance(self.maturity, Unset) else (None, str(self.maturity).encode(), "text/plain")
        )

        trust = self.trust if isinstance(self.trust, Unset) else (None, str(self.trust).encode(), "text/plain")

        conclusion: Unset | tuple[None, bytes, str]

        if isinstance(self.conclusion, Unset):
            conclusion = UNSET
        elif isinstance(self.conclusion, ConclusionEnum):
            conclusion = (None, str(self.conclusion.value).encode(), "text/plain")
        elif isinstance(self.conclusion, BlankEnum):
            conclusion = (None, str(self.conclusion.value).encode(), "text/plain")
        elif isinstance(self.conclusion, None):
            conclusion = (None, str(self.conclusion).encode(), "text/plain")
        else:
            conclusion = (None, str(self.conclusion).encode(), "text/plain")

        folder: Unset | bytes = UNSET
        if not isinstance(self.folder, Unset):
            folder = str(self.folder)

        perimeter: Unset | tuple[None, bytes, str]

        if isinstance(self.perimeter, Unset):
            perimeter = UNSET
        elif isinstance(self.perimeter, UUID):
            perimeter = str(self.perimeter)
        else:
            perimeter = (None, str(self.perimeter).encode(), "text/plain")

        entity: Unset | bytes = UNSET
        if not isinstance(self.entity, Unset):
            entity = str(self.entity)

        compliance_assessment: Unset | tuple[None, bytes, str]

        if isinstance(self.compliance_assessment, Unset):
            compliance_assessment = UNSET
        elif isinstance(self.compliance_assessment, UUID):
            compliance_assessment = str(self.compliance_assessment)
        else:
            compliance_assessment = (None, str(self.compliance_assessment).encode(), "text/plain")

        evidence: Unset | tuple[None, bytes, str]

        if isinstance(self.evidence, Unset):
            evidence = UNSET
        elif isinstance(self.evidence, UUID):
            evidence = str(self.evidence)
        else:
            evidence = (None, str(self.evidence).encode(), "text/plain")

        authors: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.authors, Unset):
            _temp_authors = []
            for authors_item_data in self.authors:
                authors_item = str(authors_item_data)
                _temp_authors.append(authors_item)
            authors = (None, json.dumps(_temp_authors).encode(), "application/json")

        reviewers: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.reviewers, Unset):
            _temp_reviewers = []
            for reviewers_item_data in self.reviewers:
                reviewers_item = str(reviewers_item_data)
                _temp_reviewers.append(reviewers_item)
            reviewers = (None, json.dumps(_temp_reviewers).encode(), "application/json")

        representatives: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.representatives, Unset):
            _temp_representatives = []
            for representatives_item_data in self.representatives:
                representatives_item = str(representatives_item_data)
                _temp_representatives.append(representatives_item)
            representatives = (None, json.dumps(_temp_representatives).encode(), "application/json")

        solutions: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.solutions, Unset):
            _temp_solutions = []
            for solutions_item_data in self.solutions:
                solutions_item = str(solutions_item_data)
                _temp_solutions.append(solutions_item)
            solutions = (None, json.dumps(_temp_solutions).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if create_audit is not UNSET:
            field_dict["create_audit"] = create_audit
        if framework is not UNSET:
            field_dict["framework"] = framework
        if selected_implementation_groups is not UNSET:
            field_dict["selected_implementation_groups"] = selected_implementation_groups
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
        if eta is not UNSET:
            field_dict["eta"] = eta
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if version is not UNSET:
            field_dict["version"] = version
        if status is not UNSET:
            field_dict["status"] = status
        if observation is not UNSET:
            field_dict["observation"] = observation
        if criticality is not UNSET:
            field_dict["criticality"] = criticality
        if penetration is not UNSET:
            field_dict["penetration"] = penetration
        if dependency is not UNSET:
            field_dict["dependency"] = dependency
        if maturity is not UNSET:
            field_dict["maturity"] = maturity
        if trust is not UNSET:
            field_dict["trust"] = trust
        if conclusion is not UNSET:
            field_dict["conclusion"] = conclusion
        if folder is not UNSET:
            field_dict["folder"] = folder
        if perimeter is not UNSET:
            field_dict["perimeter"] = perimeter
        if entity is not UNSET:
            field_dict["entity"] = entity
        if compliance_assessment is not UNSET:
            field_dict["compliance_assessment"] = compliance_assessment
        if evidence is not UNSET:
            field_dict["evidence"] = evidence
        if authors is not UNSET:
            field_dict["authors"] = authors
        if reviewers is not UNSET:
            field_dict["reviewers"] = reviewers
        if representatives is not UNSET:
            field_dict["representatives"] = representatives
        if solutions is not UNSET:
            field_dict["solutions"] = solutions

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

        create_audit = d.pop("create_audit", UNSET)

        _framework = d.pop("framework", UNSET)
        framework: Unset | UUID
        if isinstance(_framework, Unset):
            framework = UNSET
        else:
            framework = UUID(_framework)

        selected_implementation_groups = cast(list[str], d.pop("selected_implementation_groups", UNSET))

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

        def _parse_eta(data: object) -> None | Unset | datetime.date:
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
            return cast(None | Unset | datetime.date, data)

        eta = _parse_eta(d.pop("eta", UNSET))

        def _parse_due_date(data: object) -> None | Unset | datetime.date:
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
            return cast(None | Unset | datetime.date, data)

        due_date = _parse_due_date(d.pop("due_date", UNSET))

        def _parse_version(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_status(data: object) -> BlankEnum | None | Status72AEnum | Unset:
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
            return cast(BlankEnum | None | Status72AEnum | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_observation(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        observation = _parse_observation(d.pop("observation", UNSET))

        criticality = d.pop("criticality", UNSET)

        penetration = d.pop("penetration", UNSET)

        dependency = d.pop("dependency", UNSET)

        maturity = d.pop("maturity", UNSET)

        trust = d.pop("trust", UNSET)

        def _parse_conclusion(data: object) -> BlankEnum | ConclusionEnum | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                conclusion_type_0 = ConclusionEnum(data)

                return conclusion_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                conclusion_type_1 = BlankEnum(data)

                return conclusion_type_1
            except:  # noqa: E722
                pass
            return cast(BlankEnum | ConclusionEnum | None | Unset, data)

        conclusion = _parse_conclusion(d.pop("conclusion", UNSET))

        _folder = d.pop("folder", UNSET)
        folder: Unset | UUID
        if isinstance(_folder, Unset):
            folder = UNSET
        else:
            folder = UUID(_folder)

        def _parse_perimeter(data: object) -> None | UUID | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                perimeter_type_0 = UUID(data)

                return perimeter_type_0
            except:  # noqa: E722
                pass
            return cast(None | UUID | Unset, data)

        perimeter = _parse_perimeter(d.pop("perimeter", UNSET))

        _entity = d.pop("entity", UNSET)
        entity: Unset | UUID
        if isinstance(_entity, Unset):
            entity = UNSET
        else:
            entity = UUID(_entity)

        def _parse_compliance_assessment(data: object) -> None | UUID | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                compliance_assessment_type_0 = UUID(data)

                return compliance_assessment_type_0
            except:  # noqa: E722
                pass
            return cast(None | UUID | Unset, data)

        compliance_assessment = _parse_compliance_assessment(d.pop("compliance_assessment", UNSET))

        def _parse_evidence(data: object) -> None | UUID | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                evidence_type_0 = UUID(data)

                return evidence_type_0
            except:  # noqa: E722
                pass
            return cast(None | UUID | Unset, data)

        evidence = _parse_evidence(d.pop("evidence", UNSET))

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

        representatives = []
        _representatives = d.pop("representatives", UNSET)
        for representatives_item_data in _representatives or []:
            representatives_item = UUID(representatives_item_data)

            representatives.append(representatives_item)

        solutions = []
        _solutions = d.pop("solutions", UNSET)
        for solutions_item_data in _solutions or []:
            solutions_item = UUID(solutions_item_data)

            solutions.append(solutions_item)

        patched_entity_assessment_write = cls(
            id=id,
            create_audit=create_audit,
            framework=framework,
            selected_implementation_groups=selected_implementation_groups,
            created_at=created_at,
            updated_at=updated_at,
            is_published=is_published,
            name=name,
            description=description,
            eta=eta,
            due_date=due_date,
            version=version,
            status=status,
            observation=observation,
            criticality=criticality,
            penetration=penetration,
            dependency=dependency,
            maturity=maturity,
            trust=trust,
            conclusion=conclusion,
            folder=folder,
            perimeter=perimeter,
            entity=entity,
            compliance_assessment=compliance_assessment,
            evidence=evidence,
            authors=authors,
            reviewers=reviewers,
            representatives=representatives,
            solutions=solutions,
        )

        patched_entity_assessment_write.additional_properties = d
        return patched_entity_assessment_write

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
