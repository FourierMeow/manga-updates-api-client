from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    category_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/faq/{category_id}/questions".format(client.base_url, category_id=category_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List[Any]]]:
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 200:
        response_200 = cast(List[Any], response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List[Any]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    category_id: int,
    *,
    client: Client,
) -> Response[Union[Any, List[Any]]]:
    """retrieve all quesitons for a category

    Args:
        category_id (int):

    Returns:
        Response[Union[Any, List[Any]]]
    """

    kwargs = _get_kwargs(
        category_id=category_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    category_id: int,
    *,
    client: Client,
) -> Optional[Union[Any, List[Any]]]:
    """retrieve all quesitons for a category

    Args:
        category_id (int):

    Returns:
        Response[Union[Any, List[Any]]]
    """

    return sync_detailed(
        category_id=category_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    category_id: int,
    *,
    client: Client,
) -> Response[Union[Any, List[Any]]]:
    """retrieve all quesitons for a category

    Args:
        category_id (int):

    Returns:
        Response[Union[Any, List[Any]]]
    """

    kwargs = _get_kwargs(
        category_id=category_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    category_id: int,
    *,
    client: Client,
) -> Optional[Union[Any, List[Any]]]:
    """retrieve all quesitons for a category

    Args:
        category_id (int):

    Returns:
        Response[Union[Any, List[Any]]]
    """

    return (
        await asyncio_detailed(
            category_id=category_id,
            client=client,
        )
    ).parsed
