from fireREST.defaults import API_RELEASE_760
from fireREST.fmc import Connection, Resource
from fireREST.fmc.object.macaddresspooloverride import MacAddressPoolOverride


class MacAddressPool(Resource):
    """Retrieves, creates, updates, or deletes MAC address pool objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllMacAddressPool` (GET (list))
    - `getMacAddressPool` (GET)
    - `createMacAddressPool` (CREATE)
    - `updateMacAddressPool` (UPDATE)
    - `deleteMacAddressPool` (DELETE)
    """

    PATH = '/object/macaddresspools/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_760

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.override = MacAddressPoolOverride(conn)
