from fireREST.defaults import API_RELEASE_760
from fireREST.fmc import Resource


class LtpDeviceRecord(Resource):
    """Retrieves or deletes LTP device records.

    **Tags:** Devices

    **Supported operations:** GET, DELETE

    **Operation IDs:**

    - `getAllLtpDeviceRecord` (GET (list))
    - `getLtpDeviceRecord` (GET)
    - `deleteLtpDeviceRecord` (DELETE)
    """

    PATH = '/devices/ltpdevicerecords/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_UPDATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_760
