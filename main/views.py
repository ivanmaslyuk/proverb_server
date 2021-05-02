import datetime

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Node
from .serializers import NodeSerializer


class NodeViewSet(ModelViewSet):
    queryset = Node.objects.all().select_related('request', 'parent')
    serializer_class = NodeSerializer
    lookup_field = 'uuid'

    def perform_destroy(self, instance):
        instance.pointer += 1
        instance.deleted = True
        instance.save()


@api_view(['POST'])
def sync_check(request):
    incoming_data = request.data

    response = {
        'out_of_sync': False,
        'conflicts': [],  # The same version of these nodes were edited by multiple users.
        'new': [],  # These nodes exist on the server, but not on the client.
        'updated': [],  # These nodes have new versions on the server. (Updated, deleted)
        'unknown': [],  # Server doesn't know about this node.
        'outdated': [],  # The client has newer versions of these nodes.
    }
    new_nodes = Node.objects.exclude(uuid__in=incoming_data).exclude(deleted=True)
    response['new'] = NodeSerializer(new_nodes, many=True).data

    nodes = {str(n.uuid): n for n in Node.objects.filter(uuid__in=incoming_data)}
    for uuid, incoming_node in incoming_data.items():
        if uuid not in nodes:
            response['unknown'].append(uuid)
            continue

        current_node = nodes[uuid]

        if incoming_node['pointer'] != current_node.pointer:
            print('conflict', 'server', current_node.pointer, 'incoming', incoming_node['pointer'])
            response['conflicts'].append(NodeSerializer(nodes[uuid]).data)
            continue

        incoming_edited_at = datetime.datetime.fromisoformat(incoming_node['edited_at'])

        if incoming_edited_at < current_node.edited_at.replace(tzinfo=None):
            print('UPDATED', incoming_node['edited_at'], '|', incoming_edited_at, '|', current_node.edited_at)
            response['updated'].append(NodeSerializer(nodes[uuid]).data)
            continue

        if incoming_edited_at > current_node.edited_at.replace(tzinfo=None):
            print('OUTDATED', incoming_node['edited_at'], '|', incoming_edited_at, '|', current_node.edited_at)
            response['outdated'].append(uuid)
            continue

    response['out_of_sync'] = any(response.values())
    return Response(response)
