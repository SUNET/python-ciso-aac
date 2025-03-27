from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_stored_libraries_list_object_type_item import ApiStoredLibrariesListObjectTypeItem
from ...models.paginated_stored_library_list import PaginatedStoredLibraryList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Unset | int = UNSET,
    locale: Unset | str = UNSET,
    object_type: Unset | list[ApiStoredLibrariesListObjectTypeItem] = UNSET,
    offset: Unset | int = UNSET,
    ordering: Unset | str = UNSET,
    packager: Unset | str = UNSET,
    provider: Unset | str = UNSET,
    search: Unset | str = UNSET,
    urn: Unset | str = UNSET,
    version: Unset | int = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["locale"] = locale

    json_object_type: Unset | list[str] = UNSET
    if not isinstance(object_type, Unset):
        json_object_type = []
        for object_type_item_data in object_type:
            object_type_item = object_type_item_data.value
            json_object_type.append(object_type_item)

    params["object_type"] = json_object_type

    params["offset"] = offset

    params["ordering"] = ordering

    params["packager"] = packager

    params["provider"] = provider

    params["search"] = search

    params["urn"] = urn

    params["version"] = version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/stored-libraries/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedStoredLibraryList | None:
    if response.status_code == 200:
        response_200 = PaginatedStoredLibraryList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedStoredLibraryList]:
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
    locale: Unset | str = UNSET,
    object_type: Unset | list[ApiStoredLibrariesListObjectTypeItem] = UNSET,
    offset: Unset | int = UNSET,
    ordering: Unset | str = UNSET,
    packager: Unset | str = UNSET,
    provider: Unset | str = UNSET,
    search: Unset | str = UNSET,
    urn: Unset | str = UNSET,
    version: Unset | int = UNSET,
) -> Response[PaginatedStoredLibraryList]:
    """
    Args:
        limit (Union[Unset, int]):
        locale (Union[Unset, str]):
        object_type (Union[Unset, list[ApiStoredLibrariesListObjectTypeItem]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        packager (Union[Unset, str]):
        provider (Union[Unset, str]):
        search (Union[Unset, str]):
        urn (Union[Unset, str]):
        version (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedStoredLibraryList]
    """

    kwargs = _get_kwargs(
        limit=limit,
        locale=locale,
        object_type=object_type,
        offset=offset,
        ordering=ordering,
        packager=packager,
        provider=provider,
        search=search,
        urn=urn,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: Unset | int = UNSET,
    locale: Unset | str = UNSET,
    object_type: Unset | list[ApiStoredLibrariesListObjectTypeItem] = UNSET,
    offset: Unset | int = UNSET,
    ordering: Unset | str = UNSET,
    packager: Unset | str = UNSET,
    provider: Unset | str = UNSET,
    search: Unset | str = UNSET,
    urn: Unset | str = UNSET,
    version: Unset | int = UNSET,
) -> PaginatedStoredLibraryList | None:
    """
    Args:
        limit (Union[Unset, int]):
        locale (Union[Unset, str]):
        object_type (Union[Unset, list[ApiStoredLibrariesListObjectTypeItem]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        packager (Union[Unset, str]):
        provider (Union[Unset, str]):
        search (Union[Unset, str]):
        urn (Union[Unset, str]):
        version (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedStoredLibraryList
    """

    return sync_detailed(
        client=client,
        limit=limit,
        locale=locale,
        object_type=object_type,
        offset=offset,
        ordering=ordering,
        packager=packager,
        provider=provider,
        search=search,
        urn=urn,
        version=version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: Unset | int = UNSET,
    locale: Unset | str = UNSET,
    object_type: Unset | list[ApiStoredLibrariesListObjectTypeItem] = UNSET,
    offset: Unset | int = UNSET,
    ordering: Unset | str = UNSET,
    packager: Unset | str = UNSET,
    provider: Unset | str = UNSET,
    search: Unset | str = UNSET,
    urn: Unset | str = UNSET,
    version: Unset | int = UNSET,
) -> Response[PaginatedStoredLibraryList]:
    """
    Args:
        limit (Union[Unset, int]):
        locale (Union[Unset, str]):
        object_type (Union[Unset, list[ApiStoredLibrariesListObjectTypeItem]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        packager (Union[Unset, str]):
        provider (Union[Unset, str]):
        search (Union[Unset, str]):
        urn (Union[Unset, str]):
        version (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedStoredLibraryList]
    """

    kwargs = _get_kwargs(
        limit=limit,
        locale=locale,
        object_type=object_type,
        offset=offset,
        ordering=ordering,
        packager=packager,
        provider=provider,
        search=search,
        urn=urn,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: Unset | int = UNSET,
    locale: Unset | str = UNSET,
    object_type: Unset | list[ApiStoredLibrariesListObjectTypeItem] = UNSET,
    offset: Unset | int = UNSET,
    ordering: Unset | str = UNSET,
    packager: Unset | str = UNSET,
    provider: Unset | str = UNSET,
    search: Unset | str = UNSET,
    urn: Unset | str = UNSET,
    version: Unset | int = UNSET,
) -> PaginatedStoredLibraryList | None:
    """
    Args:
        limit (Union[Unset, int]):
        locale (Union[Unset, str]):
        object_type (Union[Unset, list[ApiStoredLibrariesListObjectTypeItem]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        packager (Union[Unset, str]):
        provider (Union[Unset, str]):
        search (Union[Unset, str]):
        urn (Union[Unset, str]):
        version (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedStoredLibraryList
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            locale=locale,
            object_type=object_type,
            offset=offset,
            ordering=ordering,
            packager=packager,
            provider=provider,
            search=search,
            urn=urn,
            version=version,
        )
    ).parsed
