from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import ChildResource


class VniInterface(ChildResource):
    """Get the VNII interface associated with the specified NGFW device and interface ID.

    **Tags:** Devices

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllFTDVNIInterface` (GET (list))
    - `getFTDVNIInterface` (GET)
    - `createFTDVNIInterface` (CREATE)
    - `updateFTDVNIInterface` (UPDATE)
    - `deleteFTDVNIInterface` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/vniinterfaces/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_740
