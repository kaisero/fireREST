from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import ChildResource


class ChassisInterface(ChildResource):
    """Retrieve all chassis interfaces

    **Tags:** Chassis

    **Supported operations:** GET

    **Operation IDs:**

    - `getAllChassisAllInterfacesModel` (GET (list))
    - `getChassisAllInterfacesModel` (GET)

    **Query parameters:**

    - `filter` (string, optional): This is a query parameter to search interfaces by name or type or port type. Use `"name:{name}"` to search by hardware name of interface. Use `"type:{type1,type2}"` to search by interface type. Type can be `PhysicalInterface,SubInterface or EtherChannelInterface` Use `"portType:{portType1,portType2}"` to search by interface port type. Port type can be `DATA,MANAGEMENT,DATA_SHARING or CLUSTER`
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """

    CONTAINER_NAME = 'Chassis'
    CONTAINER_PATH = '/chassis/fmcmanagedchassis/{uuid}'
    PATH = '/chassis/fmcmanagedchassis/{container_uuid}/interfaces/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
