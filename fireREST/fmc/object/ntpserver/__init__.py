from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class NtpServer(Resource):
    """Retrieves, deletes, creates, or modifies the NTP Server object associated with the specified ID. If no ID is specified for a GET, retrieves list of all NTP Server objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllNTPServerObject` (GET (list))
    - `getNTPServerObject` (GET)
    - `createNTPServerObject` (CREATE)
    - `updateNTPServerObject` (UPDATE)
    - `deleteNTPServerObject` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/object/ntpservers/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_740
