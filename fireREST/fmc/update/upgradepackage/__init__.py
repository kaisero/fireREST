from fireREST.defaults import API_RELEASE_630
from fireREST.fmc import Resource
from fireREST.fmc.update.upgradepackage.applicabledevice import ApplicableDevice


class UpgradePackage(Resource):
    """Retrieves the upgrade packages associated with the specified ID.

    **Tags:** Updates

    **Supported operations:** GET, DELETE

    **Operation IDs:**

    - `getAllUpgradePackage` (GET (list))
    - `getUpgradePackage` (GET)
    - `deleteUpgradePackage` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    NAMESPACE = 'platform'
    PATH = '/updates/upgradepackages/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_630

    def __init__(self, conn):
        super().__init__(conn)

        self.applicabledevice = ApplicableDevice(conn)
