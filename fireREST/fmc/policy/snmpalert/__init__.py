from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Resource


class SnmpAlert(Resource):
    """Retrieves the SNMP alert object associated with the specified ID.

    **Tags:** Policy

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllSNMPConfig` (GET (list))
    - `getSNMPConfig` (GET)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/policy/snmpalerts/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
