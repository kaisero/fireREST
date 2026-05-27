from fireREST import utils
from fireREST.defaults import API_RELEASE_660
from fireREST.fmc import ChildResource


class Command(ChildResource):
    """Retrieves the show command output from the device. Make sure the minimum device version required for using commands api is >= 6.6.0. This api supports multi threading. Only 1 request can be handled per device concurrently and across devices upto 10 devices are supported by commands api concurrently.

    **Tags:** Devices

    **Supported operations:** GET

    **Operation IDs:**

    - `getCommands` (GET (list))

    **Query parameters:**

    - `command` (string): The command filter query parameter should have value of show commands. The maximum word size of this field is 2. For eg: show failover, show snmp-server, show logging etc. <b>Note:- This API endpoint retrieves outputs from devices by executing specific CLIs which return small configurations. This endpoint should not be used to retrieve large configurations as this may not work as desired or impact performance. Specific CLI commands which should not be used include "show running-config all", "show running-config access-list", and similar commands which will provide large outputs.</b> `Supported CLIs:- `<i>show version, show version <?-option>, show failover, show failover <?-option>, show dhcpd state, show ip, show ip <?-option>, show aaa-server, show aaa-server <?-option>, show logging, show logging <?-someoptiononly>, show snmp-server <?-option>, show ssl, show ssl <?-option>, show firewall, show logging, show logging <?-someoptiononly>, show route, show route <?-option>, show vpn-sessiondb, show vpn-sessiondb <?-option>, show crypto <?-option>, show rule <?-option>, show access-list <?-option>, show network, show ntp, show banner, show snort3 status</i>
    - `parameters` (string, optional): The parameters filter query parameter should have values containing command values exceeding word size of 2 should be given as part of parameters field. For eg: history details, engineID, setting etc.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/operational/commands'

    @utils.resolve_by_name
    @utils.minimum_version_required(version=API_RELEASE_660)
    def get(self, command: str, container_uuid=None, container_name=None):
        # commands with wordsize > 2 must be split into filter and parameters params due to fmc rest api impl
        split_cmd = command.split(' ')
        filter_str = ' '.join(split_cmd[:2])
        params_str = ' '.join(split_cmd[2:])
        params = {'filter': utils.search_filter([{'command': filter_str}]), 'parameters': params_str}

        url = self.url(self.PATH.format(container_uuid=container_uuid))
        return self.conn.get(url=url, params=params)
