from rest_framework import routers

from lottery_events.views.lottery_event_views import LotteryEventView

lottery_router = routers.DefaultRouter()
lottery_router.register('lottery-event', LotteryEventView)
