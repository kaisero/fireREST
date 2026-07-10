from fireREST.defaults import API_RELEASE_760
from fireREST.fmc import Resource


class SamlRealmUserAndGroup(Resource):
    """Retrieves SAML realm users and groups.

    **Tags:** Object

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllSamlRealmUserAndGroup` (GET (list))
    """

    PATH = '/object/samlrealmusersandgroups'
    MINIMUM_VERSION_REQUIRED_CREATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_UPDATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
