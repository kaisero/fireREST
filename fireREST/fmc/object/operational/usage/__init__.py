from fireREST import utils
from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import Resource


class Usage(Resource):
    """Find usage of specified object uuid and type across objects and policies. Supported object types:<ul><li>Network: NetworkAddress, Host, Network, Range, FQDN, NetworkGroup</li><li>Port: Port, ProtocolPortObject, PortObjectGroup, ICMPV4Object, ICMPV6Object, AnyProtocolPortObject</li><li>VLAN tag: VlanTag, VlanGroupTag</li><li>URL: Url, UrlGroup</li></ul>

    **Tags:** Object

    **Supported operations:** GET

    **Operation IDs:**

    - `getObjectUsage` (GET (list))

    **Query parameters:**

    - `filter` (string): Specify uuid `"uuid:object-uuid"` and `"type:object-type"` and type of object
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/object/operational/usage'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
    SUPPORTED_FILTERS = ['uuid', 'obj_type']

    @utils.support_params
    def get(self, uuid: str, obj_type: str, params=None):
        return super().get(params=params)
