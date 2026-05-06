from fireREST import utils
from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import ChildResource


class VirtualSwitch(ChildResource):
    """Retrieves, deletes, creates, or modifies the virtual switch associated with the specified NGIPS device ID and virtual switch ID. If no virtual switch ID is specified, retrieves list of all virtual switches associated with the specified NGIPS device ID.

    **Tags:** Devices

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllVirtualSwitch` (GET (list))
    - `getVirtualSwitch` (GET)
    - `createVirtualSwitch` (CREATE)
    - `updateVirtualSwitch` (UPDATE)
    - `deleteVirtualSwitch` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/virtualswitches/{uuid}'
    SUPPORTED_PARAMS = ['name']
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_610

    @utils.support_params
    def get(self, container_uuid=None, container_name=None, uuid=None, name=None, params=None):
        return super().get(
            container_uuid=container_uuid, container_name=container_name, uuid=uuid, name=name, params=params
        )
