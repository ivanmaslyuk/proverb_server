from django.db import transaction
from rest_framework import serializers

from .models import Node, Request


class RequestSerializer(serializers.ModelSerializer):
    uuid = serializers.CharField(read_only=True)

    class Meta:
        model = Request
        exclude = 'id', 'node'


class NodeSerializer(serializers.ModelSerializer):
    request = RequestSerializer(allow_null=True)
    parent = serializers.SlugRelatedField(slug_field='uuid', queryset=Node.objects.all(), allow_null=True)
    accept = serializers.BooleanField(required=False)

    def validate_edited_at(self, value):
        if self.instance and self.instance.edited_at > value:
            raise serializers.ValidationError('Old version of the node received.')
        return value

    def validate_pointer(self, value):
        if not self.instance and value != 1:
            raise serializers.ValidationError('Number of pointer should be 1 on creation.')
        return value

    def validate_is_folder(self, value):
        if self.instance and self.instance.is_folder != value:
            raise serializers.ValidationError('Cannot change is_folder after the node has been created.')

        return value

    def validate(self, attrs):
        if attrs['request'] and attrs['is_folder']:
            raise serializers.ValidationError('Folder nodes should have an empty request field.')

        if attrs['request'] is None and not attrs['is_folder']:
            raise serializers.ValidationError('Request nodes should not have empty request fields')

        if attrs['is_folder'] and not attrs['folder_name']:
            raise serializers.ValidationError('Folders should have a name.')

        if self.instance and self.instance.pointer != attrs['pointer'] and attrs.get('accept', False):
            raise serializers.ValidationError('Version conflict detected. Pass accept = true to save anyway.')

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

    def update(self, instance, validated_data):
        with transaction.atomic():
            request_data = validated_data.pop('request') or {}

            for key, value in validated_data.items():
                setattr(instance, key, value)
            instance.pointer += 1
            instance.save()

            if request_data:
                for key, value in request_data.items():
                    setattr(instance.request, key, value)
                instance.request.save()

            return instance

    class Meta:
        model = Node
        exclude = 'id',
