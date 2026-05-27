from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import ChildResource


class SecureClientCustomizationSettings(ChildResource):
    """Retrieves Secure Client Customization Setting inside a VPN RA Topology.

    **Tags:** Policy

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllFTDRAVpnSecureClientCustomizationSetting` (GET (list))
    - `getFTDRAVpnSecureClientCustomizationSetting` (GET)
    - `updateFTDRAVpnSecureClientCustomizationSetting` (UPDATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'RaVpn'
    CONTAINER_PATH = '/policy/ravpns/{uuid}'
    PATH = '/policy/ravpns/{container_uuid}/secureclientcustomizationsettings/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
