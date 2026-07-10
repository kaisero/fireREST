from fireREST.defaults import API_RELEASE_1000
from fireREST.fmc import Resource


class Filter(Resource):
    """Retrieves, creates, updates, or deletes analysis filter configurations.

    **Tags:** Analysis

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllFilter` (GET (list))
    - `getFilter` (GET)
    - `createFilter` (CREATE)
    - `updateFilter` (UPDATE)
    - `deleteFilter` (DELETE)
    """

    PATH = '/analysis/filters/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_1000
