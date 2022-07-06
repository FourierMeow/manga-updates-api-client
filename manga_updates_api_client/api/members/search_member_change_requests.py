from typing import Any, Dict, Union

import httpx

from ...client import AuthenticatedClient
from ...models.search_member_change_requests_asc import SearchMemberChangeRequestsAsc
from ...models.search_member_change_requests_orderby import SearchMemberChangeRequestsOrderby
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, None, int] = UNSET,
    perpage: Union[Unset, None, int] = UNSET,
    orderby: Union[Unset, None, SearchMemberChangeRequestsOrderby] = SearchMemberChangeRequestsOrderby.TIME,
    asc: Union[Unset, None, SearchMemberChangeRequestsAsc] = SearchMemberChangeRequestsAsc.ASC,
) -> Dict[str, Any]:
    url = "{}/members/{id}/requests".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params["perpage"] = perpage

    json_orderby: Union[Unset, None, str] = UNSET
    if not isinstance(orderby, Unset):
        json_orderby = orderby.value if orderby else None

    params["orderby"] = json_orderby

    json_asc: Union[Unset, None, str] = UNSET
    if not isinstance(asc, Unset):
        json_asc = asc.value if asc else None

    params["asc"] = json_asc

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, None, int] = UNSET,
    perpage: Union[Unset, None, int] = UNSET,
    orderby: Union[Unset, None, SearchMemberChangeRequestsOrderby] = SearchMemberChangeRequestsOrderby.TIME,
    asc: Union[Unset, None, SearchMemberChangeRequestsAsc] = SearchMemberChangeRequestsAsc.ASC,
) -> Response[Any]:
    """search change requests for a specific user

    Args:
        id (int):
        page (Union[Unset, None, int]):
        perpage (Union[Unset, None, int]):
        orderby (Union[Unset, None, SearchMemberChangeRequestsOrderby]):  Default:
            SearchMemberChangeRequestsOrderby.TIME.
        asc (Union[Unset, None, SearchMemberChangeRequestsAsc]):  Default:
            SearchMemberChangeRequestsAsc.ASC.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        page=page,
        perpage=perpage,
        orderby=orderby,
        asc=asc,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, None, int] = UNSET,
    perpage: Union[Unset, None, int] = UNSET,
    orderby: Union[Unset, None, SearchMemberChangeRequestsOrderby] = SearchMemberChangeRequestsOrderby.TIME,
    asc: Union[Unset, None, SearchMemberChangeRequestsAsc] = SearchMemberChangeRequestsAsc.ASC,
) -> Response[Any]:
    """search change requests for a specific user

    Args:
        id (int):
        page (Union[Unset, None, int]):
        perpage (Union[Unset, None, int]):
        orderby (Union[Unset, None, SearchMemberChangeRequestsOrderby]):  Default:
            SearchMemberChangeRequestsOrderby.TIME.
        asc (Union[Unset, None, SearchMemberChangeRequestsAsc]):  Default:
            SearchMemberChangeRequestsAsc.ASC.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        page=page,
        perpage=perpage,
        orderby=orderby,
        asc=asc,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
