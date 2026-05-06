from fireREST import utils
from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import ChildResource


class PhysicalInterface(ChildResource):
    """Retrieves the physical interface associated with the specified NGFW device ID and interface ID. If no interface ID is specified, retrieves list of all physical interfaces associated with the specified NGFW device ID. <div class="alert alert-warning">More details on netmod events(out of sync interfaces):<b> GET /interfaceevents</b></div>

    **Tags:** Devices

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllFTDPhysicalInterface` (GET (list))
    - `getFTDPhysicalInterface` (GET)
    - `updateFTDPhysicalInterface` (UPDATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/physicalinterfaces/{uuid}'
    SUPPORTED_PARAMS = ['name']
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_610

    @utils.support_params
    def get(self, container_uuid=None, container_name=None, uuid=None, name=None, params=None):
        return super().get(
            container_uuid=container_uuid, container_name=container_name, uuid=uuid, name=name, params=params
        )
