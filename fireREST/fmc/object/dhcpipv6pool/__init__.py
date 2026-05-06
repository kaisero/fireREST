from fireREST.defaults import API_RELEASE_730
from fireREST.fmc import Resource


class DhcpIpv6Pool(Resource):
    """Retrieves, deletes, creates, or modifies the DHCP IPv6 pool object associated with the specified ID. If no ID is specified, retrieves list of all DHCP IPv6 Pool objects

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllDHCPIPv6Pool` (GET (list))
    - `getDHCPIPv6Pool` (GET)
    - `createDHCPIPv6Pool` (CREATE)
    - `updateDHCPIPv6Pool` (UPDATE)
    - `deleteDHCPIPv6Pool` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/object/dhcpipv6pools/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_730
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_730
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_730
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_730
