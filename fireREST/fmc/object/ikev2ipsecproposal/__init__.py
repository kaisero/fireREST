from fireREST.defaults import API_RELEASE_630
from fireREST.fmc import Resource


class Ikev2IpsecProposal(Resource):
    """Retrieves, deletes, creates, or modifies the IKEv2 IPSec Proposal associated with the specified ID. If no ID is specified for a GET, retrieves list of all IKEv2 IPSec Proposal objects.

    **Tags:** Object

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllIKEv2IPsecProposal` (GET (list))
    - `getIKEv2IPsecProposal` (GET)
    - `createIKEv2IPsecProposal` (CREATE)
    - `updateIKEv2IPsecProposal` (UPDATE)
    - `deleteIKEv2IPsecProposal` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    """
    PATH = '/object/ikev2ipsecproposals/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_630
