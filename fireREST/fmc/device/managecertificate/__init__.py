from fireREST.defaults import API_RELEASE_770
from fireREST.fmc import Resource


class ManageCertificate(Resource):
    """Perform a certificate enrollment operation on devices. Possible action values are `ENROLL`, `REENROLL`, `REFRESH`, `DELETE`, and `EXPORT`. All actions require a `deviceCertificates` section containing a deviceID and `certificates` subsection. `EXPORT` also requires a `exportOptions` subsection containing isPemFormat which can be either true or false and a passPhrase. There can be multiple deviceCertificates sections, but each section may only have one deviceId and one certificate per deviceID. You cannot use multiple actions in the same POST operation. `ENROLL` pushes a certificate file onto a device. `REENROLL` perform an `ENROLL` but cleans up any failed previous enrollment. `REFRESH` gets the devices current certificate enrollment status. `DELETE` deletes a specific certificate enrollment and the certificate information from the device. `EXPORT` requests a copy of an existing certificate from the device.

    **Tags:** Devices

    **Supported operations:** CREATE

    **Operation IDs:**

    - `createManageDeviceCertificatesRequestModel` (CREATE)
    """

    PATH = '/devices/operational/managecertificates'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_770
    MINIMUM_VERSION_REQUIRED_GET = '99.99.99'
    MINIMUM_VERSION_REQUIRED_UPDATE = '99.99.99'
    MINIMUM_VERSION_REQUIRED_DELETE = '99.99.99'
