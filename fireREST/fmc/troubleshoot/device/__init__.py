from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class Device(Resource):
    NAMESPACE = 'troubleshoot'
    PATH = '/troubleshoot/device'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_740

    def create(self, data, params=None):
        url = self.url(self.PATH)
        return self.conn.post(url, data, params, self.IGNORE_FOR_CREATE)
