from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import ChildResource


class FpPhysicalInterface(ChildResource):
    """Retrieves, deletes, creates, or modifies the physical interface associated with the specified NGIPS device ID and interface ID. If no ID is specified, retrieves list of all physical interfaces associated with the specified NGIPS device ID.

    **Tags:** Devices

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllFPPhysicalInterface` (GET (list))
    - `getFPPhysicalInterface` (GET)
    - `updateFPPhysicalInterface` (UPDATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/fpphysicalinterfaces/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_610
