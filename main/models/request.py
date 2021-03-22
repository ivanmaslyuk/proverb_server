import uuid

from django.db import models


class Request(models.Model):
    JSON = 'application/json'
    HTML = 'text/html'
    TEXT = 'text/plain'
    URLENCODED = 'application/x-www-form-urlencoded'

    CONTENT_TYPE_CHOICES = (
        (JSON, 'JSON'),
        (HTML, 'HTML'),
        (TEXT, 'Text'),
        (URLENCODED, 'Urlencoded'),
    )

    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    node = models.OneToOneField('main.Node', on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    url = models.CharField(max_length=1000, null=True, blank=True)
    method = models.CharField(max_length=100, default="GET")
    raw_data = models.TextField(null=True, blank=True)
    content_type = models.CharField(
        max_length=500,
        choices=CONTENT_TYPE_CHOICES,
        null=True,
        blank=True
    )
    documentation = models.TextField(null=True, blank=True)
    query_params = models.TextField(null=True, blank=True)
    data_params = models.TextField(null=True, blank=True)
    headers = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name
