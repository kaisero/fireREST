from typing import Dict, List, Optional, Union

from fireREST import utils
from fireREST.defaults import API_RELEASE_710
from fireREST.fmc import Resource


class Host(Resource):
    NAMESPACE = 'netmap'
    PATH = '/hosts/{uuid}'
    SUPPORTED_FILTERS = ['ip_address']
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_710

    @utils.support_params
    def get(self, uuid: Optional[str] = None, ip_address: Optional[str] = None, params: Optional[Dict] = None):
        return super().get(uuid=uuid, params=params)

    @utils.support_params
    def delete(
        self,
        uuid: Optional[str] = None,
        ip_address: Optional[Union[str, List]] = None,
        params: Optional[Dict] = None,
    ):
        if ip_address:
            if params is None:
                params = {}
            params['bulk'] = True
        url = self.url(self.PATH.format(uuid=uuid))
        return super().delete(url=url, uuid=uuid, params=params)
