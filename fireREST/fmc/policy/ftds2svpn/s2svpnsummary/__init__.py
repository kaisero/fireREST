from fireREST.defaults import API_RELEASE_720
from fireREST.fmc import ChildResource


class S2sVpnSummary(ChildResource):
    CONTAINER_NAME = 'FtdS2sVpn'
    CONTAINER_PATH = '/policy/ftds2svpns/{uuid}'
    PATH = '/policy/ftds2svpns/{container_uuid}/summaries/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_720
