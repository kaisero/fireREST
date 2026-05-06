from typing import Union

from fireREST import utils
from fireREST.defaults import API_RELEASE_610, API_RELEASE_621
from fireREST.fmc import ChildResource


class AccessRule(ChildResource):
    """Retrieves the access control rule associated with the specified policy ID and rule ID.

    **Tags:** Policy

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllAccessRule` (GET (list))
    - `getAccessRule` (GET)
    - `createMultipleAccessRule` (CREATE)
    - `updateMultipleAccessRule` (UPDATE (bulk))
    - `updateAccessRule` (UPDATE)
    - `deleteMultipleAccessRule` (DELETE (bulk))
    - `deleteAccessRule` (DELETE)

    **Query parameters:**

    - `partialUpdate` (boolean, optional): This field specifies whether to change the entire object or only certain attributes of it. When its value is false the whole object will change, and if the value is true then only the attributes that are specified will change. The default value of this field is false.
    - `filter` (string, optional): For GetAll Filter criteria can be specified using the format `"name:filterName;timeRange:true;action:filterAction;sourceNetworks:filterValue1,filterValue2...."`. Supported filter criteria are "name","timeRange","action","sourceNetworks","originalClientIP","destinationNetworks","sourcePorts","destinationPorts","sourceZones","destinationZones","applications","sourceDynamicObjects","destinationDynamicObjects","vlanTags","comments","users","urls","intrusionPolicy","sourceSecurityGroupTags","fts".
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean): This parameter specifies that bulk put operation is being used in the query. This parameter is required for bulk edit rule operations.
    - `insertAfter` (number, optional): This parameter specifies that the rules will be inserted after the specified rule index. If no section or category is specified, the rules will be added to the section or category after the insertion point. insertBefore takes precedence over insertAfter - if both are specified, the insertBefore parameter will apply.
    - `insertBefore` (number, optional): This parameter specifies that the rules will be inserted before the specified rule index. If no section or category is specified, the rules will be added to the section or category before the insertion point. insertBefore takes precedence over insertAfter - if both are specified, the insertBefore parameter will apply.
    - `section` (string, optional): This parameter specifies the section into which the rules will be added. If this parameter is not used the section will be the default section. Only mandatory and default are allowed values. If a section is specified, a category cannot be specified.
    - `category` (string, optional): This parameter specifies the category into which the rules will be added. If a category is specified it must exist or the request will fail. If a section is specified, a category cannot be specified.
    """
    CONTAINER_NAME = 'AccessPolicy'
    CONTAINER_PATH = '/policy/accesspolicies/{uuid}'
    PATH = '/policy/accesspolicies/{container_uuid}/accessrules/{uuid}'
    SUPPORTED_PARAMS = ['category', 'section', 'insert_before', 'insert_after']
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_621
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_610

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
