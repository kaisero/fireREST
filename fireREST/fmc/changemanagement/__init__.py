from fireREST.fmc import Connection
from fireREST.fmc.changemanagement.ticket import Ticket


class ChangeManagement:
    def __init__(self, conn: Connection):
        self.ticket = Ticket(conn)
