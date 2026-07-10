from fireREST.defaults import API_RELEASE_760
from fireREST.fmc import Resource


class TestRealm(Resource):
    """Initiates a realm test operation.

    **Tags:** Object

    **Supported operations:** CREATE

    **Operation IDs:**

    - `createTestRealm` (CREATE)
    """

    PATH = '/object/operational/testrealms'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_GET = '99.99.99'
    MINIMUM_VERSION_REQUIRED_UPDATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
