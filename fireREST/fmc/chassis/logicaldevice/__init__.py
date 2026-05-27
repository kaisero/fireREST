from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import ChildResource


class LogicalDevice(ChildResource):
    """Retrieves the list of all logical devices available on the specified chassis.

    **Tags:** Chassis

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllLogicalDevice` (GET (list))
    - `getLogicalDevice` (GET)
    - `createLogicalDevice` (CREATE)
    - `updateLogicalDevice` (UPDATE)
    - `deleteLogicalDevice` (DELETE)

    **Query parameters:**

    - `useCache` (string, optional): Fetch the data from Cache. This is applicable only for UI.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'Chassis'
    CONTAINER_PATH = '/chassis/fmcmanagedchassis/{uuid}'
    PATH = '/chassis/fmcmanagedchassis/{container_uuid}/logicaldevices/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_740
