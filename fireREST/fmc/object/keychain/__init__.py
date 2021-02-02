from fireREST.fmc import Resource, Connection
from fireREST.fmc.object.keychain.override import Override


class KeyChain(Resource):
    PATH = '/object/keychains/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '6.4.0'
    MINIMUM_VERSION_REQUIRED_GET = '6.4.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '6.4.0'
    MINIMUM_VERSION_REQUIRED_DELETE = '6.4.0'

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.override = Override(conn)
