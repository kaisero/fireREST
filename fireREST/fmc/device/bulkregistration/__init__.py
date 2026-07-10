from fireREST.defaults import API_RELEASE_760
from fireREST.fmc import Resource


class BulkRegistration(Resource):
    """Initiates bulk registration of devices from a CSV file.

    **Tags:** Devices

    **Supported operations:** CREATE

    **Operation IDs:**

    - `createBulkRegistration` (CREATE)
    """

    PATH = '/devices/operational/bulkregistrations'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_GET = '99.99.99'
    MINIMUM_VERSION_REQUIRED_UPDATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
