from typing import Dict

from fireREST import utils
from fireREST.defaults import API_RELEASE_730
from fireREST.fmc import Connection, Resource
from fireREST.fmc.backup.downloadbackup import DownloadBackup
from fireREST.fmc.backup.file import BackupFile


class Backup(Resource):
    """Retrieves or deletes the backup associated with the specified UUID(In case of FMC manager identifier should be entered in place of UUID). If no filter is specified for a GET, DELETE retrieves the latest backup.

    **Tags:** Backup

    **Supported operations:** GET, DELETE

    **Operation IDs:**

    - `getAllBackupFile` (GET (list))
    - `getBackupFile` (GET)
    - `deleteBackupFile` (DELETE)

    **Query parameters:**

    - `backupVersion` (string, optional): To be used in locating backup for device/container UUID `backupVersion`. **Filter parameter is optional and if not provided the latest backup will be fetched.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/backup/files/{uuid}'

    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.downloadbackup = DownloadBackup(conn)
        self.file = BackupFile(conn)

    @utils.minimum_version_required(version=API_RELEASE_730)
    def create_device_backup(self, data: Dict, params=None):
        url = self.url('/backup/operational/devicebackup')
        return self.conn.post(url=url, data=data, params=params)
