from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Resource


class EndpointDeviceType(Resource):
    """Retrieves the endpoint device type object associated with the specified ID. If no ID is specified, retrieves list of all endpoint device type objects.

    **Tags:** Object

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllEndPointDeviceType` (GET (list))
    - `getEndPointDeviceType` (GET)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/object/endpointdevicetypes/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
