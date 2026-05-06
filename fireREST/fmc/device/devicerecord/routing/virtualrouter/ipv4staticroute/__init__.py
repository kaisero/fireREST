from fireREST.defaults import API_RELEASE_660
from fireREST.fmc import NestedChildResource


class Ipv4StaticRoute(NestedChildResource):
    """Retrieves, deletes, creates, or modifies the IPv4 Static Route associated with the specified virtual router. Also, retrieves list of all IPv4 Static routes.

    **Tags:** Devices

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllVrfIPv4StaticRouteModel` (GET (list))
    - `getVrfIPv4StaticRouteModel` (GET)
    - `createVrfIPv4StaticRouteModel` (CREATE)
    - `updateVrfIPv4StaticRouteModel` (UPDATE)
    - `deleteVrfIPv4StaticRouteModel` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    CHILD_CONTAINER_NAME = 'VirtualRouter'
    CHILD_CONTAINER_PATH = '/devices/devicerecords/{container_uuid}/routing/virtualrouters/{uuid}'
    PATH = (
        '/devices/devicerecords/{container_uuid}/routing/virtualrouters/{child_container_uuid}/ipv4staticroutes/{uuid}'
    )
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_660
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_660
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_660
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_660
