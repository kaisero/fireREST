from fireREST.defaults import API_RELEASE_770
from fireREST.fmc import Resource


class RadKitService(Resource):
    """Get the RADKit Service data from the specified ID.

    **Tags:** Troubleshoot

    **Supported operations:** GET, CREATE

    **Operation IDs:**

    - `getAllRADKitService` (GET (list))
    - `getRADKitService` (GET)
    - `createRADKitService` (CREATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    NAMESPACE = 'troubleshoot'
    PATH = '/radkit/services/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_770
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_770
    MINIMUM_VERSION_REQUIRED_UPDATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
