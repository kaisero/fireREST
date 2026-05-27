from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class CdfmcSnapshot(Resource):
    """[DEV ERROR: Missing description]

    **Tags:** Integration

    **Supported operations:** GET, CREATE

    **Operation IDs:**

    - `getCdFMCSnapshot` (GET)
    - `createCdFMCSnapshot` (CREATE)
    """

    PATH = '/integration/cdfmcsnapshot/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
