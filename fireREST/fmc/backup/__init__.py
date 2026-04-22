from typing import Dict

from fireREST import utils
from fireREST.defaults import API_RELEASE_730
from fireREST.fmc import Connection, Resource
from fireREST.fmc.backup.downloadbackup import DownloadBackup
from fireREST.fmc.backup.file import BackupFile


class Backup(Resource):
    PATH = '/backup/files/{uuid}'

    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.downloadbackup = DownloadBackup(conn)
        self.file = BackupFile(conn)

    @utils.minimum_version_required(version=API_RELEASE_730)
    def create_device_backup(self, data: Dict, params=None):
        url = self.url('/backup/operational/devicebackup')
        return self.conn.post(url=url, data=data, params=params)
