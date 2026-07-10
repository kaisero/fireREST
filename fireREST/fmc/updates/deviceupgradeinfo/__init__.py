from fireREST.defaults import API_RELEASE_1000
from fireREST.fmc import Resource


class DeviceUpgradeInfo(Resource):
    """Retrieves device upgrade information.

    **Tags:** Updates

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllDeviceUpgradeInfo` (GET (list))
    - `getDeviceUpgradeInfo` (GET)
    """

    NAMESPACE = 'platform'
    PATH = '/updates/deviceupgradeinfo/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_UPDATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
