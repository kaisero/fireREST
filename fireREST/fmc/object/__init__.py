from fireREST.fmc import Connection, Resource
from fireREST.fmc.object.network import Network


class Object(Resource):
    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.network = Network(conn)
