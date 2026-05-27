from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class ExternalCertificateGroup(Resource):
    """Retrieves list of all the external certificate groups.

    **Tags:** Object

    **Supported operations:** GET

    **Operation IDs:**

    - `getExternalCertificateGroup` (GET (list))

    **Query parameters:**

    - `filter` (string, optional): Filter by name of the external certificate group is supported.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/object/externalcertificategroups/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
