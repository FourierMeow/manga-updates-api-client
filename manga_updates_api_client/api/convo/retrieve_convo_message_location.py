from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.api_response_v1 import ApiResponseV1
from ...types import Response


def _get_kwargs(
    id: int,
    message_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/convo/{id}/messages/{message_id}/location".format(client.base_url, id=id, message_id=message_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[ApiResponseV1]:
    if response.status_code == 200:
        response_200 = ApiResponseV1.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ApiResponseV1]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: int,
    message_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ApiResponseV1]:
    """get a specific convo message location

    Args:
        id (int):
        message_id (int):

    Returns:
        Response[ApiResponseV1]
    """

    kwargs = _get_kwargs(
        id=id,
        message_id=message_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: int,
    message_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[ApiResponseV1]:
    """get a specific convo message location

    Args:
        id (int):
        message_id (int):

    Returns:
        Response[ApiResponseV1]
    """

    return sync_detailed(
        id=id,
        message_id=message_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: int,
    message_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ApiResponseV1]:
    """get a specific convo message location

    Args:
        id (int):
        message_id (int):

    Returns:
        Response[ApiResponseV1]
    """

    kwargs = _get_kwargs(
        id=id,
        message_id=message_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: int,
    message_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[ApiResponseV1]:
    """get a specific convo message location

    Args:
        id (int):
        message_id (int):

    Returns:
        Response[ApiResponseV1]
    """

    return (
        await asyncio_detailed(
            id=id,
            message_id=message_id,
            client=client,
        )
    ).parsed
