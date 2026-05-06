from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class DistinguishedNameGroup(Resource):
    """Retrieves the list of all Distinguished Name group objects.

    **Tags:** Object

    **Supported operations:** GET

    **Operation IDs:**

    - `getDistinguishedNameGroup` (GET (list))

    **Query parameters:**

    - `filter` (string, optional): Filter by name of the Distinguished Name group is supported.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/object/distinguishednamegroups/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
