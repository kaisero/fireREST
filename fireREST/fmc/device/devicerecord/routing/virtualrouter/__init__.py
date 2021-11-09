from fireREST.defaults import API_RELEASE_660
from fireREST.fmc import ChildResource, Connection
from fireREST.fmc.device.devicerecord.routing.virtualrouter.bgp import Bgp


class VirtualRouter(ChildResource):
    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/routing/virtualrouters/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_660
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_660
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_660
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_660

    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.bgp = Bgp(conn)
