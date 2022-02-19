from fireREST import utils
from fireREST.defaults import API_RELEASE_640
from fireREST.fmc import ChildResource


class InterfaceEvent(ChildResource):
    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/interfaceevents'

    @utils.minimum_version_required(version=API_RELEASE_640)
    @utils.resolve_by_name
    def get(self, container_uuid=None, container_name=None):
        url = self.url(self.PATH.format(container_uuid=container_uuid))
        return self.conn.get(url=url)

    @utils.minimum_version_required(version=API_RELEASE_640)
    @utils.resolve_by_name
    def accept(self, container_uuid=None, container_name=None):
        url = self.url(path=self.PATH.format(container_uuid=container_uuid))
        data = {'action': 'ACCEPT_CHANGES'}
        return self.conn.post(url=url, data=data)

    @utils.resolve_by_name
    @utils.minimum_version_required(version=API_RELEASE_640)
    def sync(self, container_uuid=None, container_name=None):
        url = self.url(path=self.PATH.format(container_uuid=container_uuid))
        data = {'action': 'SYNC_WITH_DEVICE'}
        return self.conn.post(url=url, data=data)
