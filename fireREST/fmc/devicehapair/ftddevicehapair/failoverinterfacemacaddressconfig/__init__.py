from fireREST.defaults import API_RELEASE_630
from fireREST.fmc import ChildResource


class FailoverInterfaceMacAddressConfig(ChildResource):
    """Retrieves or modifies the Firewall Threat Defense HA failover policy interface MAC addresses record associated with the specified Firewall Threat Defense HA pair. If no ID is specified for a GET, retrieves list of all Firewall Threat Defense HA failover policy interface MAC addresses records.

    **Tags:** Device HA Pairs

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllFTDHAInterfaceMACAddresses` (GET (list))
    - `getFTDHAInterfaceMACAddresses` (GET)
    - `createFTDHAInterfaceMACAddresses` (CREATE)
    - `updateFTDHAInterfaceMACAddresses` (UPDATE)
    - `deleteFTDHAInterfaceMACAddresses` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'FtdDeviceHAPair'
    CONTAINER_PATH = '/devicehapairs/ftddevicehapairs/{uuid}'
    PATH = '/devicehapairs/ftddevicehapairs/{container_uuid}/failoverinterfacemacaddressconfigs/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_630
