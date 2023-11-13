from django.conf import settings

class HttpPostTunnelingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'POST':
            if '_method' in request.POST:
                http_method = request.POST['_method']

                if http_method.lower() == 'put':
                    request.method = 'PUT'
                    request.META['REQUEST_METHOD'] = 'PUT'
                    request.PUT = request.POST
                elif http_method.lower() == 'delete':
                    request.method = 'DELETE'
                    request.META['REQUEST_METHOD'] = 'DELETE'
                    request.DELETE = request.POST
                request.META[settings.CSRF_HEADER_NAME] = request.POST['csrfmiddlewaretoken']

        response = self.get_response(request)
        return response
