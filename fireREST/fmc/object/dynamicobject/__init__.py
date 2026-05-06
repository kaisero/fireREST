from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import Resource, Connection
from fireREST.fmc.object.dynamicobject.mapping import Mapping


class DynamicObject(Resource):
    """Retrieves, deletes, creates, or modifies the Dynamic Object associated with the specified ID. If no ID is specified for a GET, retrieves list of all Dynamic Objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllDynamicObject` (GET (list))
    - `getDynamicObject` (GET)
    - `createMultipleDynamicObject` (CREATE)
    - `updateDynamicObject` (UPDATE)
    - `deleteMultipleDynamicObject` (DELETE (bulk))
    - `deleteDynamicObject` (DELETE)

    **Query parameters:**

    - `includeCount` (boolean, optional): If parameter is specified, mappingsCount field will be added into metadata. Can be used if object ID is specified in path.
    - `name` (string, optional): If parameter is specified, only the Dynamic Objects matching with the specified name will be displayed. Cannot be used if object ID is specified in path.
    - `filter` (string, optional): Specify filter criteria<ul><li>Object with ids: `"ids:id1,id2,..."`</li><li>Unused objects: `"unusedOnly:true"`</li><li>Name starts with: `"nameStartsWith:{name-pattern}"`</li></ul>
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean, optional): Enables bulk create (POST) or delete (DELETE) of Dynamic Objects.
    """
    PATH = '/object/dynamicobjects/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_700

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.mapping = Mapping(conn)
