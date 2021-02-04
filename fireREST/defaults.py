from .version import __version__

#: protocol used to connect to api
API_PROTOCOL = 'https'

#: user agent sent to fmc
API_USER_AGENT = f'FireREST/{__version__}'

#: url used to generate token for api authorization
API_AUTH_URL = '/api/fmc_platform/v1/auth/generatetoken'

#: url used to refresh existing authorization token
API_REFRESH_URL = '/api/fmc_platform/v1/auth/refreshtoken'

#: url used to access platform related api calls
API_PLATFORM_URL = '/api/fmc_platform/v1'
API_PLATFORM_NAME = 'platform'

#: url used to access configuration related api calls
API_CONFIG_URL = '/api/fmc_config/v1'
API_CONFIG_NAME = 'config'

#: url used to access threat intelligence director related api calls
API_TID_URL = '/api/fmc_tid/v1'

#: content type. as of 6.6.0 FMC only supports json
API_CONTENT_TYPE = 'application/json'

#: paging limit for get requests that contain multiple items
API_PAGING_LIMIT = 1000

#: expansion mode for get requests
API_EXPANSION_MODE = True

#: http request timeout
API_REQUEST_TIMEOUT = 120

#: name of fmc default domain for api requests
API_DEFAULT_DOMAIN = 'Global'

#: intial authorization token refresh counter
API_REFRESH_COUNTER_INIT = 0

#: max no. of authorization token refresh operations
API_REFRESH_COUNTER_MAX = 3

#: max size of api payload in bytes
API_PAYLOAD_SIZE_MAX = 2048000

# software releases
API_RELEASE_610 = '6.1.0'
API_RELEASE_620 = '6.2.0'
API_RELEASE_621 = '6.2.1'
API_RELEASE_623 = '6.2.3'
API_RELEASE_630 = '6.3.0'
API_RELEASE_640 = '6.4.0'
API_RELEASE_650 = '6.5.0'
API_RELEASE_660 = '6.6.0'
API_RELEASE_670 = '6.7.0'

# Execute PUT,POST and DELETE operations by default. Change this switch to only log and not execute requests
DRY_RUN = False
