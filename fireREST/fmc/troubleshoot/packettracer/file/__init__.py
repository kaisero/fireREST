from fireREST.defaults import API_RELEASE_710
from fireREST.fmc import Resource


class File(Resource):
    """Retrieves the specified PCAP file from the Firewall Management Center.

    **Tags:** Troubleshoot

    **Supported operations:** GET, CREATE, DELETE

    **Operation IDs:**

    - `getAllPacketTracerPCAPFiles` (GET (list))
    - `getPacketTracerPCAPFiles` (GET)
    - `createPacketTracerPCAPFiles` (CREATE)
    - `deleteMultiplePacketTracerPCAPFiles` (DELETE (bulk))
    - `deletePacketTracerPCAPFiles` (DELETE)

    **Query parameters:**

    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean): Enables bulk delete for PCAP files.
    - `filter` (string): To be used in conjunction with `bulk=true` for bulk deletion. Various filter criteria can be specified using the format: `pcapFileNames:file1,file2,file3...` will delete only the PCAP files provided in the list. `deleteAllFiles:true` will delete all the PCAP files.
    """

    NAMESPACE = 'troubleshoot'
    PATH = '/packettracer/files/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_710
