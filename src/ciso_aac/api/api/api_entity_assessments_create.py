from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.entity_assessment_write import EntityAssessmentWrite
from ...types import Response


def _get_kwargs(
    *,
    body: EntityAssessmentWrite | EntityAssessmentWrite | EntityAssessmentWrite,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/entity-assessments/",
    }

    if isinstance(body, EntityAssessmentWrite):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, EntityAssessmentWrite):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, EntityAssessmentWrite):
        _files_body = body.to_multipart()

        _kwargs["files"] = _files_body
        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> EntityAssessmentWrite | None:
    if response.status_code == 201:
        response_201 = EntityAssessmentWrite.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EntityAssessmentWrite]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: EntityAssessmentWrite | EntityAssessmentWrite | EntityAssessmentWrite,
) -> Response[EntityAssessmentWrite]:
    """API endpoint that allows entity assessments to be viewed or edited.

    Args:
        body (EntityAssessmentWrite):
        body (EntityAssessmentWrite):
        body (EntityAssessmentWrite):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EntityAssessmentWrite]
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
    body: EntityAssessmentWrite | EntityAssessmentWrite | EntityAssessmentWrite,
) -> EntityAssessmentWrite | None:
    """API endpoint that allows entity assessments to be viewed or edited.

    Args:
        body (EntityAssessmentWrite):
        body (EntityAssessmentWrite):
        body (EntityAssessmentWrite):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EntityAssessmentWrite
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: EntityAssessmentWrite | EntityAssessmentWrite | EntityAssessmentWrite,
) -> Response[EntityAssessmentWrite]:
    """API endpoint that allows entity assessments to be viewed or edited.

    Args:
        body (EntityAssessmentWrite):
        body (EntityAssessmentWrite):
        body (EntityAssessmentWrite):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EntityAssessmentWrite]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: EntityAssessmentWrite | EntityAssessmentWrite | EntityAssessmentWrite,
) -> EntityAssessmentWrite | None:
    """API endpoint that allows entity assessments to be viewed or edited.

    Args:
        body (EntityAssessmentWrite):
        body (EntityAssessmentWrite):
        body (EntityAssessmentWrite):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EntityAssessmentWrite
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
