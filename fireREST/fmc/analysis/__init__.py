from fireREST.fmc import Connection
from fireREST.fmc.analysis.activesessions import ActiveSessions
from fireREST.fmc.analysis.useractivity import UserActivity


class Analysis:
    def __init__(self, conn: Connection):
        self.activesessions = ActiveSessions(conn)
        self.useractivity = UserActivity(conn)
