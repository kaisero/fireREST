from fireREST import utils
from fireREST.defaults import API_RELEASE_700, API_RELEASE_720
from fireREST.fmc import Resource, Connection
from fireREST.fmc.object.ssoserver.override import Override


class SsoServer(Resource):
    """Retrieves the SSO Server Policy Object associated with the specified ID. If no ID is specified, retrieves list of all SSO Server Policy Objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllSSOServer` (GET (list))
    - `getSSOServer` (GET)
    - `createMultipleSSOServer` (CREATE)
    - `updateSSOServer` (UPDATE)
    - `deleteSSOServer` (DELETE)

    **Query parameters:**

    - `overrideTargetId` (string, optional): Retrieves the override(s) associated with the host object on given target ID.
    - `filter` (string, optional): To be used in conjunction with `"unusedOnly:true"` to search for unused objects and `"nameOrValue:{nameOrValue}"` to search for both name and value.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean, optional): Enables bulk create for SSO Server Policy Objects.
    """
    PATH = '/object/ssoservers/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_720

    SUPPORTED_PARAMS = ['override_target_id']

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.override = Override(conn)

    @utils.support_params
    def get(self, uuid=None, name=None, override_target_id=None, params=None):
        return super().get(uuid=uuid, name=name, params=params)
