from fireREST.defaults import API_RELEASE_623
from fireREST.fmc import ChildResource


class StaticRoute(ChildResource):
    """Retrieves list of all Static routes (ipv4 and ipv6) associated with the specified device. When device is in multi virtual router mode, this API is applicable to Global Virtual Router.

    **Tags:** Devices

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllStaticRouteModel` (GET (list))
    - `getStaticRouteModel` (GET)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/routing/staticroutes/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_623
