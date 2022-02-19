from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import Connection, Resource
from fireREST.fmc.policy.ravpn.addressassignmentsettings import AddressAssignmentSettings
from fireREST.fmc.policy.ravpn.certificatemapsettings import CertificateMapSettings
from fireREST.fmc.policy.ravpn.connectionprofile import ConnectionProfile


class RaVpn(Resource):
    PATH = '/policy/ravpns/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700

    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.addressassignmentsettings = AddressAssignmentSettings(conn)
        self.certificatemapsettings = CertificateMapSettings(conn)
        self.connectionprofile = ConnectionProfile(conn)
