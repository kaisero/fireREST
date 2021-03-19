from fireREST.fmc import Resource


class Ikev2IpsecProposal(Resource):
    PATH = '/object/ikev2ipsecproposals/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = '6.3.0'
    MINIMUM_VERSION_REQUIRED_GET = '6.3.0'
    MINIMUM_VERSION_REQUIRED_UPDATE = '6.3.0'
    MINIMUM_VERSION_REQUIRED_DELETE = '6.3.0'
