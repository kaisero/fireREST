from fireREST.defaults import API_RELEASE_760
from fireREST.fmc import Resource


class DownloadSampleCsv(Resource):
    """Downloads a sample CSV file for bulk device registration.

    **Tags:** Devices

    **Supported operations:** GET

    **Operation IDs:**

    - `getDownloadSampleCsv` (GET (list))
    """

    PATH = '/devices/operational/bulkregistrations/downloadsamplecsv'
    MINIMUM_VERSION_REQUIRED_CREATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_UPDATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
