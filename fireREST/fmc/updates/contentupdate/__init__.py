from fireREST.defaults import API_RELEASE_1000
from fireREST.fmc import Resource


class ContentUpdate(Resource):
    """Retrieves or updates content update information.

    **Tags:** Updates

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllContentUpdate` (GET (list))
    - `getContentUpdate` (GET)
    - `updateContentUpdate` (UPDATE)
    """

    NAMESPACE = 'platform_with_domain'
    PATH = '/updates/contentupdates/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
