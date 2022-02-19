from fireREST.defaults import API_RELEASE_700
from fireREST.fmc import ChildResource


class AddressAssignmentSettings(ChildResource):
    CONTAINER_NAME = 'RaVpn'
    CONTAINER_PATH = '/policy/ravpns/{uuid}'
    PATH = '/policy/ravpns/{container_uuid}/addressassignmentsettings/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
