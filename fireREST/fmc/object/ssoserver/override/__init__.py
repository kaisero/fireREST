from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import ChildResource


class Override(ChildResource):
    """Retrieves all(Domain and Device) overrides on a SSO Server Policy Object. Response will always be in expanded form. If passed, the "expanded" query parameter will be ignored.

    **Tags:** Object

    **Supported operations:** GET

    **Operation IDs:**

    - `getSSOServerOverride` (GET (list))

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    CONTAINER_NAME = 'SsoServer'
    CONTAINER_PATH = '/object/ssoservers/{uuid}'
    PATH = '/object/ssoservers/{container_uuid}/overrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
