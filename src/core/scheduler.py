from apscheduler.schedulers.background import BackgroundScheduler

from core.scheduled_tasks import close_active_lottery

"""This task will be triggered at 12.01 AM every day on UTC time"""
task_list_config = [
    {
        "func": close_active_lottery,
        "trigger": "cron",
        "hour": 0,
        "minute": 1,
        "timezone": "UTC",
    },
]


def start():
    scheduler = BackgroundScheduler()
    for task_config in task_list_config:
        scheduler.add_job(**task_config)
    scheduler.start()
