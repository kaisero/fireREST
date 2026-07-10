from fireREST.defaults import API_RELEASE_1000
from fireREST.fmc import Resource


class BulkCommand(Resource):
    """Executes a bulk command operation across multiple device records.

    **Tags:** Devices

    **Supported operations:** CREATE

    **Operation IDs:**

    - `createBulkCommand` (CREATE)
    """

    PATH = '/devices/devicerecords/operational/bulkcommands'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_GET = '99.99.99'
    MINIMUM_VERSION_REQUIRED_UPDATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
