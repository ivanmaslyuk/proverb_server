import base64
import binascii

from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions


class BasicAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        authorization = request.headers.get('Authorization')
        if not authorization:
            raise exceptions.AuthenticationFailed('No credentials provided.')

        if not authorization.startswith('Basic '):
            raise exceptions.AuthenticationFailed('Wrong format in Authorization header.')

        try:
            credentials = authorization.replace('Basic ', '')
            credentials_decoded = base64.b64decode(credentials.encode('utf-8').decode('utf-8')).decode('utf-8')
        except binascii.Error:
            raise exceptions.AuthenticationFailed('Cannot decode credentials.')

        try:
            username, password = credentials_decoded.split(':')
        except ValueError:
            raise exceptions.AuthenticationFailed('Credentials format is invalid.')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('Wrong username or password.')

        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('Wrong username or password.')

        return user, None
