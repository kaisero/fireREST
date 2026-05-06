from fireREST.defaults import API_RELEASE_630
from fireREST.fmc import Resource, Connection
from fireREST.fmc.object.fqdn.override import Override


class Fqdn(Resource):
    """Retrieves, deletes, creates, or modifies the FQDN object associated with the specified ID. If no ID is specified for a GET, retrieves list of all FQDN objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllFQDNObject` (GET (list))
    - `getFQDNObject` (GET)
    - `createMultipleFQDNObject` (CREATE)
    - `updateFQDNObject` (UPDATE)
    - `deleteMultipleFQDNObject` (DELETE (bulk))
    - `deleteFQDNObject` (DELETE)

    **Query parameters:**

    - `overrideTargetId` (string, optional): Retrieves the override(s) associated with the FQDN object on given target ID.
    - `filter` (string, optional): To be used in conjunction with `"unusedOnly:true"` to search for unused objects and `"nameOrValue:{nameOrValue}"` to search for both name and value. `"ids:id1,id2,..."`.`ids` is a comma-separated list of rule IDs to be deleted.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean, optional): Enables bulk create for FQDN objects.
    """
    PATH = '/object/fqdns/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_630

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.override = Override(conn)
