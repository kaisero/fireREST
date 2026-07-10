from fireREST.defaults import API_RELEASE_770
from fireREST.fmc import ChildResource


class ServiceAccessObjectOverride(ChildResource):
    """Retrieves overrides for the specified service access object.

    **Tags:** Object

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllServiceAccessObjectOverride` (GET (list))
    """

    CONTAINER_NAME = 'ServiceAccessObject'
    CONTAINER_PATH = '/object/serviceaccessobjects/{uuid}'
    PATH = '/object/serviceaccessobjects/{container_uuid}/overrides'
    MINIMUM_VERSION_REQUIRED_CREATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_770
    MINIMUM_VERSION_REQUIRED_UPDATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
