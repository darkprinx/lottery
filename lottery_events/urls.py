from django.urls import path
from lottery_events.views.lottery_event_views import HelloView
from rest_framework import routers
from lottery_events.views.lottery_event_views import LotteryEventView

lottery_router = routers.DefaultRouter()
lottery_router.register('', LotteryEventView)


urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello'),
] + lottery_router.urls
