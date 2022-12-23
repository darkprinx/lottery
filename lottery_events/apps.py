from django.apps import AppConfig

class LotteryEventsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lottery_events'

    def ready(self):
        from core import scheduler
        scheduler.start()
