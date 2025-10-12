from django.contrib.auth.models import User


class UserManager:
    def __init__(self, request=None):
        self.request = request

    def is_user_exists(self, user_id):
        return User.objects.filter(pk=user_id).exists()

    def get_participants_of_lottery_event(self, lottery_event_id):
        return User.objects.filter(registered_lotteries=lottery_event_id).all()
