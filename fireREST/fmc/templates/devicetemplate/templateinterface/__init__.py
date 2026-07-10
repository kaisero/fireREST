from fireREST.defaults import API_RELEASE_760
from fireREST.fmc import ChildResource


class TemplateInterface(ChildResource):
    """Retrieves, creates, or deletes template interfaces for the specified device template.

    **Tags:** Templates

    **Supported operations:** GET, CREATE, DELETE

    **Operation IDs:**

    - `getAllTemplateInterface` (GET (list))
    - `getTemplateInterface` (GET)
    - `createTemplateInterface` (CREATE)
    - `deleteTemplateInterface` (DELETE)
    """

    CONTAINER_NAME = 'DeviceTemplate'
    CONTAINER_PATH = '/templates/devicetemplates/{uuid}'
    PATH = '/templates/devicetemplates/{container_uuid}/templateinterfaces/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_UPDATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_760
