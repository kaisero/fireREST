from fireREST.defaults import API_RELEASE_760
from fireREST.fmc import Resource


class RealmStatus(Resource):
    """Retrieves the status of all realm synchronization operations.

    **Tags:** Object

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllRealmStatus` (GET (list))
    """

    PATH = '/object/operational/realmstatuses'
    MINIMUM_VERSION_REQUIRED_CREATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_UPDATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
