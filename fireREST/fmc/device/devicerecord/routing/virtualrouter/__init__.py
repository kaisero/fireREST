from fireREST.defaults import API_RELEASE_660
from fireREST.fmc import ChildResource, Connection
from fireREST.fmc.device.devicerecord.routing.virtualrouter.bfdpolicy import BfdPolicy
from fireREST.fmc.device.devicerecord.routing.virtualrouter.bgp import Bgp
from fireREST.fmc.device.devicerecord.routing.virtualrouter.eigrproute import EigrpRoute
from fireREST.fmc.device.devicerecord.routing.virtualrouter.ipv4staticroute import Ipv4StaticRoute
from fireREST.fmc.device.devicerecord.routing.virtualrouter.ipv6staticroute import Ipv6StaticRoute
from fireREST.fmc.device.devicerecord.routing.virtualrouter.ospfinterface import OspfInterface
from fireREST.fmc.device.devicerecord.routing.virtualrouter.ospfv2route import Ospfv2Route
from fireREST.fmc.device.devicerecord.routing.virtualrouter.ospfv3interface import Ospfv3Interface
from fireREST.fmc.device.devicerecord.routing.virtualrouter.ospfv3route import Ospfv3Route
from fireREST.fmc.device.devicerecord.routing.virtualrouter.policybasedroute import PolicyBasedRoute


class VirtualRouter(ChildResource):
    """Retrieves list of all virtual routers created in the specified device.

    **Tags:** Devices

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllVirtualRouterModel` (GET (list))
    - `getVirtualRouterModel` (GET)
    - `createVirtualRouterModel` (CREATE)
    - `updateVirtualRouterModel` (UPDATE)
    - `deleteVirtualRouterModel` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/routing/virtualrouters/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_660
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_660
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_660
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_660

    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.bfdpolicy = BfdPolicy(conn)
        self.bgp = Bgp(conn)
        self.eigrproute = EigrpRoute(conn)
        self.ipv4staticroute = Ipv4StaticRoute(conn)
        self.ipv6staticroute = Ipv6StaticRoute(conn)
        self.ospfinterface = OspfInterface(conn)
        self.ospfv2route = Ospfv2Route(conn)
        self.ospfv3interface = Ospfv3Interface(conn)
        self.ospfv3route = Ospfv3Route(conn)
        self.policybasedroute = PolicyBasedRoute(conn)
