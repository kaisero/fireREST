from fireREST.defaults import API_RELEASE_760
from fireREST.fmc import ChildResource


class VpnSetting(ChildResource):
    """Retrieves, creates, updates, or deletes VPN settings for the specified device template.

    **Tags:** Templates

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllVpnSetting` (GET (list))
    - `getVpnSetting` (GET)
    - `createVpnSetting` (CREATE)
    - `updateVpnSetting` (UPDATE)
    - `deleteVpnSetting` (DELETE)
    """

    CONTAINER_NAME = 'DeviceTemplate'
    CONTAINER_PATH = '/templates/devicetemplates/{uuid}'
    PATH = '/templates/devicetemplates/{container_uuid}/vpnsettings/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_760
