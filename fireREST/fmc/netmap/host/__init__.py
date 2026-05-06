from typing import Dict, List, Optional, Union

from fireREST import utils
from fireREST.defaults import API_RELEASE_710
from fireREST.fmc import Resource


class Host(Resource):
    """Retrieves the host associated with the specified ID in the Network Map.

    **Tags:** Network Map

    **Supported operations:** GET, CREATE, DELETE

    **Operation IDs:**

    - `getAllNetmapHost` (GET (list))
    - `getNetmapHost` (GET)
    - `createMultipleNetmapHost` (CREATE)
    - `deleteMultipleNetmapHost` (DELETE (bulk))
    - `deleteNetmapHost` (DELETE)

    **Query parameters:**

    - `filter` (string, optional): Filters for retrieve and delete operations. Values can be: `ipAddress:{192.168.1.2|'::ffff:c0a8:0102'}`.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean, optional): Enables bulk create or delete. This field must be true in order to delete with a filter rather than an identifier.
    """
    NAMESPACE = 'netmap'
    PATH = '/hosts/{uuid}'
    SUPPORTED_FILTERS = ['ip_address']
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_710

    @utils.support_params
    def get(self, uuid: Optional[str] = None, ip_address: Optional[str] = None, params: Optional[Dict] = None):
        return super().get(uuid=uuid, params=params)

    @utils.support_params
    def delete(
        self,
        uuid: Optional[str] = None,
        ip_address: Optional[Union[str, List]] = None,
        params: Optional[Dict] = None,
    ):
        if ip_address:
            if params is None:
                params = {}
            params['bulk'] = True
        url = self.url(self.PATH.format(uuid=uuid))
        return self.conn.delete(url, params)
