from fireREST import utils
from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Resource, Connection
from fireREST.fmc.object.host.override import Override


class Host(Resource):
    """Retrieves, deletes, creates, or modifies the host object associated with the specified ID. If no ID is specified for a GET, retrieves list of all host objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllHostObject` (GET (list))
    - `getHostObject` (GET)
    - `createMultipleHostObject` (CREATE)
    - `updateHostObject` (UPDATE)
    - `deleteMultipleHostObject` (DELETE (bulk))
    - `deleteHostObject` (DELETE)

    **Query parameters:**

    - `overrideTargetId` (string, optional): Retrieves the override(s) associated with the host object on given target ID.
    - `filter` (string, optional): To be used in conjunction with `"unusedOnly:true"` to search for unused objects and `"nameOrValue:{nameOrValue}"` to search for both name and value. `"ids:id1,id2,..."`.`ids` is a comma-separated list of rule IDs to be deleted.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean, optional): Enables bulk create for host objects.
    """
    PATH = '/object/hosts/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_610

    SUPPORTED_FILTERS = ['name_or_value', 'unused_only']
    SUPPORTED_PARAMS = ['override_target_id']

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.override = Override(conn)

    @utils.support_params
    def get(self, uuid=None, name=None, name_or_value=None, unused_only=None, override_target_id=None, params=None):
        return super().get(uuid=uuid, name=name, params=params)
