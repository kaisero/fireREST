from typing import Dict, Optional

from fireREST import utils
from fireREST.defaults import API_RELEASE_710
from fireREST.fmc import ChildResource


class Operational(ChildResource):
    CONTAINER_NAME = 'Chassis'
    CONTAINER_PATH = '/chassis/fmcmanagedchassis/{uuid}'
    PATH = '/chassis/fmcmanagedchassis/{container_uuid}/operational/{uuid}'

    @utils.minimum_version_required(version=API_RELEASE_710)
    @utils.resolve_by_name
    def breakout_interfaces(
        self,
        data: Dict,
        container_uuid: Optional[str] = None,
        container_name: Optional[str] = None,
        params: Optional[Dict] = None,
    ):
        url = self.url(f'{self.PATH.format(container_uuid=container_uuid)}/breakoutinterfaces')
        return self.conn.post(url=url, data=data, params=params)

    @utils.minimum_version_required(version=API_RELEASE_710)
    @utils.resolve_by_name
    def join_interfaces(
        self,
        data: Dict,
        container_uuid: Optional[str] = None,
        container_name: Optional[str] = None,
        params: Optional[Dict] = None,
    ):
        url = self.url(f'{self.PATH.format(container_uuid=container_uuid)}/joininterfaces')
        return self.conn.post(url=url, data=data, params=params)

    @utils.minimum_version_required(version=API_RELEASE_710)
    @utils.resolve_by_name
    def sync_networkmodule(
        self,
        data: Dict,
        container_uuid: Optional[str] = None,
        container_name: Optional[str] = None,
        params: Optional[Dict] = None,
    ):
        url = self.url(f'{self.PATH.format(container_uuid=container_uuid)}/syncnetworkmodule')
        return self.conn.put(url=url, data=data, params=params)
