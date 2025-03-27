from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_user_read_list import PaginatedUserReadList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    email: Unset | str = UNSET,
    first_name: Unset | str = UNSET,
    is_active: Unset | bool = UNSET,
    is_applied_control_owner: Unset | bool = UNSET,
    is_approver: Unset | bool = UNSET,
    is_third_party: Unset | bool = UNSET,
    last_name: Unset | str = UNSET,
    limit: Unset | int = UNSET,
    offset: Unset | int = UNSET,
    ordering: Unset | str = UNSET,
    search: Unset | str = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["email"] = email

    params["first_name"] = first_name

    params["is_active"] = is_active

    params["is_applied_control_owner"] = is_applied_control_owner

    params["is_approver"] = is_approver

    params["is_third_party"] = is_third_party

    params["last_name"] = last_name

    params["limit"] = limit

    params["offset"] = offset

    params["ordering"] = ordering

    params["search"] = search

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/users/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PaginatedUserReadList | None:
    if response.status_code == 200:
        response_200 = PaginatedUserReadList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedUserReadList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    email: Unset | str = UNSET,
    first_name: Unset | str = UNSET,
    is_active: Unset | bool = UNSET,
    is_applied_control_owner: Unset | bool = UNSET,
    is_approver: Unset | bool = UNSET,
    is_third_party: Unset | bool = UNSET,
    last_name: Unset | str = UNSET,
    limit: Unset | int = UNSET,
    offset: Unset | int = UNSET,
    ordering: Unset | str = UNSET,
    search: Unset | str = UNSET,
) -> Response[PaginatedUserReadList]:
    """API endpoint that allows users to be viewed or edited

    Args:
        email (Union[Unset, str]):
        first_name (Union[Unset, str]):
        is_active (Union[Unset, bool]):
        is_applied_control_owner (Union[Unset, bool]):
        is_approver (Union[Unset, bool]):
        is_third_party (Union[Unset, bool]):
        last_name (Union[Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        search (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedUserReadList]
    """

    kwargs = _get_kwargs(
        email=email,
        first_name=first_name,
        is_active=is_active,
        is_applied_control_owner=is_applied_control_owner,
        is_approver=is_approver,
        is_third_party=is_third_party,
        last_name=last_name,
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
    email: Unset | str = UNSET,
    first_name: Unset | str = UNSET,
    is_active: Unset | bool = UNSET,
    is_applied_control_owner: Unset | bool = UNSET,
    is_approver: Unset | bool = UNSET,
    is_third_party: Unset | bool = UNSET,
    last_name: Unset | str = UNSET,
    limit: Unset | int = UNSET,
    offset: Unset | int = UNSET,
    ordering: Unset | str = UNSET,
    search: Unset | str = UNSET,
) -> PaginatedUserReadList | None:
    """API endpoint that allows users to be viewed or edited

    Args:
        email (Union[Unset, str]):
        first_name (Union[Unset, str]):
        is_active (Union[Unset, bool]):
        is_applied_control_owner (Union[Unset, bool]):
        is_approver (Union[Unset, bool]):
        is_third_party (Union[Unset, bool]):
        last_name (Union[Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        search (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedUserReadList
    """

    return sync_detailed(
        client=client,
        email=email,
        first_name=first_name,
        is_active=is_active,
        is_applied_control_owner=is_applied_control_owner,
        is_approver=is_approver,
        is_third_party=is_third_party,
        last_name=last_name,
        limit=limit,
        offset=offset,
        ordering=ordering,
        search=search,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    email: Unset | str = UNSET,
    first_name: Unset | str = UNSET,
    is_active: Unset | bool = UNSET,
    is_applied_control_owner: Unset | bool = UNSET,
    is_approver: Unset | bool = UNSET,
    is_third_party: Unset | bool = UNSET,
    last_name: Unset | str = UNSET,
    limit: Unset | int = UNSET,
    offset: Unset | int = UNSET,
    ordering: Unset | str = UNSET,
    search: Unset | str = UNSET,
) -> Response[PaginatedUserReadList]:
    """API endpoint that allows users to be viewed or edited

    Args:
        email (Union[Unset, str]):
        first_name (Union[Unset, str]):
        is_active (Union[Unset, bool]):
        is_applied_control_owner (Union[Unset, bool]):
        is_approver (Union[Unset, bool]):
        is_third_party (Union[Unset, bool]):
        last_name (Union[Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        search (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedUserReadList]
    """

    kwargs = _get_kwargs(
        email=email,
        first_name=first_name,
        is_active=is_active,
        is_applied_control_owner=is_applied_control_owner,
        is_approver=is_approver,
        is_third_party=is_third_party,
        last_name=last_name,
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
    email: Unset | str = UNSET,
    first_name: Unset | str = UNSET,
    is_active: Unset | bool = UNSET,
    is_applied_control_owner: Unset | bool = UNSET,
    is_approver: Unset | bool = UNSET,
    is_third_party: Unset | bool = UNSET,
    last_name: Unset | str = UNSET,
    limit: Unset | int = UNSET,
    offset: Unset | int = UNSET,
    ordering: Unset | str = UNSET,
    search: Unset | str = UNSET,
) -> PaginatedUserReadList | None:
    """API endpoint that allows users to be viewed or edited

    Args:
        email (Union[Unset, str]):
        first_name (Union[Unset, str]):
        is_active (Union[Unset, bool]):
        is_applied_control_owner (Union[Unset, bool]):
        is_approver (Union[Unset, bool]):
        is_third_party (Union[Unset, bool]):
        last_name (Union[Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        search (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedUserReadList
    """

    return (
        await asyncio_detailed(
            client=client,
            email=email,
            first_name=first_name,
            is_active=is_active,
            is_applied_control_owner=is_applied_control_owner,
            is_approver=is_approver,
            is_third_party=is_third_party,
            last_name=last_name,
            limit=limit,
            offset=offset,
            ordering=ordering,
            search=search,
        )
    ).parsed
