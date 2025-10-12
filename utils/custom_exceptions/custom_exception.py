import logging

from rest_framework.views import exception_handler
from rest_framework.response import Response

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    handlers = {
        "ValidationError": _handle_generic_error,
        "Http404": _handle_generic_error,
        "PermissionDenied": _handle_generic_error,
        "AuthenticationFailed": _handle_generic_error,
        "NotAuthenticated": _handle_generic_error,
    }
    response = exception_handler(exc, context)

    logger.error(context)
    logger.error(exc, exc_info=True)

    if response is not None:
        response.data["status_code"] = response.status_code

    exception_class = exc.__class__.__name__
    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)
    return _handle_other_errors_as_500(exc, context, response)


def _handle_generic_error(exc, context, response):
    return response


def _handle_other_errors_as_500(exc, context, response):
    if not response:
        return Response(data={"error": str(exc)}, status=500)

    response.data = {
        "error": "Something went wrong",
        "status_code": response.status_code,
    }
    return response
