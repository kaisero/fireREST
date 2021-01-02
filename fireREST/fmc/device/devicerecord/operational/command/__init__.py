from fireREST import utils
from fireREST.fmc import ChildResource


class Command(ChildResource):
    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/operational/commands'

    @utils.resolve_by_name
    @utils.minimum_version_required(version='6.6.0')
    def get(self, command: str, container_uuid=None, container_name=None):
        # commands with wordsize > 2 must be split into filter and parameters params due to fmc rest api impl
        split_cmd = command.split(' ')
        filter_str = ' '.join(split_cmd[:2])
        params_str = ' '.join(split_cmd[2:])
        params = {'filter': utils.search_filter({'command': filter_str}), 'parameters': params_str}

        url = self.url(self.PATH.format(container_uuid=container_uuid))
        return self.conn.get(url=url, params=params)
