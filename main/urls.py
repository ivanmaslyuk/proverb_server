from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import NodeViewSet, sync_check

urlpatterns = [
    path('sync-check/', sync_check, name='sync_check'),
]

router = SimpleRouter()

router.register('nodes', NodeViewSet, 'nodes')

urlpatterns += router.urls
