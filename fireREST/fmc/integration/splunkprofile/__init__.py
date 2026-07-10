from fireREST.defaults import API_RELEASE_1000
from fireREST.fmc import Resource


class SplunkProfile(Resource):
    """Retrieves, creates, updates, or deletes Splunk integration profiles.

    **Tags:** Integration

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllSplunkProfile` (GET (list))
    - `getSplunkProfile` (GET)
    - `createSplunkProfile` (CREATE)
    - `updateSplunkProfile` (UPDATE)
    - `deleteSplunkProfile` (DELETE)
    """

    PATH = '/integration/splunk/profiles/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_1000
