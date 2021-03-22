from rest_framework.viewsets import ModelViewSet

from .models import Node
from .serializers import NodeSerializer


class NodeViewSet(ModelViewSet):
    queryset = Node.objects.all().select_related('request')
    serializer_class = NodeSerializer
    lookup_field = 'uuid'
