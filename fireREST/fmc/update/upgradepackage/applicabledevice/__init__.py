from fireREST.defaults import API_RELEASE_630
from fireREST.fmc import ChildResource


class ApplicableDevice(ChildResource):
    """Retrieves the devices available for a particular upgrade package associated with the specified ID.

    **Tags:** Updates

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllApplicableDevice` (GET (list))

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    CONTAINER_NAME = 'UpgradePackage'
    CONTAINER_PATH = '/updates/upgradepackages/{uuid}'
    NAMESPACE = 'platform'
    PATH = '/updates/upgradepackages/{container_uuid}/applicabledevices/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_630
