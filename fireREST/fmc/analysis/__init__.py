from fireREST.fmc import Connection
from fireREST.fmc.analysis.activesessions import ActiveSessions
from fireREST.fmc.analysis.filter import Filter
from fireREST.fmc.analysis.identifieduser import IdentifiedUser
from fireREST.fmc.analysis.useractivity import UserActivity


class Analysis:
    def __init__(self, conn: Connection):
        self.activesessions = ActiveSessions(conn)
        self.filter = Filter(conn)
        self.identifieduser = IdentifiedUser(conn)
        self.useractivity = UserActivity(conn)
