from fireREST.defaults import API_RELEASE_710
from fireREST.fmc import ChildResource


class NetworkModule(ChildResource):
    """Retrieves list of all network modules available on the specified device.

    **Tags:** Chassis

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllNetworkModule` (GET (list))
    - `getNetworkModule` (GET)
    - `updateNetworkModule` (UPDATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'Chassis'
    CONTAINER_PATH = '/chassis/fmcmanagedchassis/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_710
    PATH = '/chassis/fmcmanagedchassis/{container_uuid}/networkmodules/{uuid}'
