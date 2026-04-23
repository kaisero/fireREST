from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import ChildResource


class InterfaceSummary(ChildResource):
    CONTAINER_NAME = 'Chassis'
    CONTAINER_PATH = '/chassis/fmcmanagedchassis/{uuid}'
    PATH = '/chassis/fmcmanagedchassis/{container_uuid}/interfacesummary/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
