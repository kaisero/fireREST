from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import Resource


class SiDnsList(Resource):
    """Retrieves the Security Intelligence DNS list objects associated with the specified ID. If no ID is specified for a GET, retrieves list of all Security Intelligence DNS list objects.

    **Tags:** Object

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllSIDNSList` (GET (list))
    - `getSIDNSList` (GET)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/object/sidnslists/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
