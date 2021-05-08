import json
from pprint import pprint

from django.conf import settings
from rest_framework.response import Response


class VerboseRequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request_body = request.body

        if '/admin/' not in request.path and settings.DEBUG:
            print('\n<Request>', request.path, request.method, '-' * 100)
            pprint(json.loads(request_body) if request_body else 'No body.')

        response = self.get_response(request)

        if '/admin/' not in request.path and settings.DEBUG:
            print(f'\n\nResponse: {response.status_code} {response.headers["Content-Type"]}', '-' * 80)
            if type(response) == Response:
                pprint(response.data)
            print('</Request>', '-' * 100, '\n')

        return response
