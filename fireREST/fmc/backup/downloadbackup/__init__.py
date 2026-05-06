from fireREST.defaults import API_RELEASE_730
from fireREST.fmc import Resource


class DownloadBackup(Resource):
    """Retrieves the backup associated with the specified UUID(In case of FMC manager identifier should be entered in place of UUID). If no filter is specified for a GET, retrieves the latest backup.

    **Tags:** Backup

    **Supported operations:** GET

    **Operation IDs:**

    - `getDownloadBackup` (GET)

    **Query parameters:**

    - `backupVersion` (string, optional): To be used in locating backup for device/container UUID `backupVersion`. **Filter parameter is optional and if not provided the latest backup will be fetched.
    """
    PATH = '/backup/downloadbackup/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_730
