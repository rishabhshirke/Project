from django.utils.timezone import now


class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f"Request at {now()}: {request.method} {request.path}")
        response = self.get_response(request)
        print(f"Response at {now()}: {response.status_code}")
        return response
