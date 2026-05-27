from fireREST.defaults import API_RELEASE_700, API_RELEASE_720
from fireREST.fmc import Resource


class HostscanPackage(Resource):
    """Retrieves, update, deletes or creates the HostScan packages. If no ID is specified for a GET, retrieves list of all HostScan packages.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllHostScanPackageObject` (GET (list))
    - `getHostScanPackageObject` (GET)
    - `createHostScanPackageObject` (CREATE)
    - `updateHostScanPackageObject` (UPDATE)
    - `deleteHostScanPackageObject` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/object/hostscanpackages/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_720
