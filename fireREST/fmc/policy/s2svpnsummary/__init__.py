from fireREST.defaults import API_RELEASE_720
from fireREST.fmc import Resource


class S2sVpnSummary(Resource):
    """Get all the configured S2S VPN in the system, with short summary along with the health of the tunnels.

    **Tags:** Policy

    **Supported operations:** GET

    **Operation IDs:**

    - `getS2SVpnSummaryModel` (GET (list))

    **Query parameters:**

    - `filter` (string, optional): The filter criteria for which the details have to be fetched. The following filters are supported - device:{deviceId};name:{Topology name};routeBased:{true|false};includeSubDomains:{true|false}. User can enter one or many filters.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/policy/s2svpnsummaries'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_720
