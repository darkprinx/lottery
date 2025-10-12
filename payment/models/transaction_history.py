from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TransactionHistory(models.Model):
    paid_by = models.ForeignKey(
        User, related_name="transaction_history", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=16, default="pending")
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    payment_via = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)
    transaction_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = "transaction_history"
