from auditlog.registry import auditlog
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.admin import GenericTabularInline
from django.db import models

from common.models.base import GenericForeignKeyModel

User = get_user_model()


@auditlog.register()
class Comment(GenericForeignKeyModel):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author}"

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["-created_at"]),
        ]
        db_table = "comment"


class CommentInline(GenericTabularInline):
    model = Comment
    extra = 0
    readonly_fields = ("author", "content", "created_at")
    can_delete = False
    max_num = 20  # Limit items per page
    ordering = ("-created_at",)

    def has_add_permission(self, request, obj=None):
        # Disable adding comments from event admin
        return False
