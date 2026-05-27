from fireREST.defaults import API_RELEASE_720
from fireREST.fmc import Resource


class SmartLicense(Resource):
    """API operations on Smart Licenses including: retrieving registration status, requesting license registration, de-registering Smart Licenses and activating evaluation mode.

    **Tags:** License

    **Supported operations:** GET, CREATE

    **Operation IDs:**

    - `getSmartLicense` (GET (list))
    - `createSmartLicense` (CREATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    NAMESPACE = 'platform'
    PATH = '/license/smartlicenses/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_720
