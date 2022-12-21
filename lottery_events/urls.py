from django.urls import path
from lottery_events.views.lottery_event_views import PingView
from rest_framework import routers
from lottery_events.views.lottery_event_views import LotteryEventView

lottery_router = routers.DefaultRouter()
lottery_router.register('', LotteryEventView)


urlpatterns = [
    path('ping/', PingView.as_view(), name='ping'),
] + lottery_router.urls
