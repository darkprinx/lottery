from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Ballot(models.Model):
    bought_at = models.DateTimeField(auto_now_add=True)
    ballot_number = models.CharField(max_length=128)
    owner = models.ForeignKey(
        User, related_name="purchased_ballots", on_delete=models.CASCADE
    )

    class Meta:
        managed = True
        db_table = "ballot"

    def __str__(self):
        return f"Ballot {self.ballot_number} owned by {self.owner.username}"
