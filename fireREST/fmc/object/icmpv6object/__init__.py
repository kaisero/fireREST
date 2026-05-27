from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Resource, Connection
from fireREST.fmc.object.icmpv6object.override import Override


class Icmpv6Object(Resource):
    """Retrieves, deletes, creates, or modifies the icmpv6 object associated with the specified ID. If no ID is specified for a GET, retrieves list of all icmpv6 objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllICMPV6Object` (GET (list))
    - `getICMPV6Object` (GET)
    - `createMultipleICMPV6Object` (CREATE)
    - `updateICMPV6Object` (UPDATE)
    - `deleteMultipleICMPV6Object` (DELETE (bulk))
    - `deleteICMPV6Object` (DELETE)

    **Query parameters:**

    - `overrideTargetId` (string, optional): Retrieves the override(s) associated with the ICMPv6 object on given target ID.
    - `filter` (string, optional): To be used in conjunction with `"unusedOnly:true"` to search for unused objects and `"nameOrValue:{nameOrValue}"` to search for both name and value.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean, optional): Enables bulk create for ICMPv6 objects.
    """

    PATH = '/object/icmpv6objects/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_610

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.override = Override(conn)
