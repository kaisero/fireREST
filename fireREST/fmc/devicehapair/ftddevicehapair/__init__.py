from fireREST.defaults import API_RELEASE_623
from fireREST.fmc import Connection, Resource
from fireREST.fmc.devicehapair.ftddevicehapair.failoverinterfacemacaddressconfig import (
    FailoverInterfaceMacAddressConfig,
)
from fireREST.fmc.devicehapair.ftddevicehapair.monitoredinterface import MonitoredInterface


class FtdHAPair(Resource):
    """Retrieves or modifies the Firewall Threat Defense HA record associated with the specified ID. Creates or breaks or deletes a Firewall Threat Defense HA pair. If no ID is specified for a GET, retrieves list of all Firewall Threat Defense HA pairs.

    **Tags:** Device HA Pairs

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllFTDHADeviceContainer` (GET (list))
    - `getFTDHADeviceContainer` (GET)
    - `createFTDHADeviceContainer` (CREATE)
    - `updateFTDHADeviceContainer` (UPDATE)
    - `deleteFTDHADeviceContainer` (DELETE)

    **Query parameters:**

    - `filter` (string, optional): Filter for analytics only HA `analyticsOnly` -- Allowed values are `{true|false}`
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/devicehapairs/ftddevicehapairs/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_623
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_623
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_623
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_623
    SUPPORTED_PARAMS = ['name']

    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.failoverinterfacemacaddressconfig = FailoverInterfaceMacAddressConfig(conn)
        self.monitoredinterface = MonitoredInterface(conn)
