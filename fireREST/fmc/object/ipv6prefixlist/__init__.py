from fireREST.defaults import API_RELEASE_660, API_RELEASE_710
from fireREST.fmc import Resource


class Ipv6PrefixList(Resource):
    """Retrieves, deletes, creates, or modifies the IPv6 Prefix List associated with the specified ID. If no ID is specified, retrieves list of all IPv6 Prefix Lists.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllIPv6PrefixList` (GET (list))
    - `getIPv6PrefixList` (GET)
    - `createIPv6PrefixList` (CREATE)
    - `updateIPv6PrefixList` (UPDATE)
    - `deleteIPv6PrefixList` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/object/ipv6prefixlists/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_660
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_710
