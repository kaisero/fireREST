from fireREST.defaults import API_RELEASE_760
from fireREST.fmc import ChildResource


class ModelMapping(ChildResource):
    """Retrieves, creates, updates, or deletes model mappings for the specified device template.

    **Tags:** Templates

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllModelMapping` (GET (list))
    - `getModelMapping` (GET)
    - `createModelMapping` (CREATE)
    - `updateModelMapping` (UPDATE)
    - `deleteModelMapping` (DELETE)
    """

    CONTAINER_NAME = 'DeviceTemplate'
    CONTAINER_PATH = '/templates/devicetemplates/{uuid}'
    PATH = '/templates/devicetemplates/{container_uuid}/modelmappings/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_760
