from typing import Dict

from fireREST import utils
from fireREST.defaults import API_RELEASE_730
from fireREST.fmc import Resource


class InternalCertificate(Resource):
    """Retrieves, deletes, creates, or modifies the Internal Certificate associated with the specified ID. If no ID is specified, retrieves list of all Internal Certificates.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllInternalCertificate` (GET (list))
    - `getInternalCertificate` (GET)
    - `createInternalCertificate` (CREATE)
    - `updateInternalCertificate` (UPDATE)
    - `deleteInternalCertificate` (DELETE)

    **Query parameters:**

    - `filter` (string, optional): Filter by name of certificate is supported.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/object/internalcertificates/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_730
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_730
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_730
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_730

    @utils.minimum_version_required(version=API_RELEASE_730)
    def validate(self, data: Dict, params=None):
        url = self.url('/object/validatecertfile')
        return self.conn.post(url=url, data=data, params=params)
