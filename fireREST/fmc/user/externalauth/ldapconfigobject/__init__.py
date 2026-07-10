from fireREST.defaults import API_RELEASE_1000
from fireREST.fmc import Resource


class LdapConfigObject(Resource):
    """Retrieves, creates, updates, or deletes LDAP authentication configuration objects.

    **Tags:** User

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllLdapConfigObject` (GET (list))
    - `getLdapConfigObject` (GET)
    - `createLdapConfigObject` (CREATE)
    - `updateLdapConfigObject` (UPDATE)
    - `deleteLdapConfigObject` (DELETE)
    """

    PATH = '/users/externalauths/authconfigobjects/ldapconfigobjects/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_1000
