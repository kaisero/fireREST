from fireREST.defaults import API_RELEASE_630
from fireREST.fmc import ChildResource


class MonitoredInterface(ChildResource):
    """Retrieves or modifies the Firewall Threat Defense HA Monitored interface policy record associated with the specified Firewall Threat Defense HA pair. If no ID is specified for a GET, retrieves list of all Firewall Threat Defense HA monitored interface policy records.

    **Tags:** Device HA Pairs

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllFTDHAMonitoredInterfaces` (GET (list))
    - `getFTDHAMonitoredInterfaces` (GET)
    - `updateFTDHAMonitoredInterfaces` (UPDATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    CONTAINER_NAME = 'FtdDeviceHAPair'
    CONTAINER_PATH = '/devicehapairs/ftddevicehapairs/{uuid}'
    PATH = '/devicehapairs/ftddevicehapairs/{container_uuid}/monitoredinterfaces/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_630
