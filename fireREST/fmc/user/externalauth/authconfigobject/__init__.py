from fireREST.defaults import API_RELEASE_1000
from fireREST.fmc import Resource


class AuthConfigObject(Resource):
    """Retrieves all authentication configuration objects.

    **Tags:** User

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllAuthConfigObject` (GET (list))
    """

    PATH = '/users/externalauths/authconfigobjects'
    MINIMUM_VERSION_REQUIRED_CREATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_UPDATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
