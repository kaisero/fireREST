from fireREST import utils
from fireREST.defaults import API_RELEASE_630
from fireREST.fmc import Resource, Connection
from fireREST.fmc.object.dnsservergroup.override import Override


class DnsServerGroup(Resource):
    """Retrieves, deletes, creates, or modifies the DNS Server Group object associated with the specified ID. If no ID is specified for a GET, retrieves list of all DNS Server Group objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllDNSServerGroupObject` (GET (list))
    - `getDNSServerGroupObject` (GET)
    - `createDNSServerGroupObject` (CREATE)
    - `updateDNSServerGroupObject` (UPDATE)
    - `deleteDNSServerGroupObject` (DELETE)

    **Query parameters:**

    - `overrideTargetId` (string, optional): Retrieves the override(s) associated with the object on given target ID.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/object/dnsservergroups/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_630

    SUPPORTED_PARAMS = ['override_target_id']

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.override = Override(conn)

    @utils.support_params
    def get(self, uuid=None, name=None, override_target_id=None, params=None):
        return super().get(uuid=uuid, name=name, params=params)
