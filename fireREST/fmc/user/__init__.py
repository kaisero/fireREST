from fireREST.fmc import Connection
from fireREST.fmc.user.authrole import AuthRole
from fireREST.fmc.user.duoconfig import DuoConfig
from fireREST.fmc.user.ssoconfig import SsoConfig


class User:
    def __init__(self, conn: Connection):
        self.authrole = AuthRole(conn)
        self.duoconfig = DuoConfig(conn)
        self.ssoconfig = SsoConfig(conn)
