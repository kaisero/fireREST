from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import Resource


class SecurexConfig(Resource):
    """Retrieves, creates, or modifies the SecureX configuration associated with the specified ID. If no ID is specified for a GET, retrieves list of all SecureX configurations.

    **Tags:** Integration

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllSecurexConfig` (GET (list))
    - `getSecurexConfig` (GET)
    - `updateSecurexConfig` (UPDATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/integration/securexconfigs/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_700
