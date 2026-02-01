from django.urls import path
from rest_framework import routers

from event.views.lottery_event_views import (
    CloseLotteryView,
    EventView,
    LotteryParticipantView,
    LotteryWinnerView,
    PingView,
    PurchaseLotteryBallotView,
    RegisterLotteryView,
)

lottery_router = routers.DefaultRouter()
lottery_router.register("", EventView)


urlpatterns = [
    path("ping/", PingView.as_view(), name="ping"),
    path(
        "close-active-lotteries/",
        CloseLotteryView.as_view(),
        name="close-lottery-manually",
    ),
    path("register/", RegisterLotteryView.as_view(), name="register-lottery"),
    path(
        "purchase-ballot/",
        PurchaseLotteryBallotView.as_view(),
        name="purchase-lottery-ballot",
    ),
    path("winners/", LotteryWinnerView.as_view(), name="get-lottery-winners"),
    path(
        "<int:pk>/participants",
        LotteryParticipantView.as_view(),
        name="get-lottery-participant-list",
    ),
]

urlpatterns += lottery_router.urls
