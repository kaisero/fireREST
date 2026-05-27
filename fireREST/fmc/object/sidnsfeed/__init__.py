from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import Resource


class SiDnsFeed(Resource):
    """Retrieves the Security Intelligence DNS feed objects associated with the specified ID. If no ID is specified for a GET, retrieves list of all Security Intelligence DNS feed objects.

    **Tags:** Object

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllSIDNSFeed` (GET (list))
    - `getSIDNSFeed` (GET)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/object/sidnsfeeds/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
