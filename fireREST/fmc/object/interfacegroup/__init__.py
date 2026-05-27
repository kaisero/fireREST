from fireREST.defaults import API_RELEASE_630
from fireREST.fmc import Resource


class InterfaceGroup(Resource):
    """Retrieves, deletes, creates, or modifies the Interface group objects associated with the specified ID. If no ID is specified for a GET, retrieves list of all interface group objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllInterfaceGroupObject` (GET (list))
    - `getInterfaceGroupObject` (GET)
    - `createMultipleInterfaceGroupObject` (CREATE)
    - `updateInterfaceGroupObject` (UPDATE)
    - `deleteInterfaceGroupObject` (DELETE)

    **Query parameters:**

    - `groupByDevice` (string, optional): Set true to group interfaces by device and return as `devices` attribute, instead of `interfaces`.
    - `filter` (string, optional): Query Param to return interface groups of specified InterfaceModeIG type based on the filter. Value is of format `interfaceMode:ROUTED or interfaceMode:PASSIVE or interfaceMode:INLINE or interfaceMode:SWITCHED or interfaceMode:MANAGEMENT or interfaceMode:LOOPBACK`.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean, optional): Enables bulk create for interface group objects.
    """

    PATH = '/object/interfacegroups/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_630
