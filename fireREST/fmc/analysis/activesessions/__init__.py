from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class ActiveSessions(Resource):
    """Retrieves active sessions.

    **Tags:** Analysis

    **Supported operations:** GET, DELETE

    **Operation IDs:**

    - `getAllActiveSession` (GET (list))
    - `deleteMultipleActiveSession` (DELETE (bulk))
    - `deleteMultipleActiveSession` (DELETE)

    **Query parameters:**

    - `userId` (number, optional): Search based on user ID.Operator: `EQUALS`.
    - `loginTime` (string, optional): Search based on the session login time, format: `{before|after}:{loginTime}` or `after:{loginTime},before:{loginTime}`, where loginTime takes Long value (Unix Timestamp).
    - `lastSeen` (string, optional): Search based on the time when the user was last seen. Format and values as for loginTime.
    - `username` (string, optional): Search based on user username. Operator: `CONTAINS` (i.e. search for ana will return users with usernames ana, banana, canada if they have active sessions)
    - `email` (string, optional): Search based on user email. Operator: `CONTAINS`.
    - `department` (string, optional): Search based on user department. Operator: `EQUALS`.
    - `authenticationType` (string, optional): Search based on authentication type (passive, active). Operator: `EQUALS`.
    - `device` (string, optional): Search based on device. Operator: `EQUALS`.
    - `currentIP` (string, optional): Search based on IP of the session. Operator: `EQUALS`.
    - `user` (string, optional): Search based on user common name in AD. Operator: `EQUALS`.
    - `realmId` (number, optional): Search based on realm ID. Operator: `EQUALS`.
    - `realmName` (string, optional): Search based on realm name. Operator: `EQUALS`.
    - `firstName` (string, optional): Search based on user first name. Operator: `CONTAINS`.
    - `lastName` (string, optional): Search based on user last name. Operator: `CONTAINS`.
    - `phone` (string, optional): Search based on user phone. Operator: `EQUALS`.
    - `discoveryApplication` (string, optional): Search based on realm type (LDAP, Microsoft Azure). Operator: `EQUALS`.
    - `sort` (string, optional): Sort by specific field (ORDER BY), format:`{fieldName}:{asc|desc}`
    - `offset` (integer, optional): Index of first item to return.
    - `limit` (integer, optional): Number of items to return.
    - `expanded` (boolean, optional): Include extended sub-object details in response.
    - `bulk` (boolean, optional): should always be set to true
    """

    PATH = '/analysis/activesessions/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_740
