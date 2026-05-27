from fireREST import utils
from fireREST.defaults import API_RELEASE_700, API_RELEASE_720
from fireREST.fmc import Resource, Connection
from fireREST.fmc.object.ipv6addresspool.override import Override


class Ipv6AddressPool(Resource):
    """Retrieves the IPv6 Address Pool object associated with the specified ID. If no ID is specified for a GET, retrieves list of all IPv6 Address Pool objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllIPv6AddressPool` (GET (list))
    - `getIPv6AddressPool` (GET)
    - `createIPv6AddressPool` (CREATE)
    - `updateIPv6AddressPool` (UPDATE)
    - `deleteIPv6AddressPool` (DELETE)

    **Query parameters:**

    - `overrideTargetId` (string, optional): Retrieves the override(s) associated with the IPv6 Address Pool object on given target ID.
    - `filter` (string, optional): To be used in conjunction with `"unusedOnly:true"` to search for unused objects and `"nameOrValue:{nameOrValue}"` to search for both name and value.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/object/ipv6addresspools/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_720

    SUPPORTED_FILTERS = ['name_or_value', 'unused_only']
    SUPPORTED_PARAMS = ['override_target_id']

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.override = Override(conn)

    @utils.support_params
    def get(self, uuid=None, name=None, override_target_id=None, params=None):
        return super().get(uuid=uuid, name=name, params=params)
