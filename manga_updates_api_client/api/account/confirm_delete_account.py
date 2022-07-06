from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.api_response_v1 import ApiResponseV1
from ...types import Response


def _get_kwargs(
    auth_hash: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/account/delete/confirm/{auth_hash}".format(client.base_url, auth_hash=auth_hash)

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
    auth_hash: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiResponseV1]:
    """confirm deletion of your account

    Args:
        auth_hash (str):

    Returns:
        Response[ApiResponseV1]
    """

    kwargs = _get_kwargs(
        auth_hash=auth_hash,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    auth_hash: str,
    *,
    client: AuthenticatedClient,
) -> Optional[ApiResponseV1]:
    """confirm deletion of your account

    Args:
        auth_hash (str):

    Returns:
        Response[ApiResponseV1]
    """

    return sync_detailed(
        auth_hash=auth_hash,
        client=client,
    ).parsed


async def asyncio_detailed(
    auth_hash: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiResponseV1]:
    """confirm deletion of your account

    Args:
        auth_hash (str):

    Returns:
        Response[ApiResponseV1]
    """

    kwargs = _get_kwargs(
        auth_hash=auth_hash,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    auth_hash: str,
    *,
    client: AuthenticatedClient,
) -> Optional[ApiResponseV1]:
    """confirm deletion of your account

    Args:
        auth_hash (str):

    Returns:
        Response[ApiResponseV1]
    """

    return (
        await asyncio_detailed(
            auth_hash=auth_hash,
            client=client,
        )
    ).parsed
