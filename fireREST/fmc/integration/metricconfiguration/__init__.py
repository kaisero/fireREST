from fireREST.defaults import API_RELEASE_1000
from fireREST.fmc import Resource


class MetricConfiguration(Resource):
    """Retrieves or creates AIOps metric configuration.

    **Tags:** Integration

    **Supported operations:** GET, CREATE

    **Operation IDs:**

    - `getAllMetricConfiguration` (GET (list))
    - `createMetricConfiguration` (CREATE)
    """

    PATH = '/integration/aiops/metricconfiguration'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_UPDATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
