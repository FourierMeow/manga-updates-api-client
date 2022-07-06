from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.api_response_v1 import ApiResponseV1
from ...types import Response


def _get_kwargs(
    captcha_response: str,
    *,
    client: Client,
    json_body: Any,
) -> Dict[str, Any]:
    url = "{}/account/forgotpass/{captcha_response}".format(client.base_url, captcha_response=captcha_response)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
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
    captcha_response: str,
    *,
    client: Client,
    json_body: Any,
) -> Response[ApiResponseV1]:
    """send a forgotten password email

    Args:
        captcha_response (str):
        json_body (Any):

    Returns:
        Response[ApiResponseV1]
    """

    kwargs = _get_kwargs(
        captcha_response=captcha_response,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    captcha_response: str,
    *,
    client: Client,
    json_body: Any,
) -> Optional[ApiResponseV1]:
    """send a forgotten password email

    Args:
        captcha_response (str):
        json_body (Any):

    Returns:
        Response[ApiResponseV1]
    """

    return sync_detailed(
        captcha_response=captcha_response,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    captcha_response: str,
    *,
    client: Client,
    json_body: Any,
) -> Response[ApiResponseV1]:
    """send a forgotten password email

    Args:
        captcha_response (str):
        json_body (Any):

    Returns:
        Response[ApiResponseV1]
    """

    kwargs = _get_kwargs(
        captcha_response=captcha_response,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    captcha_response: str,
    *,
    client: Client,
    json_body: Any,
) -> Optional[ApiResponseV1]:
    """send a forgotten password email

    Args:
        captcha_response (str):
        json_body (Any):

    Returns:
        Response[ApiResponseV1]
    """

    return (
        await asyncio_detailed(
            captcha_response=captcha_response,
            client=client,
            json_body=json_body,
        )
    ).parsed
