from fireREST.fmc import Connection
from fireREST.fmc.intelligence.taxiiconfig import TaxiiConfig
from fireREST.fmc.intelligence.tid import Tid


class Intelligence:
    def __init__(self, conn: Connection):
        self.taxiiconfig = TaxiiConfig(conn)
        self.tid = Tid(conn)
