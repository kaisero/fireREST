from fireREST.defaults import API_RELEASE_730
from fireREST.fmc import ChildResource


class ClusterHealthMonitorSettings(ChildResource):
    CONTAINER_NAME = 'FtdDeviceCluster'
    CONTAINER_PATH = '/deviceclusters/ftddevicecluster/{uuid}'
    PATH = '/deviceclusters/ftddevicecluster/{container_uuid}/clusterhealthmonitorsettings/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_730
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_730
