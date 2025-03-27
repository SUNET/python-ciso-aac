from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patched_requirement_mapping_set_write import PatchedRequirementMappingSetWrite
from ...models.requirement_mapping_set_write import RequirementMappingSetWrite
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: PatchedRequirementMappingSetWrite | PatchedRequirementMappingSetWrite | PatchedRequirementMappingSetWrite,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/requirement-mapping-sets/{id}/",
    }

    if isinstance(body, PatchedRequirementMappingSetWrite):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedRequirementMappingSetWrite):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedRequirementMappingSetWrite):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RequirementMappingSetWrite | None:
    if response.status_code == 200:
        response_200 = RequirementMappingSetWrite.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RequirementMappingSetWrite]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PatchedRequirementMappingSetWrite | PatchedRequirementMappingSetWrite | PatchedRequirementMappingSetWrite,
) -> Response[RequirementMappingSetWrite]:
    """
    Args:
        id (str):
        body (PatchedRequirementMappingSetWrite):
        body (PatchedRequirementMappingSetWrite):
        body (PatchedRequirementMappingSetWrite):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequirementMappingSetWrite]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PatchedRequirementMappingSetWrite | PatchedRequirementMappingSetWrite | PatchedRequirementMappingSetWrite,
) -> RequirementMappingSetWrite | None:
    """
    Args:
        id (str):
        body (PatchedRequirementMappingSetWrite):
        body (PatchedRequirementMappingSetWrite):
        body (PatchedRequirementMappingSetWrite):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequirementMappingSetWrite
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PatchedRequirementMappingSetWrite | PatchedRequirementMappingSetWrite | PatchedRequirementMappingSetWrite,
) -> Response[RequirementMappingSetWrite]:
    """
    Args:
        id (str):
        body (PatchedRequirementMappingSetWrite):
        body (PatchedRequirementMappingSetWrite):
        body (PatchedRequirementMappingSetWrite):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RequirementMappingSetWrite]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PatchedRequirementMappingSetWrite | PatchedRequirementMappingSetWrite | PatchedRequirementMappingSetWrite,
) -> RequirementMappingSetWrite | None:
    """
    Args:
        id (str):
        body (PatchedRequirementMappingSetWrite):
        body (PatchedRequirementMappingSetWrite):
        body (PatchedRequirementMappingSetWrite):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RequirementMappingSetWrite
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
