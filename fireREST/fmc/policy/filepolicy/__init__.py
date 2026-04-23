from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Connection, Resource
from fireREST.fmc.policy.filepolicy.filerule import FileRule


class FilePolicy(Resource):
    PATH = '/policy/filepolicies/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.filerule = FileRule(conn)
