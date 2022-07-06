# manga-updates-api-client
A client library for accessing [MangaUpdates API](https://api.mangaupdates.com/)


## Usage
1. First, create a client:

    ```python
    from manga_updates_api_client import Client

    client = Client(base_url="https://api.mangaupdates.com/v1")
    ```

    If the endpoints you're going to hit require authentication, use `AuthenticatedClient` instead:

    ```python
    from manga_updates_api_client import AuthenticatedClient

    client = AuthenticatedClient(base_url="https://api.mangaupdates.com/v1", token="SuperSecretToken")
    ```

1. Now call your endpoint:

    ```python
    from manga_updates_api_client.api.series import retrieve_series

    response  = retrieve_series.sync_detailed(client=client, id=15090100540)
    ```

    Or do the same thing with an async version:

    ```python
    from manga_updates_api_client.models import MyDataModel
    from manga_updates_api_client.api.series import retrieve_series
    from manga_updates_api_client.types import Response

    response = await retrieve_series.asyncio_detailed(client=client, id=15090100540)
    ```

### Things to know
1. Every path/method combo becomes a Python module with four functions:
    1. `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.
    1. `asyncio_detailed`: Like `sync_detailed` but async instead of blocking

1. All path/query params, and bodies become method arguments.
1. If your endpoint had any tags on it, the first tag will be used as a module name for the function (series above)
1. Any endpoint which did not have a tag will be in `manga_updates_api_client.api.default`
