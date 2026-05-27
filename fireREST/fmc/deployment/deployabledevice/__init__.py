from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Connection, Resource
from fireREST.fmc.deployment.deployabledevice.deployment import Deployment
from fireREST.fmc.deployment.deployabledevice.pendingchanges import PendingChanges


class DeployableDevice(Resource):
    """Retrieves list of all devices with configuration changes, ready to be deployed.

    **Tags:** Deployment

    **Supported operations:** GET

    **Operation IDs:**

    - `getDeployableDevice` (GET (list))

    **Query parameters:**

    - `groupDependency` (boolean, optional): Group Dependency of the dirty policies. Allowed values are `true` or `false`. Group dependency value helps to add dependent policies in Selective Policy Deployment. Results will be shown only when expanded is set to true. It may affect the performance of the API.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/deployment/deployabledevices/{uuid}'
    SUPPORTED_PARAMS = ['group_dependency']
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610

    def __init__(self, conn: Connection):
        self.deployment = Deployment(conn)
        self.pendingchanges = PendingChanges(conn)
        super().__init__(conn)
