from typing import Dict, Optional

from fireREST import utils
from fireREST.defaults import API_RELEASE_710, API_RELEASE_720
from fireREST.fmc import ChildResource


class Operational(ChildResource):
    CONTAINER_NAME = 'Chassis'
    CONTAINER_PATH = '/chassis/fmcmanagedchassis/{uuid}'
    PATH = '/chassis/fmcmanagedchassis/{container_uuid}/operational/{uuid}'

    @utils.minimum_version_required(version=API_RELEASE_710)
    @utils.resolve_by_name
    def breakout_interfaces(self,
                            data: Dict,
                            container_uuid: Optional[str] = None,
                            container_name: Optional[str] = None,
                            params: Optional[Dict] = None):
        base = self.PATH.format(container_uuid=container_uuid, uuid='').rstrip('/')
        url = self.url(f'{base}/breakoutinterfaces')
        return self.conn.post(url=url, data=data, params=params)

    @utils.minimum_version_required(version=API_RELEASE_720)
    @utils.resolve_by_name
    def evaluate_operation(self,
                           container_uuid: Optional[str] = None,
                           container_name: Optional[str] = None,
                           params: Optional[Dict] = None):
        base = self.PATH.format(container_uuid=container_uuid, uuid='').rstrip('/')
        url = self.url(f'{base}/evaluateoperation')
        return self.conn.get(url=url, params=params)

    @utils.minimum_version_required(version=API_RELEASE_710)
    @utils.resolve_by_name
    def join_interfaces(self,
                        data: Dict,
                        container_uuid: Optional[str] = None,
                        container_name: Optional[str] = None,
                        params: Optional[Dict] = None):
        base = self.PATH.format(container_uuid=container_uuid, uuid='').rstrip('/')
        url = self.url(f'{base}/joininterfaces')
        return self.conn.post(url=url, data=data, params=params)

    @utils.minimum_version_required(version=API_RELEASE_710)
    @utils.resolve_by_name
    def sync_networkmodule(self, data: Dict,
                           container_uuid: Optional[str] = None,
                           container_name: Optional[str] = None,
                           params: Optional[Dict] = None):
        base = self.PATH.format(container_uuid=container_uuid, uuid='').rstrip('/')
        url = self.url(f'{base}/syncnetworkmodule')
        return self.conn.put(url=url, data=data, params=params)
