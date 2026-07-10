from fireREST.fmc import Connection
from fireREST.fmc.user.externalauth.applyexternalauth import ApplyExternalAuth
from fireREST.fmc.user.externalauth.authconfigobject import AuthConfigObject
from fireREST.fmc.user.externalauth.externalauth import ExternalAuth
from fireREST.fmc.user.externalauth.fetchldapattributes import FetchLdapAttributes
from fireREST.fmc.user.externalauth.fetchldapdns import FetchLdapDns
from fireREST.fmc.user.externalauth.ldapconfigobject import LdapConfigObject
from fireREST.fmc.user.externalauth.radiusconfigobject import RadiusConfigObject


class ExternalAuthNamespace:
    def __init__(self, conn: Connection):
        self.applyexternalauth = ApplyExternalAuth(conn)
        self.authconfigobject = AuthConfigObject(conn)
        self.externalauth = ExternalAuth(conn)
        self.fetchldapattributes = FetchLdapAttributes(conn)
        self.fetchldapdns = FetchLdapDns(conn)
        self.ldapconfigobject = LdapConfigObject(conn)
        self.radiusconfigobject = RadiusConfigObject(conn)
