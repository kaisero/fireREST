from fireREST.fmc import Resource


class AuditRecord(Resource):
    PATH = '/audit/auditrecords/{uuid}'
    IGNORE_FOR_UPDATE = []
    MINIMUM_VERSION_REQUIRED_GET = '6.1.0'
