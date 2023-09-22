# request_logger/middleware.py
from .models import RequestLog

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log request details to the database
        RequestLog.objects.create(
            ip_address=request.META.get('REMOTE_ADDR'),
            user_agent=request.META.get('HTTP_USER_AGENT'),
            request_path=request.path,
            http_method=request.method,
        )

        response = self.get_response(request)
        return response
