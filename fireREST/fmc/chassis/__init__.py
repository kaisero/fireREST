from fireREST.fmc import Connection, Resource
from fireREST.defaults import API_RELEASE_710
from fireREST.fmc.chassis.appinfo import AppInfo
from fireREST.fmc.chassis.chassisetherchannelinterface import ChassisEtherChannelInterface
from fireREST.fmc.chassis.chassisinterface import ChassisInterface
from fireREST.fmc.chassis.chassisinterfaceevent import ChassisInterfaceEvent
from fireREST.fmc.chassis.chassissnmpsettings import ChassisSnmpSettings
from fireREST.fmc.chassis.chassissubinterface import ChassisSubInterface
from fireREST.fmc.chassis.faultsummary import FaultSummary
from fireREST.fmc.chassis.instancesummary import InstanceSummary
from fireREST.fmc.chassis.interface import Interface
from fireREST.fmc.chassis.interfacesummary import InterfaceSummary
from fireREST.fmc.chassis.inventorysummary import InventorySummary
from fireREST.fmc.chassis.logicaldevice import LogicalDevice
from fireREST.fmc.chassis.networkmodule import NetworkModule
from fireREST.fmc.chassis.operational import Operational
from fireREST.fmc.chassis.physicalinterface import PhysicalInterface


class Chassis(Resource):
    PATH = '/chassis/fmcmanagedchassis/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_710

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.appinfo = AppInfo(conn)
        self.chassisetherchannelinterface = ChassisEtherChannelInterface(conn)
        self.chassisinterface = ChassisInterface(conn)
        self.chassisinterfaceevent = ChassisInterfaceEvent(conn)
        self.chassissnmpsettings = ChassisSnmpSettings(conn)
        self.chassissubinterface = ChassisSubInterface(conn)
        self.faultsummary = FaultSummary(conn)
        self.instancesummary = InstanceSummary(conn)
        self.interface = Interface(conn)
        self.interfacesummary = InterfaceSummary(conn)
        self.inventorysummary = InventorySummary(conn)
        self.logicaldevice = LogicalDevice(conn)
        self.networkmodule = NetworkModule(conn)
        self.operational = Operational(conn)
        self.physicalinterface = PhysicalInterface(conn)
