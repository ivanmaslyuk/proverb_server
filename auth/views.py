from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView


class CheckCredentialsView(APIView):
    authentication_classes = []

    def get(self, request):
        username = request.headers.get('X-Username')
        if not username:
            return Response({'valid': False}, 403)

        if User.objects.filter(username=username).exists():
            return Response({'valid': True})
        else:
            return Response({'valid': False}, 403)
