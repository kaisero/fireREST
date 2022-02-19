from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import ChildResource


class Override(ChildResource):
    CONTAINER_NAME = 'PortObjectGroup'
    CONTAINER_PATH = '/object/portobjectgroups/{uuid}'
    PATH = '/object/portobjectgroups/{container_uuid}/overrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
