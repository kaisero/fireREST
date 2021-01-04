from fireREST.fmc import Connection
from fireREST.fmc.audit.auditrecord import AuditRecord


class Audit:
    def __init__(self, conn: Connection):
        self.auditrecord = AuditRecord(conn)
