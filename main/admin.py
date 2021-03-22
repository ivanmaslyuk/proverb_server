from django.contrib import admin

from .models import Request, Node


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = 'uuid', 'is_folder', 'folder_name'
    raw_id_fields = 'parent',


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = 'uuid', 'name', 'method'
    raw_id_fields = 'node',
