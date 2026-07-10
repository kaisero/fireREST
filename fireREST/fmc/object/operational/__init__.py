from fireREST.fmc import Connection
from fireREST.fmc.object.operational.findoverlaps import FindOverlaps
from fireREST.fmc.object.operational.realmstatus import RealmStatus
from fireREST.fmc.object.operational.testrealm import TestRealm
from fireREST.fmc.object.operational.usage import Usage


class Operational:
    def __init__(self, conn: Connection):
        self.findoverlaps = FindOverlaps(conn)
        self.realmstatus = RealmStatus(conn)
        self.testrealm = TestRealm(conn)
        self.usage = Usage(conn)
