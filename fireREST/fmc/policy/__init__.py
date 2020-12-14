from fireREST.fmc import Connection, Resource
from fireREST.fmc.policy.accesspolicy import AccessPolicy


class Policy(Resource):
    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.accesspolicy = AccessPolicy(conn)
