from fireREST.defaults import API_RELEASE_710
from fireREST.fmc import ChildResource


class NetworkModule(ChildResource):
    CONTAINER_NAME = 'Chassis'
    CONTAINER_PATH = '/chassis/fmcmanagedchassis/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_710
    PATH = '/chassis/fmcmanagedchassis/{container_uuid}/networkmodules/{uuid}'
