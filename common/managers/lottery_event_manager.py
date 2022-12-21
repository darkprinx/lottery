from lottery_events.models.lottery_event import LotteryEvent


class LotteryEventManager:
    def __int__(self, request=None):
        self.request = request

    def get_object_by_pk(self, pk):
        lottery_event = LotteryEvent.objects.filter(pk=pk)
        if not lottery_event.exists():
            return []
        return lottery_event.prefetch_related('participants').first()
