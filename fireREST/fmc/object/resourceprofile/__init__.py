from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class ResourceProfile(Resource):
    """Retrieves, deletes, creates, or modifies the ResourceProfile object associated with the specified ID. If no ID is specified for a GET, retrieves list of all ResourceProfile objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllResourceProfile` (GET (list))
    - `getResourceProfile` (GET)
    - `createResourceProfile` (CREATE)
    - `updateResourceProfile` (UPDATE)
    - `deleteResourceProfile` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/object/resourceprofiles/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_740
