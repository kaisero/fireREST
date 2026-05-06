from fireREST import utils
from fireREST.defaults import API_RELEASE_660
from fireREST.fmc import Resource, Connection
from fireREST.fmc.object.timezone.override import Override


class Timezone(Resource):
    """Retrieves, deletes, creates and modifies the Time Zone Object.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllTimeZoneObject` (GET (list))
    - `getTimeZoneObject` (GET)
    - `createMultipleTimeZoneObject` (CREATE)
    - `updateTimeZoneObject` (UPDATE)
    - `deleteTimeZoneObject` (DELETE)

    **Query parameters:**

    - `overrideTargetId` (string, optional): Retrieves the override(s) associated with the object on given target ID.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean, optional): Enables bulk create for Time Zone objects.
    """
    PATH = '/object/timezoneobjects/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_660
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_660
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_660
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_660

    SUPPORTED_PARAMS = ['override_target_id']

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.override = Override(conn)

    @utils.support_params
    def get(self, uuid=None, name=None, override_target_id=None, params=None):
        return super().get(uuid=uuid, name=name, params=params)
