from fireREST.defaults import API_RELEASE_1000
from fireREST.fmc import Resource


class FetchLdapAttributes(Resource):
    """Fetches LDAP attributes for external authentication.

    **Tags:** User

    **Supported operations:** CREATE

    **Operation IDs:**

    - `createFetchLdapAttributes` (CREATE)
    """

    PATH = '/users/externalauths/operational/fetchattrs'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_GET = '99.99.99'
    MINIMUM_VERSION_REQUIRED_UPDATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
