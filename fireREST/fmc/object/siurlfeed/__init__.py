from fireREST.defaults import API_RELEASE_623
from fireREST.fmc import Resource


class SiUrlFeed(Resource):
    """Retrieves, creates, deletes or modifies the Security Intelligence URL Feed object associated with the specified ID. If no ID is specified, retrieves list of all Security Intelligence URL Feed objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllSIURLFeed` (GET (list))
    - `getSIURLFeed` (GET)
    - `createSIURLFeed` (CREATE)
    - `updateSIURLFeed` (UPDATE)
    - `deleteSIURLFeed` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/object/siurlfeeds/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_623
