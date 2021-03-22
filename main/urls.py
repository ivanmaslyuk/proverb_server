from rest_framework.routers import SimpleRouter

from .views import NodeViewSet


urlpatterns = []

router = SimpleRouter()

router.register('nodes', NodeViewSet, 'nodes')

urlpatterns += router.urls
