from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.api_response_v1 import ApiResponseV1
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    pubname: str,
) -> Dict[str, Any]:
    url = "{}/publishers/publication".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["pubname"] = pubname

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ApiResponseV1]]:
    if response.status_code == 400:
        response_400 = ApiResponseV1.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 200:
        response_200 = cast(Any, response.json())
        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ApiResponseV1]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    pubname: str,
) -> Response[Union[Any, ApiResponseV1]]:
    """get the list of series for a specific publication

    Args:
        pubname (str):

    Returns:
        Response[Union[Any, ApiResponseV1]]
    """

    kwargs = _get_kwargs(
        client=client,
        pubname=pubname,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    pubname: str,
) -> Optional[Union[Any, ApiResponseV1]]:
    """get the list of series for a specific publication

    Args:
        pubname (str):

    Returns:
        Response[Union[Any, ApiResponseV1]]
    """

    return sync_detailed(
        client=client,
        pubname=pubname,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    pubname: str,
) -> Response[Union[Any, ApiResponseV1]]:
    """get the list of series for a specific publication

    Args:
        pubname (str):

    Returns:
        Response[Union[Any, ApiResponseV1]]
    """

    kwargs = _get_kwargs(
        client=client,
        pubname=pubname,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    pubname: str,
) -> Optional[Union[Any, ApiResponseV1]]:
    """get the list of series for a specific publication

    Args:
        pubname (str):

    Returns:
        Response[Union[Any, ApiResponseV1]]
    """

    return (
        await asyncio_detailed(
            client=client,
            pubname=pubname,
        )
    ).parsed
