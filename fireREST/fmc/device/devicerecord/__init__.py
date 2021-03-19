from fireREST.fmc import Connection, Resource
from fireREST.fmc.device.devicerecord.bridgegroupinterface import BridgeGroupInterface
from fireREST.fmc.device.devicerecord.etherchannelinterface import EtherChannelInterface
from fireREST.fmc.device.devicerecord.fpinterfacestatistics import FpInterfaceStatistics
from fireREST.fmc.device.devicerecord.fplogicalinterface import FpLogicalInterface
from fireREST.fmc.device.devicerecord.fpphysicalinterface import FpPhysicalInterface
from fireREST.fmc.device.devicerecord.inlineset import InlineSet
from fireREST.fmc.device.devicerecord.interfaceevent import InterfaceEvent
from fireREST.fmc.device.devicerecord.operational import Operational
from fireREST.fmc.device.devicerecord.redundantinterface import RedundantInterface
from fireREST.fmc.device.devicerecord.routing import Routing
from fireREST.fmc.device.devicerecord.subinterface import SubInterface
from fireREST.fmc.device.devicerecord.virtualswitch import VirtualSwitch
from fireREST.fmc.device.devicerecord.virtualtunnelinterface import VirtualTunnelInterface
from fireREST.fmc.device.devicerecord.vlaninterface import VlanInterface


class DeviceRecord(Resource):
    PATH = '/devices/devicerecords/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '6.1.0'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '6.1.0'
    MINIMUM_VERSION_REQUIRED_DELETE = '6.1.0'
    SUPPORTED_PARAMS = ['hostname']

    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.bridgegroupinterface = BridgeGroupInterface(conn)
        self.etherchannelinterface = EtherChannelInterface(conn)
        self.fpinterfacestatistics = FpInterfaceStatistics(conn)
        self.fplogicalinterface = FpLogicalInterface(conn)
        self.fpphysicalinterface = FpPhysicalInterface(conn)
        self.inlineset = InlineSet(conn)
        self.interfaceevent = InterfaceEvent(conn)
        self.operational = Operational(conn)
        self.redundantinterface = RedundantInterface(conn)
        self.routing = Routing(conn)
        self.subinterface = SubInterface(conn)
        self.virtualswitch = VirtualSwitch(conn)
        self.virtualtunnelinterface = VirtualTunnelInterface(conn)
        self.vlaninterface = VlanInterface(conn)
