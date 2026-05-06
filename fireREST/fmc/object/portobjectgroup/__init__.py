from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Resource, Connection
from fireREST.fmc.object.portobjectgroup.override import Override


class PortObjectGroup(Resource):
    """Retrieves, deletes, creates, or modifies the port object group object associated with the specified ID. If no ID is specified for a GET, retrieves list of all port object group objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllPortObjectGroup` (GET (list))
    - `getPortObjectGroup` (GET)
    - `createMultiplePortObjectGroup` (CREATE)
    - `updatePortObjectGroup` (UPDATE)
    - `deleteMultiplePortObjectGroup` (DELETE (bulk))
    - `deletePortObjectGroup` (DELETE)

    **Query parameters:**

    - `overrideTargetId` (string, optional): Retrieves the override(s) associated with the port group object on given target ID.
    - `showProtocolNames` (boolean, optional): Indicates whether the protocol will be shown in the metadata. This should be used in conjunction with `"expanded:true"`.
    - `filter` (string, optional): To be used in conjunction with `"unusedOnly:true"` to search for unused objects and `"nameOrValue:{nameOrValue}"` to search for both name and value.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean, optional): Enables bulk create for port group objects.
    """
    PATH = '/object/portobjectgroups/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_610

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.override = Override(conn)
