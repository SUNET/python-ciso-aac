from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_compliance_assessment_action_plan_list import PaginatedComplianceAssessmentActionPlanList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    limit: Unset | int = UNSET,
    offset: Unset | int = UNSET,
    ordering: Unset | str = UNSET,
    search: Unset | str = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["ordering"] = ordering

    params["search"] = search

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/compliance-assessments/{id}/action-plan/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedComplianceAssessmentActionPlanList | None:
    if response.status_code == 200:
        response_200 = PaginatedComplianceAssessmentActionPlanList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedComplianceAssessmentActionPlanList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    limit: Unset | int = UNSET,
    offset: Unset | int = UNSET,
    ordering: Unset | str = UNSET,
    search: Unset | str = UNSET,
) -> Response[PaginatedComplianceAssessmentActionPlanList]:
    """
    Args:
        id (UUID):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        search (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedComplianceAssessmentActionPlanList]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        offset=offset,
        ordering=ordering,
        search=search,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
    limit: Unset | int = UNSET,
    offset: Unset | int = UNSET,
    ordering: Unset | str = UNSET,
    search: Unset | str = UNSET,
) -> PaginatedComplianceAssessmentActionPlanList | None:
    """
    Args:
        id (UUID):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        search (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedComplianceAssessmentActionPlanList
    """

    return sync_detailed(
        id=id,
        client=client,
        limit=limit,
        offset=offset,
        ordering=ordering,
        search=search,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    limit: Unset | int = UNSET,
    offset: Unset | int = UNSET,
    ordering: Unset | str = UNSET,
    search: Unset | str = UNSET,
) -> Response[PaginatedComplianceAssessmentActionPlanList]:
    """
    Args:
        id (UUID):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        search (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedComplianceAssessmentActionPlanList]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        offset=offset,
        ordering=ordering,
        search=search,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    limit: Unset | int = UNSET,
    offset: Unset | int = UNSET,
    ordering: Unset | str = UNSET,
    search: Unset | str = UNSET,
) -> PaginatedComplianceAssessmentActionPlanList | None:
    """
    Args:
        id (UUID):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        search (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedComplianceAssessmentActionPlanList
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            limit=limit,
            offset=offset,
            ordering=ordering,
            search=search,
        )
    ).parsed
