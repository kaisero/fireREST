# -*- coding: utf-8 -*-

from http.client import responses as http_responses
from functools import lru_cache, wraps
from packaging import version
from uuid import uuid4

from .exceptions import UnsupportedOperationError, UnsupportedObjectTypeError
from .mapping import OBJECT_TYPE


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
                raise UnsupportedOperationError(
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
            raise UnsupportedObjectTypeError(f'{object_type} is not a valid object type')
        return f(*args, **kwargs)

    return wrapper
