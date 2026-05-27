from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class NetworkAddressOverride(Resource):
    """Retrieves list of all types of network override objects - Network, Host, Range and FQDN.

    **Tags:** Object

    **Supported operations:** GET

    **Operation IDs:**

    - `getNetworkAddressOverrides` (GET (list))

    **Query parameters:**

    - `networkType` (string, optional): To be used to get all override objects based on type. Here, type is Host, Network, Range, or FQDN.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/object/networkaddressoverrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
