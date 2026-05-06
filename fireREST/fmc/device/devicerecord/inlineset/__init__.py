from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import ChildResource


class InlineSet(ChildResource):
    """Retrieves, deletes, creates, or modifies the inline set associated with the specified NGIPS device ID and inline set ID. If no inline set ID is specified, retrieves list of all inline sets associated with the specified NGIPS device ID.

    **Tags:** Devices

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllInlineSet` (GET (list))
    - `getInlineSet` (GET)
    - `createInlineSet` (CREATE)
    - `updateInlineSet` (UPDATE)
    - `deleteInlineSet` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/inlinesets/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_610
