from fireREST import utils
from fireREST.fmc import Resource, Connection
from fireREST.fmc.object.ipv6addresspool.override import Override


class Ipv6AddressPool(Resource):
    PATH = '/object/ipv6addresspools/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '7.0.0'

    SUPPORTED_PARAMS = ['override_target_id']

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.override = Override(conn)

    @utils.support_params
    def get(self, uuid=None, name=None, override_target_id=None, params=None):
        return super().get(uuid=uuid, name=name, params=params)
