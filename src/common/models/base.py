from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class GenericForeignKeyModel(TimestampedModel):
    """
    An abstract base class model that provides a generic foreign key to any other model.

    This model uses Django's Generic Foreign Key pattern to create flexible relationships
    that can point to instances of any model, rather than being tied to a specific model.

    Fields:
        content_type (ForeignKey): References the ContentType of the related model
        object_id (PositiveIntegerField): Stores the primary key of the related object
        content_object (GenericForeignKey): Virtual field that combines content_type and
            object_id to provide direct access to the related object

    Usage:
        class Comment(GenericForeignKeyModel):
            text = models.TextField()

        # Can attach to any model instance:
        comment.content_object = blog_post
        comment.content_object = photo
        comment.content_object = video

    Note:
        - This is an abstract model and should be subclassed
        - No database-level foreign key constraints are enforced
        - Inherits timestamp fields (created_at, updated_at) from TimestampedModel
    """

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    class Meta:
        abstract = True
