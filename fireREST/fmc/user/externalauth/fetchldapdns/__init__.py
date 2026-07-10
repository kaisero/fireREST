from fireREST.defaults import API_RELEASE_1000
from fireREST.fmc import Resource


class FetchLdapDns(Resource):
    """Fetches LDAP distinguished names for external authentication.

    **Tags:** User

    **Supported operations:** CREATE

    **Operation IDs:**

    - `createFetchLdapDns` (CREATE)
    """

    PATH = '/users/externalauths/operational/fetchdns'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_GET = '99.99.99'
    MINIMUM_VERSION_REQUIRED_UPDATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
