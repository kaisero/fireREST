from typing import Dict

from fireREST import utils
from fireREST.defaults import API_RELEASE_730
from fireREST.fmc import Resource


class FlexConfigPolicy(Resource):
    """Retrieves the FlexConfig Policy with the associated ID.

    **Tags:** Policy

    **Supported operations:** GET, CREATE

    **Operation IDs:**

    - `getAllFlexConfig` (GET (list))
    - `getFlexConfig` (GET)
    - `createFlexConfig` (CREATE)

    **Query parameters:**

    - `filter` (string, optional): Filter criteria can be specified using the format `name:policyname` `policyname` -- Name of the FlexConfig Policy to be queried.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/policy/flexconfigpolicies/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_730
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_730

    @utils.minimum_version_required(version=API_RELEASE_730)
    def migrate(self, data: Dict, uuid: str, params=None):
        url = self.url(f'/policy/flexconfigpolicies/{uuid}/migrate')
        return self.conn.post(url=url, data=data, params=params)
