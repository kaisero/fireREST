from fireREST.defaults import API_RELEASE_720
from fireREST.fmc import ChildResource


class LdapAttributeMap(ChildResource):
    """Retrieves LDAP Attribute Maps inside a VPN RA Topology.

    **Tags:** Policy

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllFTDRAVpnLDAPAttributeModel` (GET (list))
    - `getFTDRAVpnLDAPAttributeModel` (GET)
    - `updateFTDRAVpnLDAPAttributeModel` (UPDATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    CONTAINER_NAME = 'RaVpn'
    CONTAINER_PATH = '/policy/ravpns/{uuid}'
    PATH = '/policy/ravpns/{container_uuid}/ldapattributemaps/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_720
