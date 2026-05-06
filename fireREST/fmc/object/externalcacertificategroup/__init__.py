from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class ExternalCaCertificateGroup(Resource):
    """Retrieves the list of all trusted CA groups.

    **Tags:** Object

    **Supported operations:** GET

    **Operation IDs:**

    - `getExternalCACertificateGroup` (GET (list))

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/object/externalcacertificategroups/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
