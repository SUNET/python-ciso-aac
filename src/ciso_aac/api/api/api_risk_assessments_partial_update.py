from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patched_risk_assessment_write import PatchedRiskAssessmentWrite
from ...models.risk_assessment_write import RiskAssessmentWrite
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: Union[
        PatchedRiskAssessmentWrite,
        PatchedRiskAssessmentWrite,
        PatchedRiskAssessmentWrite,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/risk-assessments/{id}/",
    }

    if isinstance(body, PatchedRiskAssessmentWrite):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedRiskAssessmentWrite):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedRiskAssessmentWrite):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[RiskAssessmentWrite]:
    if response.status_code == 200:
        response_200 = RiskAssessmentWrite.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[RiskAssessmentWrite]:
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
    body: Union[
        PatchedRiskAssessmentWrite,
        PatchedRiskAssessmentWrite,
        PatchedRiskAssessmentWrite,
    ],
) -> Response[RiskAssessmentWrite]:
    """API endpoint that allows risk assessments to be viewed or edited.

    Args:
        id (str):
        body (PatchedRiskAssessmentWrite):
        body (PatchedRiskAssessmentWrite):
        body (PatchedRiskAssessmentWrite):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RiskAssessmentWrite]
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
    body: Union[
        PatchedRiskAssessmentWrite,
        PatchedRiskAssessmentWrite,
        PatchedRiskAssessmentWrite,
    ],
) -> Optional[RiskAssessmentWrite]:
    """API endpoint that allows risk assessments to be viewed or edited.

    Args:
        id (str):
        body (PatchedRiskAssessmentWrite):
        body (PatchedRiskAssessmentWrite):
        body (PatchedRiskAssessmentWrite):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RiskAssessmentWrite
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
    body: Union[
        PatchedRiskAssessmentWrite,
        PatchedRiskAssessmentWrite,
        PatchedRiskAssessmentWrite,
    ],
) -> Response[RiskAssessmentWrite]:
    """API endpoint that allows risk assessments to be viewed or edited.

    Args:
        id (str):
        body (PatchedRiskAssessmentWrite):
        body (PatchedRiskAssessmentWrite):
        body (PatchedRiskAssessmentWrite):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RiskAssessmentWrite]
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
    body: Union[
        PatchedRiskAssessmentWrite,
        PatchedRiskAssessmentWrite,
        PatchedRiskAssessmentWrite,
    ],
) -> Optional[RiskAssessmentWrite]:
    """API endpoint that allows risk assessments to be viewed or edited.

    Args:
        id (str):
        body (PatchedRiskAssessmentWrite):
        body (PatchedRiskAssessmentWrite):
        body (PatchedRiskAssessmentWrite):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RiskAssessmentWrite
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
