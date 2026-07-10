from fireREST.defaults import API_RELEASE_740, API_RELEASE_770
from fireREST.fmc import ChildResource


class Ospfv3Route(ChildResource):
    """Retrieves, creates, updates, or deletes OSPFv3 routes for the specified device.

    **Tags:** Devices

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllOspfv3RoutePolicyModel` (GET (list))
    - `getOspfv3RoutePolicyModel` (GET)
    - `createOspfv3RoutePolicyModel` (CREATE)
    - `updateOspfv3RoutePolicyModel` (UPDATE)
    - `deleteOspfv3RoutePolicyModel` (DELETE)
    """

    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/routing/ospfv3routes/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_770
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_770
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_770
