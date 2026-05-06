from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Resource


class ServerVersion(Resource):
    """Retrieves version information for the specified server.

    **Tags:** System Information

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllServerVersion` (GET (list))
    - `getServerVersion` (GET)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    NAMESPACE = 'platform'
    PATH = '/info/serverversion/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
