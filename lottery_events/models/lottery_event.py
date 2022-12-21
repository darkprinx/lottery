from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class LotteryEvent(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    title = models.CharField(max_length=64)
    status = models.CharField(max_length=32, choices=(('active', 'active'), ('closed', 'closed')), default='active')
    ballot_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    prize_money = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    participants = models.ManyToManyField(User, related_name='registered_lotteries', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lottery_event'
