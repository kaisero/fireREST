from fireREST.defaults import API_RELEASE_730
from fireREST.fmc import Resource


class PathMonitoredInterface(Resource):
    """[DEV ERROR: Missing description]

    **Tags:** Health

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllPathMonitoredInterface` (GET (list))

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/health/pathmonitoredinterfaces/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_730
