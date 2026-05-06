from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Connection, Resource
from fireREST.fmc.device.devicerecord.bridgegroupinterface import BridgeGroupInterface
from fireREST.fmc.device.devicerecord.dhcp import Dhcp
from fireREST.fmc.device.devicerecord.etherchannelinterface import EtherChannelInterface
from fireREST.fmc.device.devicerecord.fpinterfacestatistics import FpInterfaceStatistics
from fireREST.fmc.device.devicerecord.fplogicalinterface import FpLogicalInterface
from fireREST.fmc.device.devicerecord.fpphysicalinterface import FpPhysicalInterface
from fireREST.fmc.device.devicerecord.inlineset import InlineSet
from fireREST.fmc.device.devicerecord.interfaceevent import InterfaceEvent
from fireREST.fmc.device.devicerecord.loopbackinterface import LoopbackInterface
from fireREST.fmc.device.devicerecord.managementconvergencemode import ManagementConvergenceMode
from fireREST.fmc.device.devicerecord.operational import Operational
from fireREST.fmc.device.devicerecord.physicalinterface import PhysicalInterface
from fireREST.fmc.device.devicerecord.redundantinterface import RedundantInterface
from fireREST.fmc.device.devicerecord.routing import Routing
from fireREST.fmc.device.devicerecord.subinterface import SubInterface
from fireREST.fmc.device.devicerecord.virtualswitch import VirtualSwitch
from fireREST.fmc.device.devicerecord.virtualtunnelinterface import VirtualTunnelInterface
from fireREST.fmc.device.devicerecord.vlaninterface import VlanInterface


class DeviceRecord(Resource):
    """Retrieves or modifies the device record associated with the specified ID. Registers or unregisters a device. If no ID is specified for a GET, retrieves list of all device records.

    **Tags:** Devices

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllDevice` (GET (list))
    - `getDevice` (GET)
    - `createMultipleDevice` (CREATE)
    - `updateDevice` (UPDATE)
    - `deleteMultipleDevice` (DELETE (bulk))
    - `deleteDevice` (DELETE)

    **Query parameters:**

    - `filter` (string, optional): Filter to retrieve or delete device records based upon filter parameters specified. For bulk deletion, we need the filter="ids:" with `bulk=true` flag, Value is of format : `"ids:id1,id2,..."`. `ids:id1,id2,...` is a comma-separated list of device uuids to be deleted. For fetching device records, Filter criteria should be `name:{name};hostName:{hostName};serialNumber:{ABCXXXXX};containerType:{value};version:{x.x.x};clusterBootstrapSupported:{true|false};analyticsOnly:{true|false};includeOtherAssociatedPolicies:{true|false};modelType:{NGFW|Chassis}` `containerType` -- Allowed values are `{DeviceCluster|DeviceHAPair|DeviceStack}` `clusterBootstrapSupported` -- Allowed values are `{true|false}` `analyticsOnly` -- Allowed values are `{true|false}` `modelType` -- Allowed values are `{NGFW|Chassis}`. When set to `NGFW`, will fetch all NGFW devices, when set to `Chassis`, will fetch all Chassis devices. If filter is not specified, it fetches all the devices</br></br>`includeOtherAssociatedPolicies` -- Allowed values are `{true|false}`. When set to `true`, will give following policies if assigned to device: [`RAVpn`,`FTDS2SVpn`,`PlatformSettingsPolicy`,`QosPolicy`,`NatPolicy`,`FlexConfigPolicy`]
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean, optional): Enables bulk registration or unregistration for devices.
    """
    PATH = '/devices/devicerecords/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_610
    SUPPORTED_PARAMS = ['hostname']

    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.bridgegroupinterface = BridgeGroupInterface(conn)
        self.dhcp = Dhcp(conn)
        self.etherchannelinterface = EtherChannelInterface(conn)
        self.fpinterfacestatistics = FpInterfaceStatistics(conn)
        self.fplogicalinterface = FpLogicalInterface(conn)
        self.fpphysicalinterface = FpPhysicalInterface(conn)
        self.inlineset = InlineSet(conn)
        self.interfaceevent = InterfaceEvent(conn)
        self.loopbackinterface = LoopbackInterface(conn)
        self.managementconvergencemode = ManagementConvergenceMode(conn)
        self.operational = Operational(conn)
        self.physicalinterface = PhysicalInterface(conn)
        self.redundantinterface = RedundantInterface(conn)
        self.routing = Routing(conn)
        self.subinterface = SubInterface(conn)
        self.virtualswitch = VirtualSwitch(conn)
        self.virtualtunnelinterface = VirtualTunnelInterface(conn)
        self.vlaninterface = VlanInterface(conn)
