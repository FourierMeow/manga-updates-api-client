from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.api_response_v1 import ApiResponseV1
from ...types import Response


def _get_kwargs(
    forum_id: int,
    topic_id: int,
    post_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/forums/{forum_id}/topics/{topic_id}/posts/{post_id}/location".format(
        client.base_url, forum_id=forum_id, topic_id=topic_id, post_id=post_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ApiResponseV1]]:
    if response.status_code == 200:
        response_200 = ApiResponseV1.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ApiResponseV1]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    forum_id: int,
    topic_id: int,
    post_id: int,
    *,
    client: Client,
) -> Response[Union[Any, ApiResponseV1]]:
    """retrieve a forum post location within topic

    Args:
        forum_id (int):
        topic_id (int):
        post_id (int):

    Returns:
        Response[Union[Any, ApiResponseV1]]
    """

    kwargs = _get_kwargs(
        forum_id=forum_id,
        topic_id=topic_id,
        post_id=post_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    forum_id: int,
    topic_id: int,
    post_id: int,
    *,
    client: Client,
) -> Optional[Union[Any, ApiResponseV1]]:
    """retrieve a forum post location within topic

    Args:
        forum_id (int):
        topic_id (int):
        post_id (int):

    Returns:
        Response[Union[Any, ApiResponseV1]]
    """

    return sync_detailed(
        forum_id=forum_id,
        topic_id=topic_id,
        post_id=post_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    forum_id: int,
    topic_id: int,
    post_id: int,
    *,
    client: Client,
) -> Response[Union[Any, ApiResponseV1]]:
    """retrieve a forum post location within topic

    Args:
        forum_id (int):
        topic_id (int):
        post_id (int):

    Returns:
        Response[Union[Any, ApiResponseV1]]
    """

    kwargs = _get_kwargs(
        forum_id=forum_id,
        topic_id=topic_id,
        post_id=post_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    forum_id: int,
    topic_id: int,
    post_id: int,
    *,
    client: Client,
) -> Optional[Union[Any, ApiResponseV1]]:
    """retrieve a forum post location within topic

    Args:
        forum_id (int):
        topic_id (int):
        post_id (int):

    Returns:
        Response[Union[Any, ApiResponseV1]]
    """

    return (
        await asyncio_detailed(
            forum_id=forum_id,
            topic_id=topic_id,
            post_id=post_id,
            client=client,
        )
    ).parsed
