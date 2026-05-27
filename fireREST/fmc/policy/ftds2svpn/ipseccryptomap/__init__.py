from fireREST.defaults import API_RELEASE_720
from fireREST.fmc import ChildResource


class IpsecCryptoMap(ChildResource):
    CONTAINER_NAME = 'FtdS2sVpn'
    CONTAINER_PATH = '/policy/ftds2svpns/{uuid}'
    PATH = '/policy/ftds2svpns/{container_uuid}/ipseccryptomaps/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_720
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_720
