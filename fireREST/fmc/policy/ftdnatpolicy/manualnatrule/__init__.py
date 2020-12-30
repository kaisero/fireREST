from typing import Dict, Union

from fireREST import utils
from fireREST.fmc import Connection, ChildResource


class ManualNatRule(ChildResource):
    CONTAINER_NAME = 'FtdNatPolicy'
    CONTAINER_PATH = '/policy/ftdnatpolicies/{uuid}'
    PATH = '/policy/ftdnatpolicies/{container_uuid}/manualnatrules/{uuid}'
    SUPPORTED_FILTERS = []
    SUPPORTED_PARAMS = ['section', 'target_index']
    IGNORE_FOR_CREATE = []
    IGNORE_FOR_UPDATE = []
    MINIMUM_VERSION_REQUIRED_CREATE = '6.2.3'
    MINIMUM_VERSION_REQUIRED_GET = '6.2.3'
    MINIMUM_VERSION_REQUIRED_UPDATE = '6.2.3'
    MINIMUM_VERSION_REQUIRED_DELETE = '6.2.3'

    @utils.support_params
    def create(
        self,
        data: Union[dict, list],
        container_uuid=None,
        container_name=None,
        section=None,
        target_index=None,
        params=None,
    ):
        return super().create(data=data, container_uuid=container_uuid, container_name=container_name, params=params)

    @utils.support_params
    def update(
        self, data: Dict, container_uuid=None, container_name=None, section=None, target_index=None, params=None,
    ):
        return super().update(data=data, container_uuid=container_uuid, container_name=container_name, params=params)
