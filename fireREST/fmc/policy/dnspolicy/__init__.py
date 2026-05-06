from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import Connection, Resource
from fireREST.fmc.policy.dnspolicy.allowdnsrule import AllowDnsRule
from fireREST.fmc.policy.dnspolicy.blockdnsrule import BlockDnsRule


class DnsPolicy(Resource):
    """Retrieves the DNS Policy.

    **Tags:** Policy

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllDNSPolicy` (GET (list))
    - `getDNSPolicy` (GET)

    **Query parameters:**

    - `filter` (string, optional): Filter criteria can be specified using the format `name:policyname` `policyname` -- Name of the DNS Policy to be queried.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/policy/dnspolicies/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700

    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.allowdnsrule = AllowDnsRule(conn)
        self.blockdnsrule = BlockDnsRule(conn)
