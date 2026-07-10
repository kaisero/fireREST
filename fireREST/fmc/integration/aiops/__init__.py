from fireREST.fmc import Connection
from fireREST.fmc.integration.aiops.aiconfiguration import AiConfiguration
from fireREST.fmc.integration.aiops.tsdbupload import TsdbUpload
from fireREST.fmc.integration.aiops.tsdbuploadstatus import TsdbUploadStatus


class AiOps:
    def __init__(self, conn: Connection):
        self.aiconfiguration = AiConfiguration(conn)
        self.tsdbupload = TsdbUpload(conn)
        self.tsdbuploadstatus = TsdbUploadStatus(conn)
