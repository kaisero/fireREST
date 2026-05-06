from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Resource, Connection
from fireREST.fmc.object.protocolportobject.override import Override


class ProtocolPortObject(Resource):
    """Retrieves, deletes, creates, or modifies the protocol(tcp/udp) port object associated with the specified ID. If no ID is specified for a GET, retrieves list of all protocol(tcp/udp) port objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllProtocolPortObject` (GET (list))
    - `getProtocolPortObject` (GET)
    - `createMultipleProtocolPortObject` (CREATE)
    - `updateProtocolPortObject` (UPDATE)
    - `deleteMultipleProtocolPortObject` (DELETE (bulk))
    - `deleteProtocolPortObject` (DELETE)

    **Query parameters:**

    - `overrideTargetId` (string, optional): Retrieves the override(s) associated with the protocol port object on given target ID.
    - `filter` (string, optional): To be used in conjunction with `"unusedOnly:true"` to search for unused objects and `"nameOrValue:{nameOrValue}"` to search for both name and value.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean, optional): Enables bulk create for protocol port objects.
    """
    PATH = '/object/protocolportobjects/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_610

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.override = Override(conn)
