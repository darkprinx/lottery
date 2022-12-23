from django.contrib.auth.models import User


class UserManager:
    def __init__(self, request=None):
        self.request = request

    def is_user_exists(self, user_id):
        return User.objects.filter(pk=user_id).exists()
