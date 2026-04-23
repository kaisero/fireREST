from fireREST.fmc import Connection
from fireREST.fmc.audit.auditrecord import AuditRecord
from fireREST.fmc.audit.configchanges import ConfigChanges


class Audit:
    def __init__(self, conn: Connection):
        self.auditrecord = AuditRecord(conn)
        self.configchanges = ConfigChanges(conn)
