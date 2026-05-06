from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Resource


class VariableSet(Resource):
    """Retrieves the variable set object associated with the specified ID. If no ID is specified, retrieves list of all variable set objects.

    **Tags:** Object

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllVariableSet` (GET (list))
    - `getVariableSet` (GET)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/object/variablesets/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
