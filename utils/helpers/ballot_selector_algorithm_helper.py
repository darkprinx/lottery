from abc import ABC, abstractmethod

from lottery_event.models import LotteryEvent
import random


class BaseStrategy(ABC):

    @abstractmethod
    def select(self, *args, **kwargs):
        pass


class NaiveBallotSelectorStrategy(BaseStrategy):

    def select(self, lottery_event_id):
        ballots = LotteryEvent.objects.prefetch_related('participants__purchased_ballots').\
            filter(id=lottery_event_id, participants__purchased_ballots__isnull=False).\
            values_list('participants__purchased_ballots', flat=True).distinct()

        if not ballots:
            return None
        return random.choices(ballots)[0]

