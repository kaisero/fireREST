from fireREST.defaults import API_RELEASE_760
from fireREST.fmc import ChildResource


class ObjectOverride(ChildResource):
    """Retrieves or updates object overrides for the specified device template.

    **Tags:** Templates

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getObjectOverride` (GET)
    - `updateObjectOverride` (UPDATE)
    """

    CONTAINER_NAME = 'DeviceTemplate'
    CONTAINER_PATH = '/templates/devicetemplates/{uuid}'
    PATH = '/templates/devicetemplates/{container_uuid}/objectoverrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
