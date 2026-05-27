from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class FileCategory(Resource):
    """Retrieves the file category associated with the specified ID. If no ID is specified, retrieves a list of all the file categories.

    **Tags:** Object

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllFileCategoryModel` (GET (list))
    - `getFileCategoryModel` (GET)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    PATH = '/object/filecategories/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
