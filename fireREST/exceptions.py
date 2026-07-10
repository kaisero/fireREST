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
    """Authorization failure — HTTP 403 or insufficient privileges"""


class AuthRefreshError(GenericApiError):
    """Api token refresh cannot be refreshed"""


class BadRequestError(GenericApiError):
    """HTTP 400 — invalid query parameters, missing fields, or invalidated policy object"""


class MethodNotAllowedError(GenericApiError):
    """HTTP 405 — HTTP method not supported on this resource"""


class RateLimitError(GenericApiError):
    """HTTP 429 — API rate limit exceeded (exact threshold varies by FMC version)"""


# Backward-compatible alias — do not remove
RateLimitException = RateLimitError


class ConcurrentRequestError(RateLimitError):
    """HTTP 429 — too many concurrent connections"""


class RateLimitWriteError(RateLimitError):
    """HTTP 429 — a parallel write operation was blocked"""


class UnsupportedOperationError(GenericApiError):
    """Unsupported operation is being performed"""

    def __init__(self, msg='', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class UnprocessableEntityError(GenericApiError):
    """HTTP 422 — unprocessable entity (invalid attribute name, malformed JSON, or unknown field)"""

    def __init__(self, msg='', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class PayloadLimitExceededError(GenericApiError):
    """HTTP 422 — payload exceeds the 2 048 000-byte API limit"""

    MSG = f'Payload exceeds maximum size of {defaults.API_PAYLOAD_SIZE_MAX} bytes'

    def __init__(self, msg=MSG, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class ServerError(GenericApiError):
    """HTTP 5xx — FMC server-side error"""


class ResourceNotFoundError(GenericApiError):
    """Requested resource cannot not be found"""


class ResourceAlreadyExistsError(GenericApiError):
    """Create operation failed because a resource with the same name already exists"""


class DomainNotFoundError(GenericApiError):
    """FMC domain could not be found"""
