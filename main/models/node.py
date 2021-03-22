import uuid

from django.db import models


class Node(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    is_folder = models.BooleanField()
    folder_name = models.CharField(null=True, blank=True, max_length=500)

    def __str__(self) -> str:
        return self.folder_name if self.is_folder else str(self.uuid)
