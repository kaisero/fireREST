from fireREST.defaults import API_RELEASE_720
from fireREST.fmc import Resource


class EbsSnapshot(Resource):
    """Retrieves or creates an EBS snapshot.

    **Tags:** Integration

    **Supported operations:** GET, CREATE

    **Operation IDs:**

    - `getEBSSnapshot` (GET)
    - `createEBSSnapshot` (CREATE)
    """
    PATH = '/integration/ebssnapshot/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_720
