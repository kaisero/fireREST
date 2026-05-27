from fireREST import utils
from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import Resource, Connection
from fireREST.fmc.object.anyconnectcustomattribute.override import Override


class AnyconnectCustomAttribute(Resource):
    """Retrieves the AnyConnect Custom Attribute associated with the specified ID. If no ID is specified for a GET, retrieves list of all AnyConnect Custom Attribute objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllAnyConnectCustomAttributeModel` (GET (list))
    - `getAnyConnectCustomAttributeModel` (GET)
    - `createAnyConnectCustomAttributeModel` (CREATE)
    - `updateAnyConnectCustomAttributeModel` (UPDATE)
    - `deleteAnyConnectCustomAttributeModel` (DELETE)

    **Query parameters:**

    - `filter` (string, optional): To be used in conjunction with `"unusedOnly:true"` to search for unused objects and `"nameOrValue:{nameOrValue}"` to search for both name and value.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/object/anyconnectcustomattributes/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700

    SUPPORTED_FILTERS = ['name_or_value', 'unused_only']
    SUPPORTED_PARAMS = ['override_target_id']

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.override = Override(conn)

    @utils.support_params
    def get(self, uuid=None, name=None, name_or_value=None, unused_only=None, override_target_id=None, params=None):
        return super().get(uuid=uuid, name=name, params=params)
