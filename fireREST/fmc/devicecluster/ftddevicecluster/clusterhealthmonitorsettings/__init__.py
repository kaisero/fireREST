from fireREST.defaults import API_RELEASE_730
from fireREST.fmc import ChildResource


class ClusterHealthMonitorSettings(ChildResource):
    """Represents health check monitor settings of Firewall Threat Defense Cluster.

    **Tags:** Device Clusters

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getClusterHealthMonitorSettingsModel` (GET)
    - `updateClusterHealthMonitorSettingsModel` (UPDATE)

    **Query parameters:**

    - `partialUpdate` (boolean, optional): This is a query parameter. Default value is `false`. This field specifies whether to change the entire object or only certain attributes of it. When its value is `false` the whole object will change, and if the value is `true` then only the attributes that are specified will change.
    """

    CONTAINER_NAME = 'FtdDeviceCluster'
    CONTAINER_PATH = '/deviceclusters/ftddevicecluster/{uuid}'
    PATH = '/deviceclusters/ftddevicecluster/{container_uuid}/clusterhealthmonitorsettings/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_730
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_730
