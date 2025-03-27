from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.change_password import ChangePassword
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        ChangePassword,
        ChangePassword,
        ChangePassword,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/iam/change-password/",
    }

    if isinstance(body, ChangePassword):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, ChangePassword):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ChangePassword):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ChangePassword]:
    if response.status_code == 200:
        response_200 = ChangePassword.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ChangePassword]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        ChangePassword,
        ChangePassword,
        ChangePassword,
    ],
) -> Response[ChangePassword]:
    """An endpoint for changing password.

    Args:
        body (ChangePassword): Serializer for password change endpoint.
        body (ChangePassword): Serializer for password change endpoint.
        body (ChangePassword): Serializer for password change endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChangePassword]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: Union[
        ChangePassword,
        ChangePassword,
        ChangePassword,
    ],
) -> Optional[ChangePassword]:
    """An endpoint for changing password.

    Args:
        body (ChangePassword): Serializer for password change endpoint.
        body (ChangePassword): Serializer for password change endpoint.
        body (ChangePassword): Serializer for password change endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChangePassword
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        ChangePassword,
        ChangePassword,
        ChangePassword,
    ],
) -> Response[ChangePassword]:
    """An endpoint for changing password.

    Args:
        body (ChangePassword): Serializer for password change endpoint.
        body (ChangePassword): Serializer for password change endpoint.
        body (ChangePassword): Serializer for password change endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChangePassword]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Union[
        ChangePassword,
        ChangePassword,
        ChangePassword,
    ],
) -> Optional[ChangePassword]:
    """An endpoint for changing password.

    Args:
        body (ChangePassword): Serializer for password change endpoint.
        body (ChangePassword): Serializer for password change endpoint.
        body (ChangePassword): Serializer for password change endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChangePassword
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
