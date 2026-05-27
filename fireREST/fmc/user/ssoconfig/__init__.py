from fireREST.defaults import API_RELEASE_670
from fireREST.fmc import Resource


class SsoConfig(Resource):
    """Retrieves, creates, or modifies the SSO configuration associated with the specified ID. If no ID is specified for a GET, retrieves list of all SSO configurations.

    **Tags:** Users

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllSSOConfig` (GET (list))
    - `getSSOConfig` (GET)
    - `updateSSOConfig` (UPDATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/users/ssoconfigs/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_670
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_670
