from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.risk_scenario_write import RiskScenarioWrite
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: RiskScenarioWrite | RiskScenarioWrite | RiskScenarioWrite,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/risk-scenarios/{id}/",
    }

    if isinstance(body, RiskScenarioWrite):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, RiskScenarioWrite):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, RiskScenarioWrite):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RiskScenarioWrite | None:
    if response.status_code == 200:
        response_200 = RiskScenarioWrite.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RiskScenarioWrite]:
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
    body: RiskScenarioWrite | RiskScenarioWrite | RiskScenarioWrite,
) -> Response[RiskScenarioWrite]:
    """API endpoint that allows risk scenarios to be viewed or edited.

    Args:
        id (str):
        body (RiskScenarioWrite):
        body (RiskScenarioWrite):
        body (RiskScenarioWrite):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RiskScenarioWrite]
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
    body: RiskScenarioWrite | RiskScenarioWrite | RiskScenarioWrite,
) -> RiskScenarioWrite | None:
    """API endpoint that allows risk scenarios to be viewed or edited.

    Args:
        id (str):
        body (RiskScenarioWrite):
        body (RiskScenarioWrite):
        body (RiskScenarioWrite):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RiskScenarioWrite
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
    body: RiskScenarioWrite | RiskScenarioWrite | RiskScenarioWrite,
) -> Response[RiskScenarioWrite]:
    """API endpoint that allows risk scenarios to be viewed or edited.

    Args:
        id (str):
        body (RiskScenarioWrite):
        body (RiskScenarioWrite):
        body (RiskScenarioWrite):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RiskScenarioWrite]
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
    body: RiskScenarioWrite | RiskScenarioWrite | RiskScenarioWrite,
) -> RiskScenarioWrite | None:
    """API endpoint that allows risk scenarios to be viewed or edited.

    Args:
        id (str):
        body (RiskScenarioWrite):
        body (RiskScenarioWrite):
        body (RiskScenarioWrite):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RiskScenarioWrite
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
