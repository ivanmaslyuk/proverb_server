from django.db import transaction
from rest_framework import serializers

from .models import Node, Request


class RequestSerializer(serializers.ModelSerializer):
    def validate_uuid(self, value):
        if self.instance and value != self.instance.uuid:
            raise serializers.ValidationError('UUID should not be changed on existing requests')

        return value

    class Meta:
        model = Request
        exclude = 'id', 'node'


class NodeSerializer(serializers.ModelSerializer):
    request = RequestSerializer(required=False)
    parent = serializers.SlugRelatedField(slug_field='uuid', queryset=Node.objects.all())

    def validate_uuid(self, value):
        if self.instance and value != self.instance.uuid:
            raise serializers.ValidationError('UUID should not be changed on existing requests')

        return value

    def validate(self, attrs):
        if 'request' in attrs and attrs['request'] and attrs['is_folder']:
            raise serializers.ValidationError('Folder nodes should have an empty request field.')

        if attrs['is_folder'] and not attrs['folder_name']:
            raise serializers.ValidationError('Folders should have a name')

        return attrs

    def create(self, validated_data):
        with transaction.atomic():
            request_data = validated_data.get('request')
            if request_data:
                del validated_data['request']

            node = Node.objects.create(**validated_data)

            if request_data:
                Request.objects.create(node=node, **request_data)

        return node

    class Meta:
        model = Node
        exclude = 'id',
