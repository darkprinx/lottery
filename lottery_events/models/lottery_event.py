from django.db import models
from django.contrib.auth.models import User

from lottery_events.models.ballot import Ballot


# Create your models here.


class LotteryEventStatus:
    ACTIVE = 'active'
    CLOSED = 'closed'


class LotteryEvent(models.Model):
    created_at = models.DateField(auto_now=True, db_index=True)
    title = models.CharField(max_length=64)
    status = models.CharField(max_length=32, choices=(('active', 'active'), ('closed', 'closed')), default='active')
    ballot_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    prize_money = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    participants = models.ManyToManyField(User, related_name='registered_lotteries', blank=True, null=True)
    winning_ballot = models.OneToOneField(Ballot, related_name='winning_lottery', on_delete=models.SET_NULL, blank=True,
                                          null=True)

    class Meta:
        managed = True
        db_table = 'lottery_event'
