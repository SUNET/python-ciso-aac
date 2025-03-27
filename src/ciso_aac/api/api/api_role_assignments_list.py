from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_role_assignment_read_list import PaginatedRoleAssignmentReadList
from ...types import UNSET, Response, Unset


def _get_kwargs(
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
        "url": "/api/role-assignments/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedRoleAssignmentReadList | None:
    if response.status_code == 200:
        response_200 = PaginatedRoleAssignmentReadList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedRoleAssignmentReadList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: Unset | int = UNSET,
    offset: Unset | int = UNSET,
    ordering: Unset | str = UNSET,
    search: Unset | str = UNSET,
) -> Response[PaginatedRoleAssignmentReadList]:
    """API endpoint that allows role assignments to be viewed or edited.

    Args:
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        search (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedRoleAssignmentReadList]
    """

    kwargs = _get_kwargs(
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
    *,
    client: AuthenticatedClient,
    limit: Unset | int = UNSET,
    offset: Unset | int = UNSET,
    ordering: Unset | str = UNSET,
    search: Unset | str = UNSET,
) -> PaginatedRoleAssignmentReadList | None:
    """API endpoint that allows role assignments to be viewed or edited.

    Args:
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        search (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedRoleAssignmentReadList
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        ordering=ordering,
        search=search,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: Unset | int = UNSET,
    offset: Unset | int = UNSET,
    ordering: Unset | str = UNSET,
    search: Unset | str = UNSET,
) -> Response[PaginatedRoleAssignmentReadList]:
    """API endpoint that allows role assignments to be viewed or edited.

    Args:
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        search (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedRoleAssignmentReadList]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        ordering=ordering,
        search=search,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: Unset | int = UNSET,
    offset: Unset | int = UNSET,
    ordering: Unset | str = UNSET,
    search: Unset | str = UNSET,
) -> PaginatedRoleAssignmentReadList | None:
    """API endpoint that allows role assignments to be viewed or edited.

    Args:
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        search (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedRoleAssignmentReadList
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            ordering=ordering,
            search=search,
        )
    ).parsed
