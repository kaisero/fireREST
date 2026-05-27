from fireREST.defaults import API_RELEASE_623
from fireREST.fmc import ChildResource


class Ipv6StaticRoute(ChildResource):
    """Retrieves, deletes, creates, or modifies the IPv6 Static Route associated with the specified ID. Also, retrieves list of all IPv6 Static routes. When device is in multi virtual router mode, this API is applicable to Global Virtual Router.

    **Tags:** Devices

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllIPv6StaticRouteModel` (GET (list))
    - `getIPv6StaticRouteModel` (GET)
    - `createMultipleIPv6StaticRouteModel` (CREATE)
    - `updateIPv6StaticRouteModel` (UPDATE)
    - `deleteIPv6StaticRouteModel` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean, optional): Enables bulk create for IPv6 static routes.
    """

    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/routing/ipv6staticroutes/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_623
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_623
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_623
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_623
