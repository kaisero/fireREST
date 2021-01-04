from typing import Union

from fireREST import utils
from fireREST.fmc import ChildResource


class Hitcount(ChildResource):
    CONTAINER_NAME = 'PrefilterPolicy'
    CONTAINER_PATH = '/policy/prefilterpolicies/{uuid}'
    PATH = '/policy/prefilterpolicies/{container_uuid}/operational/hitcounts/{uuid}'
    SUPPORTED_FILTERS = []
    SUPPORTED_PARAMS = []
    MINIMUM_VERSION_REQUIRED_GET = '6.4.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '6.4.0'
    MINIMUM_VERSION_REQUIRED_DELETE = '6.4.0'

    @utils.support_params
    def update(self):
        return

    @utils.support_params
    def get(self):
        return

    @utils.support_params
    def delete(self):
        return
