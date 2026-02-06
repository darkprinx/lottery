from auditlog.registry import auditlog
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models import CheckConstraint, Index, Q

from common.models.base import TimestampedModel
from common.models.comment import Comment
from event.models.ballot import Ballot

"""
Django concepts used in this file:
- Models: Defining database schema using Django's ORM.
- Fields: Various field types like CharField, DecimalField, DateField, ForeignKey,
    and ManyToManyField to represent different data types and relationships.
- Meta class: Customizing model behavior with options like db_table, indexes,
    and constraints.
- Constraints: Enforcing data integrity using CheckConstraint.
- Indexes: Improving query performance with database indexes.
- Choices: Using TextChoices for defining enumerated types for model fields.
- Generic Relations: Establishing generic relationships to other models.
- Audit Logging: Integrating audit logging to track changes to model instances.
- Inline Table: Use inline table to show comments
"""


class EventStatus(models.TextChoices):
    UPCOMING = "upcoming"
    ACTIVE = "active"
    CLOSED = "closed"


@auditlog.register()
class Event(TimestampedModel):
    title = models.CharField(max_length=64)
    status = models.CharField(
        max_length=32,
        choices=EventStatus.choices,
        default=EventStatus.ACTIVE,
    )
    ballot_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    prize_money = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    participants = models.ManyToManyField(User, related_name="participants", blank=True)
    winning_ballot = models.OneToOneField(
        Ballot,
        related_name="winning_ballot",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    comments = GenericRelation(Comment, related_name="events")

    class Meta:
        managed = True
        db_table = "event"
        ordering = ("-created_at",)
        indexes = [
            Index(fields=["created_at"]),
            Index(fields=["status"]),
        ]
        constraints = [
            CheckConstraint(
                condition=Q(ballot_price__gte=0), name="ballot_price_non_negative"
            ),
            CheckConstraint(
                condition=Q(prize_money__gte=0), name="prize_money_non_negative"
            ),
        ]

    def __str__(self):
        return f"Lottery Event {self.title}"
