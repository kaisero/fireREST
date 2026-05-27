from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import ChildResource


class Mapping(ChildResource):
    """Retrieves, adds, or removes the Dynamic Object Mappings associated with the specified ID.

    **Tags:** Object

    **Supported operations:** GET, UPDATE

    **Operation IDs:**

    - `getDynamicObjectMappings` (GET (list))
    - `updateDynamicObjectMappings` (UPDATE (bulk))
    - `updateDynamicObjectMappings` (UPDATE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `action` (string, optional): Specify action for dynamic object mappings. It can be one of ["add", "remove", "remove_all"]. Default value is "add".
    - `propagate` (string, optional): Control propagating dynamic object mappings. It can be ["true", "false"]. Default value is "true".
    """

    CONTAINER_NAME = 'DynamicObject'
    CONTAINER_PATH = '/object/dynamicobjects/{uuid}'
    PATH = '/object/dynamicobjects/{container_uuid}/mappings'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_700
