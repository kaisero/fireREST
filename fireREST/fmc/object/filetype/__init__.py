from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class FileType(Resource):
    """Retrieves the file type associated with the specified ID. If no ID is specified, retrieves a list of all the file types.

    **Tags:** Object

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllFileTypeModel` (GET (list))
    - `getFileTypeModel` (GET)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/object/filetypes/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
