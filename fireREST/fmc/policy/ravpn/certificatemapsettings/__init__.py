from fireREST.fmc import ChildResource


class CertificateMapSettings(ChildResource):
    CONTAINER_NAME = 'RaVpn'
    CONTAINER_PATH = '/policy/ravpns/{uuid}'
    PATH = '/policy/ravpns/{container_uuid}/certificatemapsettings/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '7.0.0'
