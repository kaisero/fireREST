from fireREST.defaults import API_RELEASE_710
from fireREST.fmc import Resource


class DuoConfig(Resource):
    """Retrieves, creates, or modifies the Duo configuration associated with the specified ID. If no ID is specified for a GET, retrieves list of all Duo configurations.

    **Tags:** Users

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllDuoConfig` (GET (list))
    - `getDuoConfig` (GET)
    - `updateDuoConfig` (UPDATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/users/duoconfigs/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_710
