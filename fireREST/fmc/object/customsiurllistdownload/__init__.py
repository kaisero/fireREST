from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class CustomSiUrlListDownload(Resource):
    """Retrieves the custom Security Intelligence URL List with the specified UUID.

    **Tags:** Object

    **Supported operations:** GET

    **Operation IDs:**

    - `getCustomSIURLListDownload` (GET)
    """
    PATH = '/object/customsiurllistdownload/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
