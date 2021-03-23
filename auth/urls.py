from django.urls import path

from .views import CheckCredentialsView

urlpatterns = [
    path('check-credentials/', CheckCredentialsView.as_view(), name='check_credentials'),
]
