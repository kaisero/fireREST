from fireREST.defaults import API_RELEASE_760
from fireREST.fmc import Resource


class SupportedDeviceModel(Resource):
    """Retrieves a list of supported device models or the specified model by ID.

    **Tags:** Templates

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllSupportedDeviceModel` (GET (list))
    - `getSupportedDeviceModel` (GET)
    """

    PATH = '/templates/supporteddevicemodels/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_UPDATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
