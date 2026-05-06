from fireREST import utils
from fireREST.defaults import API_RELEASE_623, API_RELEASE_720
from fireREST.fmc import ChildResource


class NatRule(ChildResource):
    """Retrieves the NAT rule (manual and auto) associated with the specified policy ID.

    **Tags:** Policy

    **Supported operations:** GET, DELETE

    **Operation IDs:**

    - `getAllFTDNatRule` (GET (list))
    - `getFTDNatRule` (GET)
    - `deleteMultipleFTDNatRule` (DELETE (bulk))
    - `deleteMultipleFTDNatRule` (DELETE)

    **Query parameters:**

    - `section` (string, optional): Retrieves NAT rule in given section. Allowed value is beforeauto, auto and afterauto.
    - `filter` (string, optional): Value is of format : `"ids:id1,id2,...;sourceInterface:name1,name2,...;destinationInterface:name1,name2,...; originalSource:name1/value1,name2/value2,...;originalDestination:name1/value1,name2/value2,...; translatedSource:name1/value1,name2/value2,...;translatedDestination:name1/value1,name2/value2,...; originalSourcePort:name1/value1,name2/value2,...;originalDestinationPort:name1/value1,name2/value2,...; translatedSourcePort:name1/value1,name2/value2,...;translatedDestinationPort:name1/value1,name2/value2,...;"` ids:id1,id2,...etc. This ids is a comma-separated list of rule ids to fetch/delete</br>sourceInterface:SecurityZone/Interface group name (seczonename1) can be given as value to fetch/delete NAT rule destinationInterface:SecurityZone/Interface group name (seczonename1) can be given as value to fetch/delete NAT rule originalSource: Network object configured as Original source object name (objectname) or the value (10.1.2.3) of the object can be given originalDestination:Network object configured as Destination source object name (objectname) or the value (10.1.2.3) of the object can be given translatedSource:Network object configured as translated source object name (objectname) or the value (10.1.2.3) of the object can be given translatedDestination:Network object configured as translated Destination object name (objectname) or the value (10.1.2.3) of the object can be given originalSourcePort:Port object configured as Original Source Port object name (http) or value of the object as port no or protocol (tcp/80) can be given originalDestinationPort:Port object configured as Original Destination Port object name (http) or value of the object as port no or protocol (tcp/80) can be given translatedSourcePort:Port object configured as Translated Source Port object name (http) or value of the object as port no or protocol (tcp/80) can be given translatedDestinationPort:Port object configured as Translated Destination Port object name (http) or value of the object as port no or protocol (tcp/80) can be given"
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean): Enables bulk actions for NAT rules.
    """
    CONTAINER_NAME = 'FtdNatPolicy'
    CONTAINER_PATH = '/policy/ftdnatpolicies/{uuid}'
    PATH = '/policy/ftdnatpolicies/{container_uuid}/natrules/{uuid}'
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_720
    SUPPORTED_FILTERS = [
        'section',
        'source_interface',
        'destination_interface',
        'original_source',
        'original_destination',
        'translated_source',
        'translated_destination',
        'original_source_port',
        'original_destination_port',
        'translated_source_port',
        'translated_destination_port',
    ]
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_623

    @utils.support_params
    def get(
        self,
        container_uuid=None,
        container_name=None,
        uuid=None,
        name=None,
        source_interface=None,
        destination_interface=None,
        original_source=None,
        original_destination=None,
        translated_source=None,
        translated_destination=None,
        original_source_port=None,
        original_destination_port=None,
        translated_source_port=None,
        translated_destination_port=None,
        params=None,
    ):
        return super().get(
            container_uuid=container_uuid, container_name=container_name, name=name, uuid=uuid, params=params
        )
