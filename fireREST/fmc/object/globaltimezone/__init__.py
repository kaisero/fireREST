from fireREST.defaults import API_RELEASE_660
from fireREST.fmc import Resource


class GlobalTimeZone(Resource):
    """Retrieves the objects representing all the time zones defined in the IANA global time zone (tz) database.

    **Tags:** Object

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllGlobalTimeZone` (GET (list))
    - `getGlobalTimeZone` (GET)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/object/globaltimezones/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_660
