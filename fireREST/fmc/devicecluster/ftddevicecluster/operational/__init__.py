from fireREST import utils
from fireREST.defaults import API_RELEASE_710
from fireREST.fmc import ChildResource


class Operational(ChildResource):
    CONTAINER_NAME = 'FtdDeviceCluster'
    CONTAINER_PATH = '/deviceclusters/ftddevicecluster/{uuid}'
    PATH = '/deviceclusters/ftddevicecluster/{container_uuid}/operational'
    SUPPORTED_FILTERS = ['device_id', 'operation']

    @utils.minimum_version_required(version=API_RELEASE_710)
    @utils.resolve_by_name
    def command(self, container_uuid=None, container_name=None, device_id=None, operation=None, params=None):
        url = self.url(path=f'{self.PATH}/ftdclusterdevicecommands')
        return self.conn.post(url=url, data={}, params=params)
