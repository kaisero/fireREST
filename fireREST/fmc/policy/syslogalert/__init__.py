from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Resource


class SyslogAlert(Resource):
    """Retrieves the syslog alert object associated with the specified ID.

    **Tags:** Policy

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllSyslogConfig` (GET (list))
    - `getSyslogConfig` (GET)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/policy/syslogalerts/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
