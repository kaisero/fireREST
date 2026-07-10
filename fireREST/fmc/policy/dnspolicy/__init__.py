from fireREST.defaults import API_RELEASE_700, API_RELEASE_1000
from fireREST.fmc import Connection, Resource
from fireREST.fmc.policy.dnspolicy.allowdnsrule import AllowDnsRule
from fireREST.fmc.policy.dnspolicy.blockdnsrule import BlockDnsRule
from fireREST.fmc.policy.dnspolicy.dnsrule import DnsRule


class DnsPolicy(Resource):
    """Retrieves the DNS Policy.

    **Tags:** Policy

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllDNSPolicy` (GET (list))
    - `getDNSPolicy` (GET)
    - `createDNSPolicy` (CREATE)
    - `updateDNSPolicy` (UPDATE)
    - `deleteDNSPolicy` (DELETE)

    **Query parameters:**

    - `filter` (string, optional): Filter criteria can be specified using the format `name:policyname` `policyname` -- Name of the DNS Policy to be queried.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/policy/dnspolicies/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_1000

    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.allowdnsrule = AllowDnsRule(conn)
        self.blockdnsrule = BlockDnsRule(conn)
        self.dnsrule = DnsRule(conn)
