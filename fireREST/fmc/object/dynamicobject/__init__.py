from fireREST import utils
from fireREST.fmc import Resource, Connection
from fireREST.fmc.object.dynamicobject.mapping import Mapping


class DynamicObject(Resource):
    PATH = '/object/dynamicobjects/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '7.0.0'
    MINIMUM_VERSION_REQUIRED_GET = '7.0.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '7.0.0'
    MINIMUM_VERSION_REQUIRED_DELETE = '7.0.0'

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.mapping = Mapping(conn)
