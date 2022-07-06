from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.api_response_v1 import ApiResponseV1
from ...types import Response


def _get_kwargs(
    answer_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/poll/vote/{answer_id}".format(client.base_url, answer_id=answer_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[ApiResponseV1]:
    if response.status_code == 200:
        response_200 = ApiResponseV1.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ApiResponseV1.from_dict(response.json())

        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[ApiResponseV1]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    answer_id: int,
    *,
    client: Client,
) -> Response[ApiResponseV1]:
    """vote in a poll answer

    Args:
        answer_id (int):

    Returns:
        Response[ApiResponseV1]
    """

    kwargs = _get_kwargs(
        answer_id=answer_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    answer_id: int,
    *,
    client: Client,
) -> Optional[ApiResponseV1]:
    """vote in a poll answer

    Args:
        answer_id (int):

    Returns:
        Response[ApiResponseV1]
    """

    return sync_detailed(
        answer_id=answer_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    answer_id: int,
    *,
    client: Client,
) -> Response[ApiResponseV1]:
    """vote in a poll answer

    Args:
        answer_id (int):

    Returns:
        Response[ApiResponseV1]
    """

    kwargs = _get_kwargs(
        answer_id=answer_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    answer_id: int,
    *,
    client: Client,
) -> Optional[ApiResponseV1]:
    """vote in a poll answer

    Args:
        answer_id (int):

    Returns:
        Response[ApiResponseV1]
    """

    return (
        await asyncio_detailed(
            answer_id=answer_id,
            client=client,
        )
    ).parsed
