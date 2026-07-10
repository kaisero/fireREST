from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class ObjectSearch(Resource):
    """Search for objects matching specified text or IP address.

    **Tags:** Search

    **Supported operations:** GET

    **Operation IDs:**

    - `getGlobalObjectSearch` (GET (list))

    **Query parameters:**

    - `filter` (string): Text or IP address used for filtering To search for objects that contain groups, follow this format: `"text:searchText;types:Networks,Ports,etc;isAcpGlobalSearch:true;"` To perform multiple searches simultaneously, follow this format: `"text:searchText1,searchText2;types:Networks,Ports,etc;isAcpGlobalSearch:true;isMultiObjectSearch:true;"`
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/search/object'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
