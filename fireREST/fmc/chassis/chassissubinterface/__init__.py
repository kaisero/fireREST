from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import ChildResource


class ChassisSubInterface(ChildResource):
    """Retrieves, deletes, creates, or modifies the Chassis Sub interface configurations.

    **Tags:** Chassis

    **Supported operations:** GET, CREATE, DELETE

    **Operation IDs:**

    - `getAllSubInterface` (GET (list))
    - `createSubInterface` (CREATE)
    - `deleteSubInterface` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'Chassis'
    CONTAINER_PATH = '/chassis/fmcmanagedchassis/{uuid}'
    PATH = '/chassis/fmcmanagedchassis/{container_uuid}/subinterfaces/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_740
