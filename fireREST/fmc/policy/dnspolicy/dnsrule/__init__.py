from fireREST.defaults import API_RELEASE_1000
from fireREST.fmc import ChildResource


class DnsRule(ChildResource):
    """Retrieves, creates, updates, or deletes DNS rules for the specified DNS policy.

    **Tags:** Policy

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllDnsRule` (GET (list))
    - `getDnsRule` (GET)
    - `createDnsRule` (CREATE)
    - `updateDnsRule` (UPDATE)
    - `deleteDnsRule` (DELETE)
    """

    CONTAINER_NAME = 'DnsPolicy'
    CONTAINER_PATH = '/policy/dnspolicies/{uuid}'
    PATH = '/policy/dnspolicies/{container_uuid}/dnsrules/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_1000
