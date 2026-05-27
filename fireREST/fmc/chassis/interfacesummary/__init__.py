from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import ChildResource


class InterfaceSummary(ChildResource):
    """Retrieves Interface summary data from the chassis

    **Tags:** Chassis

    **Supported operations:** GET

    **Operation IDs:**

    - `getChassisInterfaceSummary` (GET (list))

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'Chassis'
    CONTAINER_PATH = '/chassis/fmcmanagedchassis/{uuid}'
    PATH = '/chassis/fmcmanagedchassis/{container_uuid}/interfacesummary/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
