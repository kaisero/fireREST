from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import ChildResource


class FpInterfaceStatistics(ChildResource):
    """Retrieves list of statistics for all interfaces associated with the specified NGIPS device ID.

    **Tags:** Devices

    **Supported operations:** GET

    **Operation IDs:**

    - `getFPInterfaceStatistics` (GET (list))

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/fpinterfacestatistics/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
