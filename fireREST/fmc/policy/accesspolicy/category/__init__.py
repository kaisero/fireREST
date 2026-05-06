from typing import Union

from fireREST import utils
from fireREST.defaults import API_RELEASE_650
from fireREST.fmc import ChildResource


class Category(ChildResource):
    """Retrieves the category associated with the specified policy ID.

    **Tags:** Policy

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllAccessPolicyCategory` (GET (list))
    - `getAccessPolicyCategory` (GET)
    - `createAccessPolicyCategory` (CREATE)
    - `updateAccessPolicyCategory` (UPDATE)
    - `deleteAccessPolicyCategory` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `section` (string, optional): Retrieves, creates or modifies category in given section. Allowed value is mandatory and default.
    - `aboveCategory` (string, optional): creates category above specified category.
    - `insertBefore` (string, optional): creates category above given rule index.
    - `insertAfter` (string, optional): creates category below given rule index.
    """
    CONTAINER_NAME = 'AccessPolicy'
    CONTAINER_PATH = '/policy/accesspolicies/{uuid}'
    PATH = '/policy/accesspolicies/{container_uuid}/categories/{uuid}'
    SUPPORTED_PARAMS = ['above_category', 'section', 'insert_before', 'insert_after']
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_650
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_650
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_650
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_650

    @utils.support_params
    def create(
        self,
        data: Union[dict, list],
        container_uuid=None,
        container_name=None,
        above_category=None,
        section=None,
        insert_after=None,
        insert_before=None,
        params=None,
    ):
        return super().create(data=data, container_uuid=container_uuid, container_name=container_name, params=params)
