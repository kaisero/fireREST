from fireREST.defaults import API_RELEASE_760
from fireREST.fmc import ChildResource


class DefaultModelMapping(ChildResource):
    """Retrieves the default model mapping for the specified device template.

    **Tags:** Templates

    **Supported operations:** GET

    **Operation IDs:**

    - `getDefaultModelMapping` (GET)
    """

    CONTAINER_NAME = 'DeviceTemplate'
    CONTAINER_PATH = '/templates/devicetemplates/{uuid}'
    PATH = '/templates/devicetemplates/{container_uuid}/defaultmodelmappings/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_UPDATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
