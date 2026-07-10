from fireREST.defaults import API_RELEASE_1000
from fireREST.fmc import Resource


class ExternalAuth(Resource):
    """Retrieves or updates external authentication configuration.

    **Tags:** User

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllExternalAuth` (GET (list))
    - `updateExternalAuth` (UPDATE)
    """

    PATH = '/users/externalauths'
    MINIMUM_VERSION_REQUIRED_CREATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
