from fireREST.defaults import API_RELEASE_730
from fireREST.fmc import Connection, Resource
from fireREST.fmc.integration.umbrella.tunneldeployment.transcript import Transcript


class TunnelDeployment(Resource):
    PATH = '/integration/umbrella/tunneldeployments/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_730
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_730

    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.transcript = Transcript(conn)
