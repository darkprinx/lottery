from lottery_events.models.lottery_event import LotteryEvent, LotteryEventStatus


class LotteryEventManager:
    def __init__(self, request=None):
        self.request = request

    def is_active_lottery_event(self, lottery_event_id):
        return LotteryEvent.objects.filter(pk=lottery_event_id, status=LotteryEventStatus.ACTIVE).exists()

    def is_user_registered(self, user_id, lottery_event_id):
        return LotteryEvent.objects.filter(pk=lottery_event_id, participants=user_id).exists()

    def get_active_lottery_events(self):
        return LotteryEvent.objects.filter(status=LotteryEventStatus.ACTIVE)

    def update_lottery_event(self, filter_params, update_params):
        return LotteryEvent.objects.filter(**filter_params).update(**update_params)
