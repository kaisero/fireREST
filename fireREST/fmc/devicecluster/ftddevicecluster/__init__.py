from typing import Dict

from fireREST import utils
from fireREST.defaults import API_RELEASE_640, API_RELEASE_710
from fireREST.fmc import Connection, Resource
from fireREST.fmc.devicecluster.ftddevicecluster.clusterhealthmonitorsettings import ClusterHealthMonitorSettings
from fireREST.fmc.devicecluster.ftddevicecluster.operational import Operational


class FtdDeviceCluster(Resource):
    """Retrieves or modifies the Firewall Threat Defense Cluster record associated with the specified ID. If no ID is specified for a GET, retrieves list of all Firewall Threat Defense Clusters.

    **Tags:** Device Clusters

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllRestFTDClusterDeviceContainer` (GET (list))
    - `getRestFTDClusterDeviceContainer` (GET)
    - `createRestFTDClusterDeviceContainer` (CREATE)
    - `updateRestFTDClusterDeviceContainer` (UPDATE)
    - `deleteRestFTDClusterDeviceContainer` (DELETE)

    **Query parameters:**

    - `liveStatus` (string, optional): Boolean to specify if live status of cluster nodes is required.
    - `includeMTUValues` (string, optional): Boolean to specify if cluster control link and data interface MTU values are required
    - `filter` (string, optional): Filter to retrieve or delete clusters based upon filter parameters specified. To delete specific nodes we need `"dataDeviceIds:dataDeviceId1,dataDeviceId2,.."`. If no filter is provided, whole cluster will be deleted from management center. For fetching clusters, filter criteria shall be `clusterBootstrapSupported:{true|false};analyticsOnly:{true|false}` `clusterBootstrapSupported` -- Allowed values are `{true|false}` `analyticsOnly` -- Allowed values are `{true|false}`
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/deviceclusters/ftddevicecluster/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_640
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_710
    SUPPORTED_PARAMS = ['skip_control_readiness']

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.clusterhealthmonitorsettings = ClusterHealthMonitorSettings(conn)
        self.operational = Operational(conn)

    @utils.minimum_version_required(version=API_RELEASE_710)
    def readiness_check(self, data: Dict, skip_control_readiness=None, params=None):
        url = self.url(path='/deviceclusters/ftdclusterreadinesscheck')
        return self.conn.post(url=url, data=data, params=params)
