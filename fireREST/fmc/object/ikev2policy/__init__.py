from fireREST.defaults import API_RELEASE_630
from fireREST.fmc import Resource


class Ikev2Policy(Resource):
    """Retrieves, deletes, creates, or modifies the IKEv2 object associated with the specified ID. If no ID is specified for a GET, retrieves list of all IKEv2 monitor objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllIkev2PolicyObject` (GET (list))
    - `getIkev2PolicyObject` (GET)
    - `createIkev2PolicyObject` (CREATE)
    - `updateIkev2PolicyObject` (UPDATE)
    - `deleteIkev2PolicyObject` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/object/ikev2policies/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_630
