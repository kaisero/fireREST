from fireREST.defaults import API_RELEASE_760
from fireREST.fmc import Resource


class DownloadRealm(Resource):
    """Initiates a realm download operation.

    **Tags:** Object

    **Supported operations:** CREATE

    **Operation IDs:**

    - `createDownloadRealm` (CREATE)
    """

    PATH = '/object/realms/operational/download'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_GET = '99.99.99'
    MINIMUM_VERSION_REQUIRED_UPDATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
