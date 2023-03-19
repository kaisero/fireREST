from fireREST.defaults import API_RELEASE_660
from fireREST.fmc import ChildResource, Connection
from fireREST.fmc.device.devicerecord.routing.virtualrouter.bgp import Bgp
from fireREST.fmc.device.devicerecord.routing.virtualrouter.ipv4staticroute import Ipv4StaticRoute
from fireREST.fmc.device.devicerecord.routing.virtualrouter.ipv6staticroute import Ipv6StaticRoute
from fireREST.fmc.device.devicerecord.routing.virtualrouter.ospfinterface import OspfInterface
from fireREST.fmc.device.devicerecord.routing.virtualrouter.ospfv2route import Ospfv2Route
from fireREST.fmc.device.devicerecord.routing.virtualrouter.policybasedroute import PolicyBasedRoute


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
        self.ipv4staticroute = Ipv4StaticRoute(conn)
        self.ipv6staticroute = Ipv6StaticRoute(conn)
        self.ospfinterface = OspfInterface(conn)
        self.ospfv2route = Ospfv2Route(conn)
        self.policybasedroute = PolicyBasedRoute(conn)
