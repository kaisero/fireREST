from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import ChildResource


class ChassisEtherChannelInterface(ChildResource):
    """Retrieves, deletes, creates, or modifies the Chassis EtherChannel interface configurations.

    **Tags:** Chassis

    **Supported operations:** GET, CREATE, DELETE

    **Operation IDs:**

    - `getAllEtherChannelInterface` (GET (list))
    - `createEtherChannelInterface` (CREATE)
    - `deleteEtherChannelInterface` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'Chassis'
    CONTAINER_PATH = '/chassis/fmcmanagedchassis/{uuid}'
    PATH = '/chassis/fmcmanagedchassis/{container_uuid}/etherchannelinterfaces/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_740
