from typing import Any, Dict

import httpx

from ...client import AuthenticatedClient
from ...types import Response


def _get_kwargs(
    topic_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/forums/lookup/topic/{topic_id}".format(client.base_url, topic_id=topic_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    topic_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """lookup a topic to find the forum id

    Args:
        topic_id (int):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        topic_id=topic_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    topic_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """lookup a topic to find the forum id

    Args:
        topic_id (int):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        topic_id=topic_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
