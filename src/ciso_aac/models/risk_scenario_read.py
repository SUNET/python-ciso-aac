import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define, field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RiskScenarioRead")


@_attrs_define
class RiskScenarioRead:
    """
    Attributes:
        id (UUID):
        risk_matrix (str):
        risk_assessment (str):
        perimeter (str):
        version (str):
        threats (list[str]):
        assets (list[str]):
        treatment (str):
        current_proba (Any):
        current_impact (Any):
        current_level (Any):
        residual_proba (Any):
        residual_impact (Any):
        residual_level (Any):
        strength_of_knowledge (Any):
        applied_controls (list[str]):
        existing_applied_controls (list[str]):
        owner (list[str]):
        security_exceptions (list[str]):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        name (str):
        is_published (Union[Unset, bool]):
        description (Union[None, Unset, str]):
        existing_controls (Union[Unset, str]): The existing controls to manage this risk. Edit the risk scenario to add
            extra applied controls.
        ref_id (Union[Unset, str]):
        qualifications (Union[Unset, Any]):
        justification (Union[None, Unset, str]):
        vulnerabilities (Union[Unset, list[UUID]]): Vulnerabities exploited by the risk scenario
    """

    id: UUID
    risk_matrix: str
    risk_assessment: str
    perimeter: str
    version: str
    threats: list[str]
    assets: list[str]
    treatment: str
    current_proba: Any
    current_impact: Any
    current_level: Any
    residual_proba: Any
    residual_impact: Any
    residual_level: Any
    strength_of_knowledge: Any
    applied_controls: list[str]
    existing_applied_controls: list[str]
    owner: list[str]
    security_exceptions: list[str]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: str
    is_published: Unset | bool = UNSET
    description: None | Unset | str = UNSET
    existing_controls: Unset | str = UNSET
    ref_id: Unset | str = UNSET
    qualifications: Unset | Any = UNSET
    justification: None | Unset | str = UNSET
    vulnerabilities: Unset | list[UUID] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        risk_matrix = self.risk_matrix

        risk_assessment = self.risk_assessment

        perimeter = self.perimeter

        version = self.version

        threats = self.threats

        assets = self.assets

        treatment = self.treatment

        current_proba = self.current_proba

        current_impact = self.current_impact

        current_level = self.current_level

        residual_proba = self.residual_proba

        residual_impact = self.residual_impact

        residual_level = self.residual_level

        strength_of_knowledge = self.strength_of_knowledge

        applied_controls = self.applied_controls

        existing_applied_controls = self.existing_applied_controls

        owner = self.owner

        security_exceptions = self.security_exceptions

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        name = self.name

        is_published = self.is_published

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        existing_controls = self.existing_controls

        ref_id = self.ref_id

        qualifications = self.qualifications

        justification: None | Unset | str
        if isinstance(self.justification, Unset):
            justification = UNSET
        else:
            justification = self.justification

        vulnerabilities: Unset | list[str] = UNSET
        if not isinstance(self.vulnerabilities, Unset):
            vulnerabilities = []
            for vulnerabilities_item_data in self.vulnerabilities:
                vulnerabilities_item = str(vulnerabilities_item_data)
                vulnerabilities.append(vulnerabilities_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "risk_matrix": risk_matrix,
                "risk_assessment": risk_assessment,
                "perimeter": perimeter,
                "version": version,
                "threats": threats,
                "assets": assets,
                "treatment": treatment,
                "current_proba": current_proba,
                "current_impact": current_impact,
                "current_level": current_level,
                "residual_proba": residual_proba,
                "residual_impact": residual_impact,
                "residual_level": residual_level,
                "strength_of_knowledge": strength_of_knowledge,
                "applied_controls": applied_controls,
                "existing_applied_controls": existing_applied_controls,
                "owner": owner,
                "security_exceptions": security_exceptions,
                "created_at": created_at,
                "updated_at": updated_at,
                "name": name,
            }
        )
        if is_published is not UNSET:
            field_dict["is_published"] = is_published
        if description is not UNSET:
            field_dict["description"] = description
        if existing_controls is not UNSET:
            field_dict["existing_controls"] = existing_controls
        if ref_id is not UNSET:
            field_dict["ref_id"] = ref_id
        if qualifications is not UNSET:
            field_dict["qualifications"] = qualifications
        if justification is not UNSET:
            field_dict["justification"] = justification
        if vulnerabilities is not UNSET:
            field_dict["vulnerabilities"] = vulnerabilities

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        risk_matrix = d.pop("risk_matrix")

        risk_assessment = d.pop("risk_assessment")

        perimeter = d.pop("perimeter")

        version = d.pop("version")

        threats = cast(list[str], d.pop("threats"))

        assets = cast(list[str], d.pop("assets"))

        treatment = d.pop("treatment")

        current_proba = d.pop("current_proba")

        current_impact = d.pop("current_impact")

        current_level = d.pop("current_level")

        residual_proba = d.pop("residual_proba")

        residual_impact = d.pop("residual_impact")

        residual_level = d.pop("residual_level")

        strength_of_knowledge = d.pop("strength_of_knowledge")

        applied_controls = cast(list[str], d.pop("applied_controls"))

        existing_applied_controls = cast(list[str], d.pop("existing_applied_controls"))

        owner = cast(list[str], d.pop("owner"))

        security_exceptions = cast(list[str], d.pop("security_exceptions"))

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

        existing_controls = d.pop("existing_controls", UNSET)

        ref_id = d.pop("ref_id", UNSET)

        qualifications = d.pop("qualifications", UNSET)

        def _parse_justification(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        justification = _parse_justification(d.pop("justification", UNSET))

        vulnerabilities = []
        _vulnerabilities = d.pop("vulnerabilities", UNSET)
        for vulnerabilities_item_data in _vulnerabilities or []:
            vulnerabilities_item = UUID(vulnerabilities_item_data)

            vulnerabilities.append(vulnerabilities_item)

        risk_scenario_read = cls(
            id=id,
            risk_matrix=risk_matrix,
            risk_assessment=risk_assessment,
            perimeter=perimeter,
            version=version,
            threats=threats,
            assets=assets,
            treatment=treatment,
            current_proba=current_proba,
            current_impact=current_impact,
            current_level=current_level,
            residual_proba=residual_proba,
            residual_impact=residual_impact,
            residual_level=residual_level,
            strength_of_knowledge=strength_of_knowledge,
            applied_controls=applied_controls,
            existing_applied_controls=existing_applied_controls,
            owner=owner,
            security_exceptions=security_exceptions,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            is_published=is_published,
            description=description,
            existing_controls=existing_controls,
            ref_id=ref_id,
            qualifications=qualifications,
            justification=justification,
            vulnerabilities=vulnerabilities,
        )

        risk_scenario_read.additional_properties = d
        return risk_scenario_read

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
