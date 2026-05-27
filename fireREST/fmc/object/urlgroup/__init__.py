from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Resource, Connection
from fireREST.fmc.object.urlgroup.override import Override


class UrlGroup(Resource):
    """Retrieves, deletes, creates, or modifies the url group objects associated with the specified ID. If no ID is specified for a GET, retrieves list of all url group objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllURLGroupObject` (GET (list))
    - `getURLGroupObject` (GET)
    - `createMultipleURLGroupObject` (CREATE)
    - `updateURLGroupObject` (UPDATE)
    - `deleteMultipleURLGroupObject` (DELETE (bulk))
    - `deleteURLGroupObject` (DELETE)

    **Query parameters:**

    - `overrideTargetId` (string, optional): Retrieves the override(s) associated with the url group object on given target ID.
    - `filter` (string, optional): To be used in conjunction with `"unusedOnly:true"` to search for unused objects and `"nameOrValue:{nameOrValue}"` to search for both name and value. `"ids:id1,id2,..."`.`ids` is a comma-separated list of rule IDs to be deleted.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean, optional): Enables bulk create for url group objects.
    """

    PATH = '/object/urlgroups/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_610

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.override = Override(conn)
