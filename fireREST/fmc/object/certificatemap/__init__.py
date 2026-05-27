from fireREST.defaults import API_RELEASE_700, API_RELEASE_720
from fireREST.fmc import Resource


class CertificateMap(Resource):
    """Retrieves the Certificate Map associated with the specified ID. If no ID is specified for a GET, retrieves list of all Certificate Map objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllCertificateMapModel` (GET (list))
    - `getCertificateMapModel` (GET)
    - `createCertificateMapModel` (CREATE)
    - `updateCertificateMapModel` (UPDATE)
    - `deleteCertificateMapModel` (DELETE)

    **Query parameters:**

    - `filter` (string, optional): To be used in conjunction with `"unusedOnly:true"` to search for unused objects and `"nameOrValue:{nameOrValue}"` to search for both name and value.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/object/certificatemaps/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_720
