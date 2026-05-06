from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class AzureAdStatus(Resource):
    """This object can be used to get Azure AD realm statuses.

    **Tags:** Object

    **Supported operations:** GET

    **Operation IDs:**

    - `getAzureADStatus` (GET (list))

    **Query parameters:**

    - `ids` (string): Identifiers of realms whose statuses will be received. The values are separated by commas.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/object/azureadstatuses/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
