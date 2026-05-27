from typing import Dict, Union

from fireREST import utils
from fireREST.defaults import API_RELEASE_623
from fireREST.fmc import ChildResource


class ManualNatRule(ChildResource):
    """Retrieves the Manual NAT rule associated with the specified ID.

    **Tags:** Policy

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllFTDManualNatRule` (GET (list))
    - `getFTDManualNatRule` (GET)
    - `createMultipleFTDManualNatRule` (CREATE)
    - `updateMultipleFTDManualNatRule` (UPDATE (bulk))
    - `updateFTDManualNatRule` (UPDATE)
    - `deleteMultipleFTDManualNatRule` (DELETE (bulk))
    - `deleteFTDManualNatRule` (DELETE)

    **Query parameters:**

    - `section` (string, optional): Retrieves manual NAT rule in given section. Allowed value is beforeauto and afterauto.
    - `partialUpdate` (boolean, optional): This field specifies whether to change the entire object or only certain attributes of it. When its value is false the whole object will change, and if the value is true then only the attributes that are specified will change. The default value of this field is false.
    - `targetIndex` (string, optional): Modifies manual NAT rule at given targetIndex. It takes an integer value.
    - `filter` (string, optional): Value is of format : `"ids:id1,id2,...;sourceInterface:name1,name2,...;destinationInterface:name1,name2,...; originalSource:name1/value1,name2/value2,...;originalDestination:name1/value1,name2/value2,...; translatedSource:name1/value1,name2/value2,...;translatedDestination:name1/value1,name2/value2,...; originalSourcePort:name1/value1,name2/value2,...;originalDestinationPort:name1/value1,name2/value2,...; translatedSourcePort:name1/value1,name2/value2,...;translatedDestinationPort:name1/value1,name2/value2,...;"` ids:id1,id2,...etc. This ids is a comma-separated list of rule ids to fetch/delete</br>sourceInterface:SecurityZone/Interface group name (seczonename1) can be given as value to fetch/delete NAT rule destinationInterface:SecurityZone/Interface group name (seczonename1) can be given as value to fetch/delete NAT rule originalSource: Network object configured as Original source object name (objectname) or the value (10.1.2.3) of the object can be given originalDestination:Network object configured as Destination source object name (objectname) or the value (10.1.2.3) of the object can be given translatedSource:Network object configured as translated source object name (objectname) or the value (10.1.2.3) of the object can be given translatedDestination:Network object configured as translated Destination object name (objectname) or the value (10.1.2.3) of the object can be given originalSourcePort:Port object configured as Original Source Port object name (http) or value of the object as port no or protocol (tcp/80) can be given originalDestinationPort:Port object configured as Original Destination Port object name (http) or value of the object as port no or protocol (tcp/80) can be given translatedSourcePort:Port object configured as Translated Source Port object name (http) or value of the object as port no or protocol (tcp/80) can be given translatedDestinationPort:Port object configured as Translated Destination Port object name (http) or value of the object as port no or protocol (tcp/80) can be given"
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean, optional): Enables bulk actions for Manual NAT rules.
    """

    CONTAINER_NAME = 'FtdNatPolicy'
    CONTAINER_PATH = '/policy/ftdnatpolicies/{uuid}'
    PATH = '/policy/ftdnatpolicies/{container_uuid}/manualnatrules/{uuid}'
    SUPPORTED_PARAMS = ['section', 'target_index']
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_623
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_623
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_623
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_623

    @utils.support_params
    def create(
        self,
        data: Union[dict, list],
        container_uuid=None,
        container_name=None,
        section=None,
        target_index=None,
        params=None,
    ):
        return super().create(data=data, container_uuid=container_uuid, container_name=container_name, params=params)

    @utils.support_params
    def update(
        self,
        data: Dict,
        container_uuid=None,
        container_name=None,
        section=None,
        target_index=None,
        params=None,
    ):
        return super().update(data=data, container_uuid=container_uuid, container_name=container_name, params=params)
