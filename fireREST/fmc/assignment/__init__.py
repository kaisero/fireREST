from fireREST.fmc import Connection
from fireREST.fmc.assignment.policyassignment import PolicyAssignment


class Assignment:
    def __init__(self, conn: Connection):
        self.policyassignment = PolicyAssignment(conn)
