from fireREST.defaults import API_RELEASE_1000
from fireREST.fmc import ChildResource


class PcapDetail(ChildResource):
    """Retrieves or submits PCAP detail analysis for the specified packet tracer PCAP file.

    **Tags:** Troubleshoot

    **Supported operations:** GET, CREATE

    **Operation IDs:**

    - `getPcapDetail` (GET)
    - `createPcapDetail` (CREATE)
    """

    NAMESPACE = 'troubleshoot'
    CONTAINER_NAME = 'File'
    CONTAINER_PATH = '/packettracer/files/{uuid}'
    PATH = '/packettracer/files/{container_uuid}/details'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_UPDATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
