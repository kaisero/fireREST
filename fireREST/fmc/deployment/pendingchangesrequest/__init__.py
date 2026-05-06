from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class PendingChangesRequest(Resource):
    """Creates a request for generating pending policy changes or pending CLI changes or both on devices.

    **Tags:** Deployment

    **Supported operations:** CREATE

    **Operation IDs:**

    - `createPendingChangesRequest` (CREATE)
    """
    PATH = '/deployment/pendingchangesrequests/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_740
