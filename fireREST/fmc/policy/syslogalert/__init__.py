from fireREST.defaults import API_CONFIG_NAME
from fireREST.fmc import Connection, Resource


class SyslogAlert(Resource):
    PATH = '/policy/syslogalerts/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
