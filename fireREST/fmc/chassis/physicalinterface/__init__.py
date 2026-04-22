from fireREST.defaults import API_RELEASE_730
from fireREST.fmc import ChildResource


class PhysicalInterface(ChildResource):
    CONTAINER_NAME = 'Chassis'
    CONTAINER_PATH = '/chassis/fmcmanagedchassis/{uuid}'
    PATH = '/chassis/fmcmanagedchassis/{container_uuid}/physicalinterfaces/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_730
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_730
