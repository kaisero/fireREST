from fireREST.defaults import API_RELEASE_770
from fireREST.fmc import Connection, Resource
from fireREST.fmc.object.serviceaccessobjectoverride import ServiceAccessObjectOverride


class ServiceAccessObject(Resource):
    """Retrieves, creates, updates, or deletes service access objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllServiceAccessObject` (GET (list))
    - `getServiceAccessObject` (GET)
    - `createServiceAccessObject` (CREATE)
    - `updateServiceAccessObject` (UPDATE)
    - `deleteServiceAccessObject` (DELETE)
    """

    PATH = '/object/serviceaccessobjects/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_770
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_770
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_770
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_770

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.override = ServiceAccessObjectOverride(conn)
