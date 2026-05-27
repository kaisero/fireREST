from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class CustomSiIpListDownload(Resource):
    """Retrieves the custom Security Intelligence IP List with the specified UUID.

    **Tags:** Object

    **Supported operations:** GET

    **Operation IDs:**

    - `getCustomSIIPListDownload` (GET)
    """

    PATH = '/object/customsiiplistdownload/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
