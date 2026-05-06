from fireREST.defaults import API_RELEASE_730
from fireREST.fmc import Resource


class BfdTemplate(Resource):
    """Retrieves, deletes, creates, or modifies the BFDTemplate object associated with the specified ID. If no ID is specified for a GET, retrieves list of all Bidirectional Forwarding Detection routing template objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllBFDTemplate` (GET (list))
    - `getBFDTemplate` (GET)
    - `createBFDTemplate` (CREATE)
    - `updateBFDTemplate` (UPDATE)
    - `deleteBFDTemplate` (DELETE)

    **Query parameters:**

    - `filter` (string, optional): To filter BFD templates based on hop type, use `hopType:{hopType}`. Supported hop types are Single-Hop and Multi-Hop.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/object/bfdtemplates/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_730
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_730
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_730
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_730
