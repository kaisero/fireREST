from fireREST.defaults import API_RELEASE_630
from fireREST.fmc import Resource


class Ikev1Policy(Resource):
    """Retrieves, deletes, creates, or modifies the IKEv1 policy object associated with the specified ID. If no ID is specified for a GET, retrieves list of all IKEv1 policy objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllIkev1PolicyObject` (GET (list))
    - `getIkev1PolicyObject` (GET)
    - `createIkev1PolicyObject` (CREATE)
    - `updateIkev1PolicyObject` (UPDATE)
    - `deleteIkev1PolicyObject` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/object/ikev1policies/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_630
