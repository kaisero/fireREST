from fireREST.defaults import API_RELEASE_1000
from fireREST.fmc import Resource


class ContentUpdateOperation(Resource):
    """Triggers a content update operation.

    **Tags:** Updates

    **Supported operations:** CREATE

    **Operation IDs:**

    - `createContentUpdateOperation` (CREATE)
    """

    NAMESPACE = 'platform_with_domain'
    PATH = '/updates/contentupdateoperation'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_GET = '99.99.99'
    MINIMUM_VERSION_REQUIRED_UPDATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
