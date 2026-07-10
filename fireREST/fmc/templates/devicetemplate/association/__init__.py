from fireREST.defaults import API_RELEASE_760
from fireREST.fmc import ChildResource


class DeviceTemplateAssociation(ChildResource):
    """Retrieves or deletes associations for the specified device template.

    **Tags:** Templates

    **Supported operations:** GET, DELETE

    **Operation IDs:**

    - `getAllDeviceTemplateAssociation` (GET (list))
    - `deleteDeviceTemplateAssociation` (DELETE)
    """

    CONTAINER_NAME = 'DeviceTemplate'
    CONTAINER_PATH = '/templates/devicetemplates/{uuid}'
    PATH = '/templates/devicetemplates/{container_uuid}/associations/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_UPDATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_760
