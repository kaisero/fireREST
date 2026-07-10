from fireREST.defaults import API_RELEASE_770
from fireREST.fmc import Resource


class TsdbUpload(Resource):
    """Initiates a TSDB data upload to AI Operations.

    **Tags:** Integration

    **Supported operations:** CREATE

    **Operation IDs:**

    - `createPrometheusTSDBUpload` (CREATE)
    """

    PATH = '/integration/aiops/tsdbupload'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_770
    MINIMUM_VERSION_REQUIRED_GET = '99.99.99'
    MINIMUM_VERSION_REQUIRED_UPDATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
