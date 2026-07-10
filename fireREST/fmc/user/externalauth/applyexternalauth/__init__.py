from fireREST.defaults import API_RELEASE_1000
from fireREST.fmc import Resource


class ApplyExternalAuth(Resource):
    """Applies external authentication configuration.

    **Tags:** User

    **Supported operations:** CREATE

    **Operation IDs:**

    - `createApplyExternalAuth` (CREATE)
    """

    PATH = '/users/externalauths/operational/apply'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_GET = '99.99.99'
    MINIMUM_VERSION_REQUIRED_UPDATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
