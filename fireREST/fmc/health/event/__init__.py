from fireREST.defaults import API_RELEASE_760
from fireREST.fmc import Resource


class Event(Resource):
    """Retrieves health events.

    **Tags:** Health

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllHealthEvent` (GET (list))
    """

    PATH = '/health/events'
    MINIMUM_VERSION_REQUIRED_CREATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_UPDATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
