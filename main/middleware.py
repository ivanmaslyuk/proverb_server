import base64
import binascii

from django.contrib.auth.models import User
from django.contrib.auth import login
from django.http import HttpResponseForbidden


class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            authorization = request.headers['Authorization']
        except KeyError:
            return HttpResponseForbidden('User credentials were not provided.')

        try:
            credentials_b64 = authorization[6:].encode('utf-8')
            username = base64.b64decode(credentials_b64).decode('utf-8').split(':')[0]
        except binascii.Error:
            return HttpResponseForbidden('Error decoding authorization data.')

        try:
            user = User.objects.get(username=username)
            login(request, user)
        except User.DoesNotExist:
            return HttpResponseForbidden('User with such credentials was not found.')

        return self.get_response(request)
