# Register your models here.
from django.contrib import admin

from common.models.comment import CommentInline
from event.models.event import Event

"""
Django concepts used in this file:
- List Display, List Filters, Search Fields, Ordering
- Exclude Fields: Excluding specific fields from the admin form. such as Participants.
- Readonly Fields: Making certain fields read-only in the admin interface.
- Custom Display Methods: Creating custom methods to display computed data in the admin. such as Participant Count.
- Generic Inline: Using GenericTabularInline to display related objects via GenericForeignKey.
- Pagination in Inlines: Implementing pagination for inline objects using show_change_link.

"""


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "status",
        "ballot_price",
        "prize_money",
        "participant_count",
        "comments_count",
        "created_at",
    )
    list_filter = ("status",)
    search_fields = ("title",)
    ordering = ("-created_at",)
    readonly_fields = ("winning_ballot", "participant_count", "comments_count")
    inlines = [CommentInline]
    filter_horizontal = ("participants",)

    @admin.display(description="Participants")
    def participant_count(self, obj):
        return obj.participants.count()

    @admin.display(description="Comments")
    def comments_count(self, obj):
        return obj.comments.count()
