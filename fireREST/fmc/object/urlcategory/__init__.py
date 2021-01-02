from fireREST.fmc import Resource


class UrlCategory(Resource):
    PATH = '/object/urlcategories/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
