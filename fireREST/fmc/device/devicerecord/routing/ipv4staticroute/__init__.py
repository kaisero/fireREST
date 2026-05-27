from fireREST.defaults import API_RELEASE_623
from fireREST.fmc import ChildResource


class Ipv4StaticRoute(ChildResource):
    """Retrieves, deletes, creates, or modifies the IPv4 Static Route associated with the specified ID. Also, retrieves list of all IPv4 Static routes. When device is in multi virtual router mode, this API is applicable to Global Virtual Router.

    **Tags:** Devices

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllIPv4StaticRouteModel` (GET (list))
    - `getIPv4StaticRouteModel` (GET)
    - `createMultipleIPv4StaticRouteModel` (CREATE)
    - `updateIPv4StaticRouteModel` (UPDATE)
    - `deleteIPv4StaticRouteModel` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean, optional): Enables bulk create for IPv4 static routes.
    """

    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/routing/ipv4staticroutes/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_623
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_623
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_623
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_623
