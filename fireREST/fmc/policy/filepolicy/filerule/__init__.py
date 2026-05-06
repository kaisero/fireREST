from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import ChildResource


class FileRule(ChildResource):
    """Retrieves the file rule associated with the specified ID.

    **Tags:** Policy

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllFileRuleModel` (GET (list))
    - `getFileRuleModel` (GET)
    - `createFileRuleModel` (CREATE)
    - `updateFileRuleModel` (UPDATE)
    - `deleteFileRuleModel` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    CONTAINER_NAME = 'FilePolicy'
    CONTAINER_PATH = '/policy/filepolicies/{uuid}'
    PATH = '/policy/filepolicies/{container_uuid}/filerules/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_740
