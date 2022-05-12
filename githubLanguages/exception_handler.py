from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):

    handlers = {
        'ValidationError': handle_validation_error,
        'Http404': handle_http_404,
        'PermissionDenied': handle_permission_denied,
        'MethodNotAllowed': handle_permission_denied,
        'NotAuthenticated': handle_auth_error,
        'InvalidToken': handle_auth_error,
        'AuthenticationFailed': handle_auth_error,
    }

    response = exception_handler(exc, context)

    exception_class = exc.__class__.__name__

    print(exception_class)
    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)

    return response


def handle_permission_denied(exc, context, response):
    response.data = {
        "message": f"{exc}"
    }

    return response


def handle_auth_error(exc, context, response):
    response.data = {
        'message': "يرجي تسجيل الدخول مرة اخري"
    }

    return response


def handle_validation_error(exc, context, response):
    message_error = ""

    try:
        for key, value in response.data.items():
            if key == "non_field_errors":
                message_error = value[0]
            else:
                message_error = key + " " + value[0]
    except:
        message_error = response.data

    response.data = {
        'message': message_error
    }

    return response


def handle_http_404(exc, context, response):
    response.data = {
        "message": f"{exc}"
    }

    return response


def handle_generic_error(exc, context, response):
    return response
