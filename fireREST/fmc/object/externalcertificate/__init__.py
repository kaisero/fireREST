from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class ExternalCertificate(Resource):
    """Retrieves or creates external certificate objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE

    **Operation IDs:**

    - `getExternalCertificate` (GET (list))
    - `createExternalCertificate` (CREATE)

    **Query parameters:**

    - `filter` (string, optional): Filter by name of the certificate is supported.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/object/externalcertificates/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
