from django.urls import path
from lottery_event.views.lottery_event_views import PingView, RegisterLotteryView, PurchaseLotteryBallotView, \
    LotteryWinnerView, CloseLotteryView, LotteryParticipantView
from rest_framework import routers
from lottery_event.views.lottery_event_views import LotteryEventView

lottery_router = routers.DefaultRouter()
lottery_router.register('', LotteryEventView)


urlpatterns = [
    path('ping/', PingView.as_view(), name='ping'),
    path('close-active-lotteries/', CloseLotteryView.as_view(), name='close-lottery-manually'),
    path('register/', RegisterLotteryView.as_view(), name='register-lottery'),
    path('purchase-ballot/', PurchaseLotteryBallotView.as_view(), name='purchase-lottery-ballot'),
    path('winners/', LotteryWinnerView.as_view(), name='get-lottery-winners'),
    path('<int:pk>/participants', LotteryParticipantView.as_view(), name='get-lottery-participant-list')
] + lottery_router.urls
