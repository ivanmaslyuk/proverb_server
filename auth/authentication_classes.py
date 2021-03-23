from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions


class UsernameAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        username = request.headers.get('X-Username')
        if not username:
            raise exceptions.AuthenticationFailed('Username not provided.')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user.')

        return user, None
