from fireREST.defaults import API_RELEASE_760
from fireREST.fmc import ChildResource


class SnortProfilerRule(ChildResource):
    """Retrieves or creates Snort profiler rules for the specified profiler session.

    **Tags:** Troubleshoot

    **Supported operations:** GET, CREATE

    **Operation IDs:**

    - `getAllSnortProfilerRule` (GET (list))
    - `getSnortProfilerRule` (GET)
    - `createSnortProfilerRule` (CREATE)
    """

    NAMESPACE = 'troubleshoot'
    CONTAINER_NAME = 'SnortProfiler'
    CONTAINER_PATH = '/snortprofiler/{uuid}'
    PATH = '/snortprofiler/{container_uuid}/rules/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_UPDATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
