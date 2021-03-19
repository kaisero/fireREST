# -*- coding: utf-8 -*-

from . import defaults


class GenericApiError(Exception):
    """Generic api error"""

    def __init__(self, msg='', *args, **kwargs):
        self.__dict__.update(kwargs)
        super().__init__(msg, *args)


class InvalidNamespaceError(Exception):
    """Invalid api namespace specified"""

    def __init__(self, msg='', *args, **kwargs):
        self.__dict__.update(kwargs)
        super().__init__(msg, *args)


class AuthError(GenericApiError):
    """Authentication failure"""


class AuthorizationError(GenericApiError):
    """Authorization failure"""


class AuthRefreshError(GenericApiError):
    """Api token refresh cannot be refreshed"""


class RateLimitException(GenericApiError):
    """API rate limiter kicked in"""


class UnsupportedOperationError(GenericApiError):
    """Unsupported operation is being performed"""

    def __init__(self, msg='', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class UnprocessableEntityError(GenericApiError):
    """Uprocessable entity passed to fmc"""

    def __init__(self, msg='', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class PayloadLimitExceededError(GenericApiError):
    """Size limit of api payload is exceeded"""

    MSG = f'Payload exceeds maximum size of {defaults.API_PAYLOAD_SIZE_MAX} bytes'

    def __init__(self, msg=MSG, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class ResourceNotFoundError(GenericApiError):
    """Requested resource cannot not be found"""


class ResourceAlreadyExistsError(GenericApiError):
    """Create operation failed because a resource with the same name already exists"""


class DomainNotFoundError(GenericApiError):
    """FMC domain could not be found"""
