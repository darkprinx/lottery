from django.urls import path
from rest_framework import routers

from event.views.event_views import (
    CloseLotteryView,
    EventView,
    LotteryParticipantView,
    LotteryWinnerView,
    PurchaseLotteryBallotView,
    RegisterLotteryView,
)

# Routers
router = routers.DefaultRouter()
router.register("", EventView)


urlpatterns = [
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

urlpatterns += router.urls
