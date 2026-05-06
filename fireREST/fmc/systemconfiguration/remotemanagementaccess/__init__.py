from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class RemoteManagementAccess(Resource):
    """Retrieves remote management access configuration associated with the specified ID.

    **Tags:** System Configuration

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllRemoteManagementAccess` (GET (list))
    - `getRemoteManagementAccess` (GET)
    - `updateRemoteManagementAccess` (UPDATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    NAMESPACE = 'platform'
    PATH = '/systemconfiguration/remotemanagementaccess/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
