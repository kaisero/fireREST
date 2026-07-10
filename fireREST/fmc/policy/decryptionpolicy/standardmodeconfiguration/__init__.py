from fireREST.defaults import API_RELEASE_1000
from fireREST.fmc import ChildResource


class StandardModeConfiguration(ChildResource):
    """Retrieves or updates the standard mode configuration for the specified decryption policy.

    **Tags:** Policy

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getAllStandardModeConfiguration` (GET (list))
    - `getStandardModeConfiguration` (GET)
    - `updateStandardModeConfiguration` (UPDATE)
    """

    CONTAINER_NAME = 'DecryptionPolicy'
    CONTAINER_PATH = '/policy/decryptionpolicies/{uuid}'
    PATH = '/policy/decryptionpolicies/{container_uuid}/standardmodeconfiguration/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_1000
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
