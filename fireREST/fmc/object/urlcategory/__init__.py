from fireREST.defaults import API_RELEASE_610
from fireREST.fmc import Resource


class UrlCategory(Resource):
    PATH = '/object/urlcategories/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
