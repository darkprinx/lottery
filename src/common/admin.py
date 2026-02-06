# Register your models here.
from django.contrib import admin

from common.models.comment import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "created_at", "content")
    list_filter = ("created_at", "content_type")
    search_fields = ("content",)
    ordering = ("-created_at",)
    list_per_page = 25
    list_display_links = ("content",)

    fieldsets = (
        ("Author Information", {"fields": ("author",)}),
        ("Comment Content", {"fields": ("content",)}),
        (
            "Related Object",
            {
                "fields": ("content_type", "object_id"),
            },
        ),
    )
