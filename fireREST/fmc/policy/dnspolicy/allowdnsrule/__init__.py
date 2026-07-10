from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import ChildResource


class AllowDnsRule(ChildResource):
    """Get the allow rules for a DNS policy.

    **Tags:** Policy

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllowDNSRule` (GET (list))

    **Query parameters:**

    - `filter` (string, optional): Filter criteria can be specified using the format `name:rulename` `rulename` -- Name of the allow rule to be queried
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    CONTAINER_NAME = 'DnsPolicy'
    CONTAINER_PATH = '/policy/dnspolicies/{uuid}'
    PATH = '/policy/dnspolicies/{container_uuid}/allowdnsrules'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
