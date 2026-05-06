from fireREST.defaults import API_RELEASE_730
from fireREST.fmc import ChildResource


class Transcript(ChildResource):
    """Retrieves Transcript for Umbrella deployment for a given device and topology.

    **Tags:** Integration

    **Supported operations:** GET

    **Operation IDs:**

    - `getUmbrellaDeploymentTranscript` (GET)
    """
    CONTAINER_NAME = 'TunnelDeployment'
    CONTAINER_PATH = '/integration/umbrella/tunneldeployments/{uuid}'
    PATH = '/integration/umbrella/tunneldeployments/{container_uuid}/transcripts/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_730
