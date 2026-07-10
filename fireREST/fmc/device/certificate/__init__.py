from fireREST.defaults import API_RELEASE_770
from fireREST.fmc import Resource


class Certificate(Resource):
    """Get a list of all the certificates enrolled in devices.

    **Tags:** Devices

    **Supported operations:** GET

    **Operation IDs:**

    - `getDeviceCertificateModel` (GET (list))

    **Query parameters:**

    - `filter` (string, optional): Filter by `deviceId` or filter by `expiryInDays`. When filtering by `deviceId:{id}`, lists all certificates enrolled on the given device. If filtering by `expiryInDays:{number of days}`, lists only the certificates which will expire within the given number of days.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/devices/certificates'
    MINIMUM_VERSION_REQUIRED_CREATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_770
    MINIMUM_VERSION_REQUIRED_UPDATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
