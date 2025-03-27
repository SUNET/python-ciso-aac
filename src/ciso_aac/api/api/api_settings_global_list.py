from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_global_settings_list import PaginatedGlobalSettingsList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Unset | int = UNSET,
    offset: Unset | int = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/settings/global/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedGlobalSettingsList | None:
    if response.status_code == 200:
        response_200 = PaginatedGlobalSettingsList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedGlobalSettingsList]:
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
) -> Response[PaginatedGlobalSettingsList]:
    """
    Args:
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedGlobalSettingsList]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
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
) -> PaginatedGlobalSettingsList | None:
    """
    Args:
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedGlobalSettingsList
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: Unset | int = UNSET,
    offset: Unset | int = UNSET,
) -> Response[PaginatedGlobalSettingsList]:
    """
    Args:
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedGlobalSettingsList]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: Unset | int = UNSET,
    offset: Unset | int = UNSET,
) -> PaginatedGlobalSettingsList | None:
    """
    Args:
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedGlobalSettingsList
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
        )
    ).parsed
