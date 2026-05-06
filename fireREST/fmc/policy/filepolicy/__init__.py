from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Connection, Resource
from fireREST.fmc.policy.filepolicy.filerule import FileRule


class FilePolicy(Resource):
    """Retrieves the File Policy associated with the specified ID.

    **Tags:** Policy

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllFilePolicy` (GET (list))
    - `getFilePolicy` (GET)
    - `createFilePolicy` (CREATE)
    - `updateFilePolicy` (UPDATE)
    - `deleteFilePolicy` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/policy/filepolicies/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.filerule = FileRule(conn)
