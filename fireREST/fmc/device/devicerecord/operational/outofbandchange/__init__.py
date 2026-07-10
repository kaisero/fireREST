from fireREST.defaults import API_RELEASE_770
from fireREST.fmc import ChildResource


class OutOfBandChange(ChildResource):
    """Get out of band changes on the device.

    **Tags:** Devices

    **Supported operations:** GET, CREATE

    **Operation IDs:**

    - `getOutOfBandChanges` (GET (list))
    - `createOutOfBandChanges` (CREATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/operational/outofbandchanges'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_770
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_770
    MINIMUM_VERSION_REQUIRED_UPDATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
