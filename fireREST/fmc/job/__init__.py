from fireREST.fmc import Connection
from fireREST.fmc.job.taskstatus import TaskStatus


class Job:
    def __init__(self, conn: Connection):
        self.taskstatus = TaskStatus(conn)
