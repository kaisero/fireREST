from fireREST import utils
from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import Resource, Connection
from fireREST.fmc.object.ssoserver.override import Override


class SsoServer(Resource):
    PATH = '/object/ssoservers/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700

    SUPPORTED_PARAMS = ['override_target_id']

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.override = Override(conn)

    @utils.support_params
    def get(self, uuid=None, name=None, override_target_id=None, params=None):
        return super().get(uuid=uuid, name=name, params=params)
