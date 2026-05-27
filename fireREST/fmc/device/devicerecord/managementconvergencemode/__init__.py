from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import ChildResource


class ManagementConvergenceMode(ChildResource):
    """Retrieves, modifies the convergence state of the device

    **Tags:** Devices

    **Supported operations:** GET, CREATE

    **Operation IDs:**

    - `getManagementInterfaceConvergence` (GET (list))
    - `createManagementInterfaceConvergence` (CREATE)

    **Query parameters:**

    - `checkConvergenceReadiness` (boolean, optional): Lists all the usages of the Management interface when the device is non converged.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `ignoreWarning` (boolean, optional): Performs merge of management interface even if there are warnings
    """

    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/managementconvergencemode/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
