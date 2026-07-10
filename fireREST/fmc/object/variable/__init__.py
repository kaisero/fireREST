from fireREST.defaults import API_RELEASE_760
from fireREST.fmc import Resource


class Variable(Resource):
    """Retrieves, creates, updates, or deletes variable objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllVariable` (GET (list))
    - `getVariable` (GET)
    - `createVariable` (CREATE)
    - `updateVariable` (UPDATE)
    - `deleteVariable` (DELETE)
    """

    PATH = '/object/variables/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_760
