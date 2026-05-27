from fireREST import utils
from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Resource, Connection
from fireREST.fmc.object.networkgroup.override import Override


class NetworkGroup(Resource):
    """Retrieves, deletes, creates, or modifies the network group object associated with the specified ID. If no ID is specified for a GET, retrieves list of all network group objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllNetworkGroup` (GET (list))
    - `getNetworkGroup` (GET)
    - `createMultipleNetworkGroup` (CREATE)
    - `updateNetworkGroup` (UPDATE)
    - `deleteMultipleNetworkGroup` (DELETE (bulk))
    - `deleteNetworkGroup` (DELETE)

    **Query parameters:**

    - `overrideTargetId` (string, optional): Retrieves the override(s) associated with the network group object on given target ID.
    - `action` (string, optional): This parameter specifies that the network objects will be added or removed from the network group. This parameter is a string. When its value is add the PUT operation will add these network objects to the network group, and if the value is remove the PUT operation will remove these network objects from the network group.
    - `filter` (string, optional): To be used in conjunction with `"unusedOnly:true"` to search for unused objects and `"nameOrValue:{nameOrValue}"` to search for both name and value.`"ids:id1,id2,..."`. `ids` is a comma-separated list of rule IDs to be deleted.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean, optional): Enables bulk create for network group objects.
    """

    PATH = '/object/networkgroups/{uuid}'
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
