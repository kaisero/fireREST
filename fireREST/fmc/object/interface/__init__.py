from fireREST.defaults import API_RELEASE_630
from fireREST.fmc import Resource


class Interface(Resource):
    """Retrieves list of all the interface objects both security zones and interface groups.

    **Tags:** Object

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllInterfaceObject` (GET (list))
    - `getInterfaceObject` (GET)

    **Query parameters:**

    - `filter` (string, optional): Query Param to return security zones and interface groups of specified InterfaceMode type based on the filter. The interface mode type passed should be common to both security zones and interface groups. Value is of format `interfaceMode:ROUTED or interfaceMode:PASSIVE or interfaceMode:INLINE or interfaceMode:SWITCHED`.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/object/interfaceobjects/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_630
