from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class ConfigChanges(Resource):
    NAMESPACE = 'platform_domain'
    PATH = '/audit/configchanges/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
