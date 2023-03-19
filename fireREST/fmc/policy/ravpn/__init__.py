from fireREST.defaults import API_RELEASE_700, API_RELEASE_720
from fireREST.fmc import Connection, Resource
from fireREST.fmc.policy.ravpn.addressassignmentsettings import AddressAssignmentSettings
from fireREST.fmc.policy.ravpn.certificatemapsettings import CertificateMapSettings
from fireREST.fmc.policy.ravpn.connectionprofile import ConnectionProfile


class RaVpn(Resource):
    PATH = '/policy/ravpns/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_720

    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.addressassignmentsettings = AddressAssignmentSettings(conn)
        self.certificatemapsettings = CertificateMapSettings(conn)
        self.connectionprofile = ConnectionProfile(conn)
