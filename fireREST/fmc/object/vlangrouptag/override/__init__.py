from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import ChildResource


class Override(ChildResource):
    """Retrieves all(Domain and Device) overrides on a VlanGroupTag Object.Response will always be in expanded form. If passed, the "expanded" query parameter will be ignored.

    **Tags:** Object

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllVlanTagGroupOverride` (GET (list))
    - `getVlanTagGroupOverride` (GET)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    CONTAINER_NAME = 'VlanGroupTag'
    CONTAINER_PATH = '/object/vlangrouptags/{uuid}'
    PATH = '/object/vlangrouptags/{container_uuid}/overrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
