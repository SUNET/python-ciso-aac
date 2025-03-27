from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patched_reference_control_write import PatchedReferenceControlWrite
from ...models.reference_control_write import ReferenceControlWrite
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: PatchedReferenceControlWrite | PatchedReferenceControlWrite | PatchedReferenceControlWrite,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/reference-controls/{id}/",
    }

    if isinstance(body, PatchedReferenceControlWrite):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedReferenceControlWrite):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedReferenceControlWrite):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ReferenceControlWrite | None:
    if response.status_code == 200:
        response_200 = ReferenceControlWrite.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ReferenceControlWrite]:
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
    body: PatchedReferenceControlWrite | PatchedReferenceControlWrite | PatchedReferenceControlWrite,
) -> Response[ReferenceControlWrite]:
    """API endpoint that allows reference controls to be viewed or edited.

    Args:
        id (str):
        body (PatchedReferenceControlWrite):
        body (PatchedReferenceControlWrite):
        body (PatchedReferenceControlWrite):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReferenceControlWrite]
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
    body: PatchedReferenceControlWrite | PatchedReferenceControlWrite | PatchedReferenceControlWrite,
) -> ReferenceControlWrite | None:
    """API endpoint that allows reference controls to be viewed or edited.

    Args:
        id (str):
        body (PatchedReferenceControlWrite):
        body (PatchedReferenceControlWrite):
        body (PatchedReferenceControlWrite):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReferenceControlWrite
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
    body: PatchedReferenceControlWrite | PatchedReferenceControlWrite | PatchedReferenceControlWrite,
) -> Response[ReferenceControlWrite]:
    """API endpoint that allows reference controls to be viewed or edited.

    Args:
        id (str):
        body (PatchedReferenceControlWrite):
        body (PatchedReferenceControlWrite):
        body (PatchedReferenceControlWrite):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReferenceControlWrite]
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
    body: PatchedReferenceControlWrite | PatchedReferenceControlWrite | PatchedReferenceControlWrite,
) -> ReferenceControlWrite | None:
    """API endpoint that allows reference controls to be viewed or edited.

    Args:
        id (str):
        body (PatchedReferenceControlWrite):
        body (PatchedReferenceControlWrite):
        body (PatchedReferenceControlWrite):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReferenceControlWrite
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
