from typing import Dict, Union

from fireREST import utils
from fireREST.defaults import API_RELEASE_623
from fireREST.fmc import ChildResource


class AutoNatRule(ChildResource):
    CONTAINER_NAME = 'FtdNatPolicy'
    CONTAINER_PATH = '/policy/ftdnatpolicies/{uuid}'
    PATH = '/policy/ftdnatpolicies/{container_uuid}/autonatrules/{uuid}'
    SUPPORTED_PARAMS = ['section']
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_623
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_623
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_623
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_623

    @utils.support_params
    def create(
        self,
        data: Union[dict, list],
        container_uuid=None,
        container_name=None,
        section=None,
        params=None,
    ):
        return super().create(data=data, container_uuid=container_uuid, container_name=container_name, params=params)

    @utils.support_params
    def update(
        self,
        data: Dict,
        container_uuid=None,
        container_name=None,
        section=None,
        params=None,
    ):
        return super().update(data=data, container_uuid=container_uuid, container_name=container_name, params=params)
