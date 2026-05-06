from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Resource


class DeviceGroupRecord(Resource):
    """Retrieves, deletes, creates, or modifies the device group associated with the specified ID. If no ID is specified for a GET, retrieves list of all device groups.

    **Tags:** Device Groups

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllDeviceGroup` (GET (list))
    - `getDeviceGroup` (GET)
    - `createDeviceGroup` (CREATE)
    - `updateDeviceGroup` (UPDATE)
    - `deleteDeviceGroup` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/devicegroups/devicegrouprecords/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_610
