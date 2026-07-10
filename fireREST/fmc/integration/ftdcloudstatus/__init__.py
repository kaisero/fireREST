from fireREST.defaults import API_RELEASE_1000
from fireREST.fmc import Resource


class FtdCloudStatus(Resource):
    """Get the cloud connectivity status of FTD managed by cdFMC.

    **Tags:** Integration

    **Supported operations:** GET

    **Operation IDs:**

    - `getFTDCloudStatus` (GET)
    """

    PATH = '/integration/ftdcloudstatus/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_UPDATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
