from fireREST.defaults import API_RELEASE_730
from fireREST.fmc import ChildResource


class LoopbackInterface(ChildResource):
    """Retrieves, deletes, creates, or modifies the loopback interface associated with the specified NGFW device ID and/or interface ID.

    **Tags:** Devices

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllFTDLoopbackInterface` (GET (list))
    - `getFTDLoopbackInterface` (GET)
    - `createFTDLoopbackInterface` (CREATE)
    - `updateFTDLoopbackInterface` (UPDATE)
    - `deleteFTDLoopbackInterface` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/loopbackinterfaces/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_730
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_730
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_730
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_730
