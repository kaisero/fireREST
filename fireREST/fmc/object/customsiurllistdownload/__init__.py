from fireREST.defaults import API_RELEASE_740
from fireREST.fmc import Resource


class CustomSiUrlListDownload(Resource):
    PATH = '/object/customsiurllistdownload/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_740
