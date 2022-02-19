from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import ChildResource


class CertificateMapSettings(ChildResource):
    CONTAINER_NAME = 'RaVpn'
    CONTAINER_PATH = '/policy/ravpns/{uuid}'
    PATH = '/policy/ravpns/{container_uuid}/certificatemapsettings/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
