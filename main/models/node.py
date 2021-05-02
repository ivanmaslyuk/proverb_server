import uuid
from datetime import datetime

from django.db import models


class Node(models.Model):
    uuid = models.CharField(max_length=36, default=uuid.uuid4, unique=True)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    is_folder = models.BooleanField()
    folder_name = models.CharField(null=True, blank=True, max_length=500)
    deleted = models.BooleanField(default=False)
    edited_at = models.DateTimeField(default=datetime.now)
    pointer = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return self.folder_name if self.is_folder else str(self.uuid)

    def save(self, *args, **kwargs):
        self.uuid = str(uuid.UUID(self.uuid))
        super().save(*args, **kwargs)
