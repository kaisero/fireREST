from fireREST.defaults import API_RELEASE_660
from fireREST.fmc import ChildResource


class Override(ChildResource):
    """Retrieves all (Domain and Device) overrides on a TimeZoneObject. Response will always be in expanded form. If passed, the "expanded" query parameter will be ignored.

    **Tags:** Object

    **Supported operations:** GET

    **Operation IDs:**

    - `getTimeZoneObjectOverride` (GET (list))

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    CONTAINER_NAME = 'Timezone'
    CONTAINER_PATH = '/object/timezoneobjects/{uuid}'
    PATH = '/object/timezoneobjects/{container_uuid}/overrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_660
