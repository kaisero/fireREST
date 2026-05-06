from typing import Dict

from fireREST import utils
from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class AzureAdRealm(Resource):
    """Retrieves, deletes, creates, or modifies the Azure AD Realm associated with the specified ID. If no ID is specified for a GET, retrieves list of all Azure AD Realms.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllAzureADRealm` (GET (list))
    - `getAzureADRealm` (GET)
    - `createAzureADRealm` (CREATE)
    - `updateAzureADRealm` (UPDATE)
    - `deleteAzureADRealm` (DELETE)

    **Query parameters:**

    - `filter` (string, optional): Filter by any of the following fields: name, tenantId, clientId
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/object/azureadrealms/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_740

    @utils.minimum_version_required(version=API_RELEASE_740)
    def download(self, uuid: str, data: Dict, params=None):
        url = self.url(f'/object/azureadrealms/{uuid}/download')
        return self.conn.post(url=url, data=data, params=params)

    @utils.minimum_version_required(version=API_RELEASE_740)
    def usersandgroups(self, uuid: str, params=None):
        url = self.url(f'/object/azureadrealms/{uuid}/usersandgroups')
        return self.conn.get(url=url, params=params)
