from django.apps import AppConfig


class EventsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "event"

    def ready(self):
        from event.admins import event  # noqa: F401
