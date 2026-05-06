from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Resource


class Port(Resource):
    """Retrieves list of all port objects.

    **Tags:** Object

    **Supported operations:** GET

    **Operation IDs:**

    - `getPortObject` (GET (list))

    **Query parameters:**

    - `filter` (string, optional): To be used in conjunction with `"unusedOnly:true"` to search for unused objects and `"nameOrValue:{nameOrValue}"` to search for both name and value.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/object/ports/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
