from fireREST import utils
from fireREST.fmc import Resource, Connection
from fireREST.fmc.object.timezone.override import Override


class Timezone(Resource):
    PATH = '/object/timezoneobjects/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '6.6.0'
    MINIMUM_VERSION_REQUIRED_GET = '6.6.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '6.6.0'
    MINIMUM_VERSION_REQUIRED_DELETE = '6.6.0'

    SUPPORTED_PARAMS = ['override_target_id']

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.override = Override(conn)

    @utils.support_params
    def get(self, uuid=None, name=None, override_target_id=None, params=None):
        return super().get(uuid=uuid, name=name, params=params)
