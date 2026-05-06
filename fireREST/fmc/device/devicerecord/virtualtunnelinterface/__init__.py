from fireREST import utils
from fireREST.defaults import API_RELEASE_670
from fireREST.fmc import ChildResource


class VirtualTunnelInterface(ChildResource):
    """Retrieves, deletes, creates, or modifies the vti interface associated with the specified NGFW device ID and/or interface ID.

    **Tags:** Devices

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllFTDVTIInterface` (GET (list))
    - `getFTDVTIInterface` (GET)
    - `createMultipleFTDVTIInterface` (CREATE)
    - `updateFTDVTIInterface` (UPDATE)
    - `deleteFTDVTIInterface` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean, optional): Enables bulk create for NGFW vti interfaces.
    """
    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/virtualtunnelinterfaces/{uuid}'
    SUPPORTED_PARAMS = ['name']
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_670
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_670
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_670
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_670

    @utils.support_params
    def get(self, container_uuid=None, container_name=None, uuid=None, name=None, params=None):
        return super().get(
            container_uuid=container_uuid, container_name=container_name, uuid=uuid, name=name, params=params
        )
