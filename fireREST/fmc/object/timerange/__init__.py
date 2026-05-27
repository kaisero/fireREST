from fireREST.defaults import API_RELEASE_660
from fireREST.fmc import Resource


class Timerange(Resource):
    """Retrieves, deletes, creates and modifies the TimeRange object.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllTimeRange` (GET (list))
    - `getTimeRange` (GET)
    - `createMultipleTimeRange` (CREATE)
    - `updateTimeRange` (UPDATE)
    - `deleteTimeRange` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean, optional): Enables bulk create for TimeRange objects.
    """

    PATH = '/object/timeranges/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_660
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_660
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_660
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_660
