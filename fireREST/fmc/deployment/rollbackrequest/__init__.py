from fireREST.defaults import API_RELEASE_670
from fireREST.fmc import Resource


class RollbackRequest(Resource):
    """Creates a request for rollback configuration to devices.

    **Tags:** Deployment

    **Supported operations:** CREATE

    **Operation IDs:**

    - `createRollbackRequest` (CREATE)
    """
    PATH = '/deployment/rollbackrequests/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_670
