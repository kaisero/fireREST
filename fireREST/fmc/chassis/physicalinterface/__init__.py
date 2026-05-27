from fireREST.defaults import API_RELEASE_730
from fireREST.fmc import ChildResource


class PhysicalInterface(ChildResource):
    """Retrieves or modifies the chassis Physical interface configurations.

    **Tags:** Chassis

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllPhysicalInterface` (GET (list))
    - `getPhysicalInterface` (GET)
    - `updatePhysicalInterface` (UPDATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'Chassis'
    CONTAINER_PATH = '/chassis/fmcmanagedchassis/{uuid}'
    PATH = '/chassis/fmcmanagedchassis/{container_uuid}/physicalinterfaces/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_730
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_730
