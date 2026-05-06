from typing import Dict

from fireREST import utils
from fireREST.defaults import API_RELEASE_730
from fireREST.fmc import Resource


class InternalCa(Resource):
    """Retrieves, deletes, creates, or modifies the Internal CA associated with the specified ID. If no ID is specified, retrieves list of all Internal CAs.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllInternalCA` (GET (list))
    - `getInternalCA` (GET)
    - `createInternalCA` (CREATE)
    - `updateInternalCA` (UPDATE)
    - `deleteInternalCA` (DELETE)

    **Query parameters:**

    - `filter` (string, optional): Filter by name of the CA is supported.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `isCSR` (boolean, optional): Boolean parameter to specify if the request is to create a Certificate Signing Request(CSR) or not. `false` by default. When `false`, if a certificate/key pair is provided, the certificate/key pair is imported. Else, a self-signed certificate is generated. When `true`, a CSR is generated.
    """
    PATH = '/object/internalcas/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_730
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_730
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_730
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_730

    @utils.minimum_version_required(version=API_RELEASE_730)
    def download(self, data: Dict, params=None):
        url = self.url('/object/downloadinternalca')
        return self.conn.post(url=url, data=data, params=params)
