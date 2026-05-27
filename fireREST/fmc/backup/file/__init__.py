from fireREST.defaults import API_RELEASE_730
from fireREST.fmc import Resource


class BackupFile(Resource):
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
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_730
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_730
