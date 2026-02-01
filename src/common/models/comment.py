from auditlog.registry import auditlog
from django.db import models

from common.models.base import TimestampedModel


@auditlog.register()
class Comment(TimestampedModel):
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author}"

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["-created_at"]),
        ]
        db_table = "comment"
