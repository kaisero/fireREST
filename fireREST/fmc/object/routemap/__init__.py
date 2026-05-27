from fireREST.defaults import API_RELEASE_660, API_RELEASE_710
from fireREST.fmc import Resource


class RouteMap(Resource):
    """Retrieves, deletes, creates or modifies the RouteMap with the specified ID. If no ID is specified, retrieves all RouteMap objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllRouteMap` (GET (list))
    - `getRouteMap` (GET)
    - `createRouteMap` (CREATE)
    - `updateRouteMap` (UPDATE)
    - `deleteRouteMap` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/object/routemaps/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_660
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_710
