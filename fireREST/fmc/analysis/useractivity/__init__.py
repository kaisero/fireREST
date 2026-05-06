from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class UserActivity(Resource):
    """Retrieves user activities.

    **Tags:** Analysis

    **Supported operations:** GET, DELETE

    **Operation IDs:**

    - `getAllUserActivity` (GET (list))
    - `deleteMultipleUserActivity` (DELETE (bulk))
    - `deleteMultipleUserActivity` (DELETE)

    **Query parameters:**

    - `sort` (string, optional): Sort by specific field (ORDER BY), format:`{fieldName}:{asc|desc}`.
    - `eventId` (string, optional): Search based on event ID. Operator: `EQUALS`.
    - `time` (string, optional): Search based on the time, format: `{before|after}:{time}` or `after:{time},before:{time}`, where time takes Long value (Unix Timestamp).
    - `event` (string, optional): Search based on event. Operator: `CONTAINS`.
    - `username` (string, optional): Search based on username. Operator: `CONTAINS` (i.e. search for ana will return users with usernames ana, banana, canada).
    - `realmName` (string, optional): Search based on realm. Operator: `EQUALS`.
    - `discoveryApplication` (string, optional): Search based on realm type (LDAP, Microsoft Azure). Operator: `EQUALS`.
    - `authenticationType` (string, optional): Search based on authentication type. Operator: `EQUALS`.
    - `ipAddress` (string, optional): Search based on IP address. Operator: `EQUALS`.
    - `startPort` (string, optional): Search based on start port. Operator: `EQUALS`.
    - `endPort` (string, optional): Search based on end port. Operator: `EQUALS`.
    - `description` (string, optional): Search based on description. Operator: `CONTAINS`
    - `vpnSessionType` (string, optional): Search based on vpn session type. Operator: `EQUALS`.
    - `vpnGroupPolicy` (string, optional): Search based on vpn group policy. Operator: `EQUALS`.
    - `vpnConnectionProfile` (string, optional): Search based on vpn connection profile. Operator: `EQUALS`.
    - `vpnClientPublicIP` (string, optional): Search based on vpn client public IP. Operator: `EQUALS`.
    - `vpnClientCountry` (string, optional): Search based on vpn client country. Operator: `EQUALS`.
    - `vpnClientOS` (string, optional): Search based on vpn client OS. Operator: `EQUALS`.
    - `vpnClientApplication` (string, optional): Search based on vpn client application. Operator: `EQUALS`.
    - `vpnConnectionDuration` (string, optional): Search based on vpn connection duration. Operator: `EQUALS`.
    - `vpnBytesOut` (string, optional): Search based on vpn bytes transmitted. Operator: `EQUALS`.
    - `vpnBytesIn` (string, optional): Search based on vpn received. Operator: `EQUALS`.
    - `securityGroupTag` (string, optional): Search based on security group tag. Operator: `EQUALS`.
    - `endpointProfile` (string, optional): Search based on endpoint profile. Operator: `EQUALS`.
    - `endpointLocation` (string, optional): Search based on endpoint location. Operator: `EQUALS`.
    - `device` (string, optional): Search based on device. Operator: `EQUALS`.
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean): Required parameter, should be always set to `true`
    - `deleteAll` (boolean, optional): Delete all user activities. When set to `true` event query parameters should be absent.
    - `azureEvents` (string, optional): Delete Azure user activities (events), format: `id1,id2,...`
    - `ldapEvents` (string, optional): Delete LDAP user activities (events), format: `id1,id2,...`
    """
    PATH = '/analysis/useractivity/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_740
