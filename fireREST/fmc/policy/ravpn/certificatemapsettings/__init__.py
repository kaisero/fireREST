from fireREST.defaults import API_RELEASE_700, API_RELEASE_720
from fireREST.fmc import ChildResource


class CertificateMapSettings(ChildResource):
    """Retrieves Certificate Map Setting inside a VPN RA Topology.

    **Tags:** Policy

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getFTDRAVpnCertificateMapSettings` (GET)
    - `updateFTDRAVpnCertificateMapSettings` (UPDATE)
    """
    CONTAINER_NAME = 'RaVpn'
    CONTAINER_PATH = '/policy/ravpns/{uuid}'
    PATH = '/policy/ravpns/{container_uuid}/certificatemapsettings/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_720
