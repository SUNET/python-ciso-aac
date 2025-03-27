import datetime
import json
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.blank_enum import BlankEnum
from ..models.status_72a_enum import Status72AEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ComplianceAssessmentWrite")


@_attrs_define
class ComplianceAssessmentWrite:
    """
    Attributes:
        id (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        name (str):
        framework (UUID):
        baseline (Union[None, UUID, Unset]):
        ebios_rm_studies (Union[Unset, list[Union[None, UUID]]]):
        create_applied_controls_from_suggestions (Union[Unset, bool]):  Default: False.
        is_published (Union[Unset, bool]):
        description (Union[None, Unset, str]):
        eta (Union[None, Unset, datetime.date]):
        due_date (Union[None, Unset, datetime.date]):
        version (Union[None, Unset, str]): Version of the compliance assessment (eg. 1.0, 2.0, etc.)
        status (Union[BlankEnum, None, Status72AEnum, Unset]):
        observation (Union[None, Unset, str]):
        selected_implementation_groups (Union[Unset, Any]):
        ref_id (Union[None, Unset, str]):
        min_score (Union[None, Unset, int]):
        max_score (Union[None, Unset, int]):
        scores_definition (Union[Unset, Any]):
        show_documentation_score (Union[Unset, bool]):
        folder (Union[Unset, UUID]):
        perimeter (Union[None, UUID, Unset]):
        authors (Union[Unset, list[UUID]]):
        reviewers (Union[Unset, list[UUID]]):
        assets (Union[Unset, list[UUID]]): Assets related to the compliance assessment
    """

    id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: str
    framework: UUID
    baseline: None | UUID | Unset = UNSET
    ebios_rm_studies: Unset | list[None | UUID] = UNSET
    create_applied_controls_from_suggestions: Unset | bool = False
    is_published: Unset | bool = UNSET
    description: None | Unset | str = UNSET
    eta: None | Unset | datetime.date = UNSET
    due_date: None | Unset | datetime.date = UNSET
    version: None | Unset | str = UNSET
    status: BlankEnum | None | Status72AEnum | Unset = UNSET
    observation: None | Unset | str = UNSET
    selected_implementation_groups: Unset | Any = UNSET
    ref_id: None | Unset | str = UNSET
    min_score: None | Unset | int = UNSET
    max_score: None | Unset | int = UNSET
    scores_definition: Unset | Any = UNSET
    show_documentation_score: Unset | bool = UNSET
    folder: Unset | UUID = UNSET
    perimeter: None | UUID | Unset = UNSET
    authors: Unset | list[UUID] = UNSET
    reviewers: Unset | list[UUID] = UNSET
    assets: Unset | list[UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        name = self.name

        framework = str(self.framework)

        baseline: None | Unset | str
        if isinstance(self.baseline, Unset):
            baseline = UNSET
        elif isinstance(self.baseline, UUID):
            baseline = str(self.baseline)
        else:
            baseline = self.baseline

        ebios_rm_studies: Unset | list[None | str] = UNSET
        if not isinstance(self.ebios_rm_studies, Unset):
            ebios_rm_studies = []
            for ebios_rm_studies_item_data in self.ebios_rm_studies:
                ebios_rm_studies_item: None | str
                if isinstance(ebios_rm_studies_item_data, UUID):
                    ebios_rm_studies_item = str(ebios_rm_studies_item_data)
                else:
                    ebios_rm_studies_item = ebios_rm_studies_item_data
                ebios_rm_studies.append(ebios_rm_studies_item)

        create_applied_controls_from_suggestions = self.create_applied_controls_from_suggestions

        is_published = self.is_published

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

        selected_implementation_groups = self.selected_implementation_groups

        ref_id: None | Unset | str
        if isinstance(self.ref_id, Unset):
            ref_id = UNSET
        else:
            ref_id = self.ref_id

        min_score: None | Unset | int
        if isinstance(self.min_score, Unset):
            min_score = UNSET
        else:
            min_score = self.min_score

        max_score: None | Unset | int
        if isinstance(self.max_score, Unset):
            max_score = UNSET
        else:
            max_score = self.max_score

        scores_definition = self.scores_definition

        show_documentation_score = self.show_documentation_score

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

        assets: Unset | list[str] = UNSET
        if not isinstance(self.assets, Unset):
            assets = []
            for assets_item_data in self.assets:
                assets_item = str(assets_item_data)
                assets.append(assets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "updated_at": updated_at,
                "name": name,
                "framework": framework,
            }
        )
        if baseline is not UNSET:
            field_dict["baseline"] = baseline
        if ebios_rm_studies is not UNSET:
            field_dict["ebios_rm_studies"] = ebios_rm_studies
        if create_applied_controls_from_suggestions is not UNSET:
            field_dict["create_applied_controls_from_suggestions"] = create_applied_controls_from_suggestions
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
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
        if selected_implementation_groups is not UNSET:
            field_dict["selected_implementation_groups"] = selected_implementation_groups
        if ref_id is not UNSET:
            field_dict["ref_id"] = ref_id
        if min_score is not UNSET:
            field_dict["min_score"] = min_score
        if max_score is not UNSET:
            field_dict["max_score"] = max_score
        if scores_definition is not UNSET:
            field_dict["scores_definition"] = scores_definition
        if show_documentation_score is not UNSET:
            field_dict["show_documentation_score"] = show_documentation_score
        if folder is not UNSET:
            field_dict["folder"] = folder
        if perimeter is not UNSET:
            field_dict["perimeter"] = perimeter
        if authors is not UNSET:
            field_dict["authors"] = authors
        if reviewers is not UNSET:
            field_dict["reviewers"] = reviewers
        if assets is not UNSET:
            field_dict["assets"] = assets

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        id = str(self.id)

        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        name = (None, str(self.name).encode(), "text/plain")

        framework = str(self.framework)

        baseline: Unset | tuple[None, bytes, str]

        if isinstance(self.baseline, Unset):
            baseline = UNSET
        elif isinstance(self.baseline, UUID):
            baseline = str(self.baseline)
        else:
            baseline = (None, str(self.baseline).encode(), "text/plain")

        ebios_rm_studies: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.ebios_rm_studies, Unset):
            _temp_ebios_rm_studies = []
            for ebios_rm_studies_item_data in self.ebios_rm_studies:
                ebios_rm_studies_item: None | str
                if isinstance(ebios_rm_studies_item_data, UUID):
                    ebios_rm_studies_item = str(ebios_rm_studies_item_data)
                else:
                    ebios_rm_studies_item = ebios_rm_studies_item_data
                _temp_ebios_rm_studies.append(ebios_rm_studies_item)
            ebios_rm_studies = (None, json.dumps(_temp_ebios_rm_studies).encode(), "application/json")

        create_applied_controls_from_suggestions = (
            self.create_applied_controls_from_suggestions
            if isinstance(self.create_applied_controls_from_suggestions, Unset)
            else (None, str(self.create_applied_controls_from_suggestions).encode(), "text/plain")
        )

        is_published = (
            self.is_published
            if isinstance(self.is_published, Unset)
            else (None, str(self.is_published).encode(), "text/plain")
        )

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

        selected_implementation_groups = (
            self.selected_implementation_groups
            if isinstance(self.selected_implementation_groups, Unset)
            else (None, str(self.selected_implementation_groups).encode(), "text/plain")
        )

        ref_id: Unset | tuple[None, bytes, str]

        if isinstance(self.ref_id, Unset):
            ref_id = UNSET
        elif isinstance(self.ref_id, str):
            ref_id = (None, str(self.ref_id).encode(), "text/plain")
        else:
            ref_id = (None, str(self.ref_id).encode(), "text/plain")

        min_score: Unset | tuple[None, bytes, str]

        if isinstance(self.min_score, Unset):
            min_score = UNSET
        elif isinstance(self.min_score, int):
            min_score = (None, str(self.min_score).encode(), "text/plain")
        else:
            min_score = (None, str(self.min_score).encode(), "text/plain")

        max_score: Unset | tuple[None, bytes, str]

        if isinstance(self.max_score, Unset):
            max_score = UNSET
        elif isinstance(self.max_score, int):
            max_score = (None, str(self.max_score).encode(), "text/plain")
        else:
            max_score = (None, str(self.max_score).encode(), "text/plain")

        scores_definition = (
            self.scores_definition
            if isinstance(self.scores_definition, Unset)
            else (None, str(self.scores_definition).encode(), "text/plain")
        )

        show_documentation_score = (
            self.show_documentation_score
            if isinstance(self.show_documentation_score, Unset)
            else (None, str(self.show_documentation_score).encode(), "text/plain")
        )

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

        assets: Unset | tuple[None, bytes, str] = UNSET
        if not isinstance(self.assets, Unset):
            _temp_assets = []
            for assets_item_data in self.assets:
                assets_item = str(assets_item_data)
                _temp_assets.append(assets_item)
            assets = (None, json.dumps(_temp_assets).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "updated_at": updated_at,
                "name": name,
                "framework": framework,
            }
        )
        if baseline is not UNSET:
            field_dict["baseline"] = baseline
        if ebios_rm_studies is not UNSET:
            field_dict["ebios_rm_studies"] = ebios_rm_studies
        if create_applied_controls_from_suggestions is not UNSET:
            field_dict["create_applied_controls_from_suggestions"] = create_applied_controls_from_suggestions
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
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
        if selected_implementation_groups is not UNSET:
            field_dict["selected_implementation_groups"] = selected_implementation_groups
        if ref_id is not UNSET:
            field_dict["ref_id"] = ref_id
        if min_score is not UNSET:
            field_dict["min_score"] = min_score
        if max_score is not UNSET:
            field_dict["max_score"] = max_score
        if scores_definition is not UNSET:
            field_dict["scores_definition"] = scores_definition
        if show_documentation_score is not UNSET:
            field_dict["show_documentation_score"] = show_documentation_score
        if folder is not UNSET:
            field_dict["folder"] = folder
        if perimeter is not UNSET:
            field_dict["perimeter"] = perimeter
        if authors is not UNSET:
            field_dict["authors"] = authors
        if reviewers is not UNSET:
            field_dict["reviewers"] = reviewers
        if assets is not UNSET:
            field_dict["assets"] = assets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        name = d.pop("name")

        framework = UUID(d.pop("framework"))

        def _parse_baseline(data: object) -> None | UUID | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                baseline_type_0 = UUID(data)

                return baseline_type_0
            except:  # noqa: E722
                pass
            return cast(None | UUID | Unset, data)

        baseline = _parse_baseline(d.pop("baseline", UNSET))

        ebios_rm_studies = []
        _ebios_rm_studies = d.pop("ebios_rm_studies", UNSET)
        for ebios_rm_studies_item_data in _ebios_rm_studies or []:

            def _parse_ebios_rm_studies_item(data: object) -> None | UUID:
                if data is None:
                    return data
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    ebios_rm_studies_item_type_0 = UUID(data)

                    return ebios_rm_studies_item_type_0
                except:  # noqa: E722
                    pass
                return cast(None | UUID, data)

            ebios_rm_studies_item = _parse_ebios_rm_studies_item(ebios_rm_studies_item_data)

            ebios_rm_studies.append(ebios_rm_studies_item)

        create_applied_controls_from_suggestions = d.pop("create_applied_controls_from_suggestions", UNSET)

        is_published = d.pop("is_published", UNSET)

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

        selected_implementation_groups = d.pop("selected_implementation_groups", UNSET)

        def _parse_ref_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        ref_id = _parse_ref_id(d.pop("ref_id", UNSET))

        def _parse_min_score(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        min_score = _parse_min_score(d.pop("min_score", UNSET))

        def _parse_max_score(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        max_score = _parse_max_score(d.pop("max_score", UNSET))

        scores_definition = d.pop("scores_definition", UNSET)

        show_documentation_score = d.pop("show_documentation_score", UNSET)

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

        assets = []
        _assets = d.pop("assets", UNSET)
        for assets_item_data in _assets or []:
            assets_item = UUID(assets_item_data)

            assets.append(assets_item)

        compliance_assessment_write = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            framework=framework,
            baseline=baseline,
            ebios_rm_studies=ebios_rm_studies,
            create_applied_controls_from_suggestions=create_applied_controls_from_suggestions,
            is_published=is_published,
            description=description,
            eta=eta,
            due_date=due_date,
            version=version,
            status=status,
            observation=observation,
            selected_implementation_groups=selected_implementation_groups,
            ref_id=ref_id,
            min_score=min_score,
            max_score=max_score,
            scores_definition=scores_definition,
            show_documentation_score=show_documentation_score,
            folder=folder,
            perimeter=perimeter,
            authors=authors,
            reviewers=reviewers,
            assets=assets,
        )

        compliance_assessment_write.additional_properties = d
        return compliance_assessment_write

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
