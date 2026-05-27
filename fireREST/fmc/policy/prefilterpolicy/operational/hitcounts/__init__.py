from fireREST import utils
from fireREST.defaults import API_RELEASE_640
from fireREST.fmc import ChildResource


class Hitcount(ChildResource):
    """Retrieves Hit Count

    **Tags:** Policy

    **Supported operations:** GET, UPDATE, DELETE

    **Operation IDs:**

    - `getPrefilterHitCount` (GET (list))
    - `updatePrefilterHitCount` (UPDATE (bulk))
    - `updatePrefilterHitCount` (UPDATE)
    - `deletePrefilterHitCount` (DELETE (bulk))
    - `deletePrefilterHitCount` (DELETE)

    **Query parameters:**

    - `filter` (string): Value is of format (including quotes): `"deviceId:{uuid};ids:{uuid1,uuid2,..};fetchZeroHitCount:{true|false};name:{rule or policy name};lastHit:{number of days as per unit};lastHitUnit:{DAYS|WEEKS|MONTHS|YEARS}"` `deviceId` is UUID of device and is a mandatory field. `ids` returns hitcounts of access rules if set to list of rule UUIDs. If this key is not used, all access rules will be returned. `fetchZeroHitCount` returns only access rules whose hit count is zero if `true`. `name` returns only access rule name or policy name matches`name`. `lastHit` returns only access rules hit in last specified number of days as per `lastHitUnit` unit. `lastHitUnit` unit of number of last hit days - DAYS, WEEKS, MONTHS or YEARS. (Note that `fetchZeroHitCount`,`name`,`lastHit`,`lastHitUnit` filters are applicable only in GET operation and if `ids` filter is not used)
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'PrefilterPolicy'
    CONTAINER_PATH = '/policy/prefilterpolicies/{uuid}'
    PATH = '/policy/prefilterpolicies/{container_uuid}/operational/hitcounts/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_640
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_640
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_640

    @utils.support_params
    def update(self):
        return

    @utils.support_params
    def get(self):
        return

    @utils.support_params
    def delete(self):
        return
