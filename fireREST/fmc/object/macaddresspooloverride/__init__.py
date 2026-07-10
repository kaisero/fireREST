from fireREST.defaults import API_RELEASE_760
from fireREST.fmc import ChildResource


class MacAddressPoolOverride(ChildResource):
    """Retrieves overrides for the specified MAC address pool object.

    **Tags:** Object

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllMacAddressPoolOverride` (GET (list))
    """

    CONTAINER_NAME = 'MacAddressPool'
    CONTAINER_PATH = '/object/macaddresspools/{uuid}'
    PATH = '/object/macaddresspools/{container_uuid}/overrides'
    MINIMUM_VERSION_REQUIRED_CREATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_UPDATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
