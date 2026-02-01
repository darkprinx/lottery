from auditlog.registry import auditlog
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from common.models.base import GenericForeignKeyModel
from common.models.comment import Comment

# Create your models here.


class PostStatus(models.TextChoices):
    DRAFT = "draft", "Draft"
    PUBLISHED = "published", "Published"


@auditlog.register()
class Post(GenericForeignKeyModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="posts"
    )
    content = models.TextField()
    status = models.CharField(
        max_length=10,
        choices=PostStatus.choices,
        default=PostStatus.DRAFT,
    )
    comments = GenericRelation(Comment, related_name="posts")

    class Meta:
        db_table = "post"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["-created_at"]),
            models.Index(fields=["slug"]),
        ]

    def __str__(self):
        return self.title
