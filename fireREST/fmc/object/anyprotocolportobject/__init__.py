from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Resource


class AnyProtocolPortObject(Resource):
    """Retrieves any protocol port object associated with the specified ID. If no ID is specified for a GET, retrieves list of all any protocol port objects (all port objects with a protocol value of All).

    **Tags:** Object

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllAnyProtocolPortObject` (GET (list))
    - `getAnyProtocolPortObject` (GET)

    **Query parameters:**

    - `filter` (string, optional): To be used in conjunction with `"unusedOnly:true"` to search for unused objects and `"nameOrValue:{nameOrValue}"` to search for both name and value.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/object/anyprotocolportobjects/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
