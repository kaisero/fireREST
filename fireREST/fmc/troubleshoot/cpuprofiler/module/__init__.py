from fireREST.defaults import API_RELEASE_760
from fireREST.fmc import ChildResource


class CpuProfilerModule(ChildResource):
    """Retrieves or creates CPU profiler modules for the specified profiler session.

    **Tags:** Troubleshoot

    **Supported operations:** GET, CREATE

    **Operation IDs:**

    - `getAllCpuProfilerModule` (GET (list))
    - `getCpuProfilerModule` (GET)
    - `createCpuProfilerModule` (CREATE)
    """

    NAMESPACE = 'troubleshoot'
    CONTAINER_NAME = 'CpuProfiler'
    CONTAINER_PATH = '/cpuprofiler/{uuid}'
    PATH = '/cpuprofiler/{container_uuid}/modules/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_UPDATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
