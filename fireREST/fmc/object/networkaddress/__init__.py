from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Resource


class NetworkAddress(Resource):
    """Retrieves list of all types of network objects - Network, Host, Range and FQDN.

    **Tags:** Object

    **Supported operations:** GET

    **Operation IDs:**

    - `getNetworkAddress` (GET (list))

    **Query parameters:**

    - `filter` (string, optional): To be used in conjunction with `"unusedOnly:true"` to search for unused objects and `"nameOrValue:{nameOrValue}"` to search for both name and value and `"type:{subType}"` to search for specific subType of the network object. `"type:{FQDN,RANGE,HOST,NETWORK}"` is for include and `"type!{FQDN,RANGE,HOST,NETWORK}"` is for exclude. To search for wildcard object type:NETWORK;includeWildcard:true.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/object/networkaddresses/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
