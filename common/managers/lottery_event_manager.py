from lottery_event.models.lottery_event import LotteryEvent, LotteryEventStatus


class LotteryEventManager:
    def __init__(self, request=None):
        self.request = request

    def get_lottery_event_by_id(self, lottery_event_id):
        return LotteryEvent.objects.filter(id=lottery_event_id).first()

    def is_active_lottery_event(self, lottery_event_id):
        return LotteryEvent.objects.filter(pk=lottery_event_id, status=LotteryEventStatus.ACTIVE).exists()

    def is_user_registered(self, user_id, lottery_event_id):
        return LotteryEvent.objects.filter(pk=lottery_event_id, participants=user_id).exists()

    def get_active_lottery_events(self):
        return LotteryEvent.objects.filter(status=LotteryEventStatus.ACTIVE)

    def update_lottery_event(self, filter_params, update_params):
        return LotteryEvent.objects.filter(**filter_params).update(**update_params)

    def get_lottery_winner_by_date(self, search_date):
        return LotteryEvent.objects.filter(created_at=search_date).\
            select_related('winning_ballot', 'winning_ballot__owner').filter(winning_ballot__isnull=False)
