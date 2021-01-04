from fireREST.fmc import Connection
from fireREST.fmc.intelligence.tid.element import Element
from fireREST.fmc.intelligence.tid.incident import Incident
from fireREST.fmc.intelligence.tid.indicator import Indicator
from fireREST.fmc.intelligence.tid.observable import Observable
from fireREST.fmc.intelligence.tid.setting import Setting
from fireREST.fmc.intelligence.tid.source import Source


class Tid:
    def __init__(self, conn: Connection):
        self.element = Element(conn)
        self.incident = Incident(conn)
        self.indicator = Indicator(conn)
        self.observable = Observable(conn)
        self.setting = Setting(conn)
        self.source = Source(conn)
