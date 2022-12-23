from django.urls import path
from lottery_events.views.lottery_event_views import PingView, RegisterLotteryView, PurchaseLotteryBallotView
from rest_framework import routers
from lottery_events.views.lottery_event_views import LotteryEventView

lottery_router = routers.DefaultRouter()
lottery_router.register('', LotteryEventView)


urlpatterns = [
    path('ping/', PingView.as_view(), name='ping'),
    path('<int:pk>/register/', RegisterLotteryView.as_view(), name='register-lottery'),
    path('purchase-ballot/', PurchaseLotteryBallotView.as_view(), name='purchase-lottery-ballot'),
] + lottery_router.urls
