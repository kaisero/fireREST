from fireREST.fmc import Resource, Connection
from fireREST.fmc.object.url.override import Override


class Url(Resource):
    PATH = '/object/urls/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '6.1.0'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '6.1.0'
    MINIMUM_VERSION_REQUIRED_DELETE = '6.1.0'

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.override = Override(conn)
