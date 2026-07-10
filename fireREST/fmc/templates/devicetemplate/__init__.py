from typing import Dict, Optional

from fireREST import utils
from fireREST.defaults import API_RELEASE_760
from fireREST.fmc import Connection, Resource
from fireREST.fmc.templates.devicetemplate.association import DeviceTemplateAssociation
from fireREST.fmc.templates.devicetemplate.defaultmodelmapping import DefaultModelMapping
from fireREST.fmc.templates.devicetemplate.modelmapping import ModelMapping
from fireREST.fmc.templates.devicetemplate.objectoverride import ObjectOverride
from fireREST.fmc.templates.devicetemplate.templateinterface import TemplateInterface
from fireREST.fmc.templates.devicetemplate.templatevariable import TemplateVariable
from fireREST.fmc.templates.devicetemplate.vpnsetting import VpnSetting


class DeviceTemplate(Resource):
    """Retrieves, creates, updates, or deletes device templates.

    **Tags:** Templates

    **Supported operations:** GET, CREATE, UPDATE, DELETE

    **Operation IDs:**

    - `getAllDeviceTemplate` (GET (list))
    - `getDeviceTemplate` (GET)
    - `createDeviceTemplate` (CREATE)
    - `updateDeviceTemplate` (UPDATE)
    - `deleteDeviceTemplate` (DELETE)
    """

    PATH = '/templates/devicetemplates/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_760
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_760

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.association = DeviceTemplateAssociation(conn)
        self.defaultmodelmapping = DefaultModelMapping(conn)
        self.modelmapping = ModelMapping(conn)
        self.objectoverride = ObjectOverride(conn)
        self.templateinterface = TemplateInterface(conn)
        self.templatevariable = TemplateVariable(conn)
        self.vpnsetting = VpnSetting(conn)

    @utils.minimum_version_required(version=API_RELEASE_760)
    @utils.resolve_by_name
    def apply(
        self,
        data: Dict,
        container_uuid: Optional[str] = None,
        container_name: Optional[str] = None,
        params: Optional[Dict] = None,
    ):
        url = self.url(f'/templates/devicetemplates/{container_uuid}/operational/apply')
        return self.conn.post(url=url, data=data, params=params)

    @utils.minimum_version_required(version=API_RELEASE_760)
    def generate(self, data: Dict, params: Optional[Dict] = None):
        url = self.url('/templates/devicetemplates/operational/generatetemplate')
        return self.conn.post(url=url, data=data, params=params)
