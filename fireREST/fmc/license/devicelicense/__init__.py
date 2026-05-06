from fireREST.defaults import API_RELEASE_720
from fireREST.fmc import Resource


class DeviceLicense(Resource):
    """Retrieves the Device Licenses associated with the specified ID.

    **Tags:** License

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllDeviceLicense` (GET (list))
    - `getDeviceLicense` (GET)
    - `updateMultipleDeviceLicense` (UPDATE (bulk))
    - `updateDeviceLicense` (UPDATE)

    **Query parameters:**

    - `filter` (string, optional): [DEV ERROR: Missing description]
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean): [DEV ERROR: Missing description]
    """
    NAMESPACE = 'platform'
    PATH = '/license/devicelicenses/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_720
