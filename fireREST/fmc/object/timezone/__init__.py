from fireREST.fmc import Resource, Connection
from fireREST.fmc.object.fqdn.override import Override


class Timezone(Resource):
    PATH = '/object/timezoneobjects/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '6.6.0'
    MINIMUM_VERSION_REQUIRED_GET = '6.6.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '6.6.0'
    MINIMUM_VERSION_REQUIRED_DELETE = '6.6.0'

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.override = Override(conn)
