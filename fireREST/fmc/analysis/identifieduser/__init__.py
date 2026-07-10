from fireREST import utils
from fireREST.defaults import API_RELEASE_760
from fireREST.fmc import Resource


class IdentifiedUser(Resource):
    """Retrieves or deletes all identified users.

    **Tags:** Analysis

    **Supported operations:** GET, DELETE

    **Operation IDs:**

    - `getAllIdentifiedUser` (GET (list))
    - `deleteIdentifiedUsers` (DELETE)

    **Query parameters:**

    - `sort`, `id`, `user`, `last_seen`, `realm_id`, `realm_name`, `username`, `first_name`, `last_name`,
      `email`, `department`, `phone`, `discovery_application`, `active_session_count`, `available_for_policy`
      (all optional): filter criteria supported by GET.
    - `bulk` (boolean, required for bulk DELETE), `delete_all` (boolean, optional), `user_ids` (string, optional):
      filter criteria supported by DELETE, in addition to the GET filters above.
    """

    PATH = '/analysis/identifiedusers'
    SUPPORTED_FILTERS = [
        'sort',
        'bulk',
        'delete_all',
        'user_ids',
        'id',
        'user',
        'last_seen',
        'realm_id',
        'realm_name',
        'username',
        'first_name',
        'last_name',
        'email',
        'department',
        'phone',
        'discovery_application',
        'active_session_count',
        'available_for_policy',
    ]
    MINIMUM_VERSION_REQUIRED_CREATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_UPDATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_760

    @utils.support_params
    def get(
        self,
        sort=None,
        id=None,
        user=None,
        last_seen=None,
        realm_id=None,
        realm_name=None,
        username=None,
        first_name=None,
        last_name=None,
        email=None,
        department=None,
        phone=None,
        discovery_application=None,
        active_session_count=None,
        available_for_policy=None,
        params=None,
    ):
        return super().get(params=params)

    @utils.minimum_version_required
    @utils.support_params
    def delete(
        self,
        bulk=None,
        delete_all=None,
        user_ids=None,
        id=None,
        user=None,
        last_seen=None,
        realm_id=None,
        realm_name=None,
        username=None,
        first_name=None,
        last_name=None,
        email=None,
        department=None,
        phone=None,
        discovery_application=None,
        active_session_count=None,
        available_for_policy=None,
        params=None,
    ):
        url = self.url(self.PATH)
        return self.conn.delete(url, params)
