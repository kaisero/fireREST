import sys


from http.client import responses as http_responses
from functools import lru_cache, wraps
from logging import getLogger
from requests import HTTPError
from retry import retry
from packaging import version
from time import sleep
from uuid import UUID, uuid4

from . import exceptions as exc
from .mapping import OBJECT_TYPE

logger = getLogger(__name__)


def is_uuid(val: str):
    '''
    verify if a value is valid uuid
    : param val: unique identifier in string format
    : return: True if valid uuid, False if invalid uuid
    '''
    try:
        UUID(val)
        return True
    except ValueError:
        return False


def is_getbyid_operation(url: str):
    '''
    verify if a api call is to a specific resource or a list of resources
    : param url: request in str format
    : return: True if resource is queried, False if multiple resources are being queried
    '''
    uuid = url.split('?')[0].split('/')[-1]
    if is_uuid(uuid):
        return True
    return False


def cache_result(f):
    '''
    decorator that applies functools lru_cache if cache is enabled in Client object
    '''

    def enabled(*args, **kwargs):
        return args[0].cache

    if enabled:

        @wraps(f)
        @lru_cache(maxsize=256)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)

        return wrapper
    return f


def log_request(action):
    '''
    decorator that adds additional debug logging for api requests
    '''

    def inner_function(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            logger = args[0].logger
            request = args[1]
            request_id = str(uuid4())[:8]
            try:
                data = args[3]
            except IndexError:
                data = None
            logger.debug('[%s] [%s] %s', request_id, action, request)
            if data:
                logger.debug('[%s] [Data] %s', request_id, data)
            result = f(*args)
            status_code = result.status_code
            status_code_name = http_responses[status_code]
            logger.debug('[%s] [Response] %s (%s)', request_id, status_code_name, status_code)
            if status_code >= 299:
                logger.debug('[%s] [Message] %s', request_id, result.content)
            return result

        return wrapper

    return inner_function


def minimum_version_required(minimum_version):
    '''
    decorator that specifies the minimal required software version to use the operation
    '''
    minimum_version = version.parse(minimum_version)

    def inner_function(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                installed_version = args[0].version
            except AttributeError:
                return f(*args, **kwargs)
            if installed_version < minimum_version:
                raise exc.UnsupportedOperationError(
                    f'{f.__name__} requires fmc software version {minimum_version}. Installed version: {installed_version}',
                )
            return f(*args, **kwargs)

        return wrapper

    return inner_function


def validate_object_type(f):
    '''
    decorator that validates object type and transforms input if neccessary
    '''

    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            object_type = kwargs.get('object_type', None)
            if object_type:
                kwargs['object_type'] = OBJECT_TYPE[object_type]
            else:
                args = list(args)
                object_type = args[1]
                args[1] = OBJECT_TYPE[object_type]
        except KeyError:
            if object_type in OBJECT_TYPE.values():
                return f(*args, **kwargs)
            raise exc.UnsupportedObjectTypeError(f'{object_type} is not a valid object type')
        return f(*args, **kwargs)

    return wrapper


@retry(exceptions=exc.RateLimitException, tries=6, delay=10, logger=logger)
def handle_errors(f):
    ''' decorator that handles common api errors automatically '''

    @wraps(f)
    def wrapper(*args, **kwargs):
        client = args[0]
        try:
            validate_data(kwargs.get('method', args[1]), kwargs.get('data', args[-1]))
            response = f(*args, **kwargs)
            response.raise_for_status()
        except HTTPError:
            if response.status_code == 401:
                # Invalid access token detected. Refresh authorization token
                client._refresh()
            else:
                raise_for_status(response)
        return response

    return wrapper


def validate_data(method, data):
    '''
    validate payload that will be sent to fmc for errors
    '''
    if method != 'get':
        if sys.getsizeof(data) > 2048000:
            raise exc.PayloadLimitExceededError


def raise_for_status(response):
    '''
    raise exception based on error received by fmc
    '''
    status_code = response.status_code
    exceptions = {
        422: exc.UnprocessableEntityError,
        429: exc.RateLimitException,
        500: exc.GenericApiError,
    }
    errors = {500: [{'msg': 'Unauthorized', 'exception': exc.AuthError}]}
    if status_code in errors:
        for error in errors[status_code]:
            if error['msg'] in response.text:
                raise error['exception']
    raise exceptions.get(status_code, HTTPError)
