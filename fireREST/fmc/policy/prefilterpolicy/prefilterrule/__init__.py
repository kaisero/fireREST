from typing import Union

from fireREST import utils
from fireREST.defaults import API_RELEASE_650
from fireREST.fmc import ChildResource


class PrefilterRule(ChildResource):
    """Retrieves the prefilter rule associated with the specified policy ID and rule ID.

    **Tags:** Policy

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllPrefilterRule` (GET (list))
    - `getPrefilterRule` (GET)
    - `createMultiplePrefilterRule` (CREATE)
    - `updateMultiplePrefilterRule` (UPDATE (bulk))
    - `updatePrefilterRule` (UPDATE)
    - `deleteMultiplePrefilterRule` (DELETE (bulk))
    - `deletePrefilterRule` (DELETE)

    **Query parameters:**

    - `ruleType` (string, optional): If parameter is specified, only the policies with specified `ruleType` will be shown. Allowed values are PREFILTER and TUNNEL. Cannot be used if object ID is specified in path.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean): This parameter specifies that bulk operation is being used in the query. This parameter is required for bulk rule operations.
    - `insertAfter` (number, optional): This parameter specifies that the rules will be inserted after the specified rule index. insertBefore takes precedence over insertAfter - if both are specified, the insertBefore parameter will apply.
    - `insertBefore` (number, optional): This parameter specifies that the rules will be inserted before the specified rule index. insertBefore takes precedence over insertAfter - if both are specified, the insertBefore parameter will apply.
    - `filter` (string): To be used in conjunction with `bulk=true` for bulk deletion. Value is of format (including quotes): `"ids:id1,id2,..."`. `ids` is a comma-separated list of rule IDs to be deleted.
    """
    CONTAINER_NAME = 'PrefilterPolicy'
    CONTAINER_PATH = '/policy/prefilterpolicies/{uuid}'
    PATH = '/policy/prefilterpolicies/{container_uuid}/prefilterrules/{uuid}'
    SUPPORTED_PARAMS = ['category', 'section', 'insert_before', 'insert_after']
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
        category=None,
        section=None,
        insert_after=None,
        insert_before=None,
        params=None,
    ):
        return super().create(data=data, container_uuid=container_uuid, container_name=container_name, params=params)
