import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, generics

from utils.helpers.circuit_breaker_dummy_apis import send_message
from utils.helpers.random_number_generator_helper import generate_customized_uuid
from utils.managers.ballot_manager import BallotManager
from utils.managers.lottery_event_manager import LotteryEventManager
from utils.managers.user_manager import UserManager
from core.scheduled_tasks import close_active_lottery
from lottery_event.models import LotteryEvent
from lottery_event.serializers.lottery_event_serializers import (
    LotteryEventReadSerializer,
    LotteryEventWriteSerializer,
    RegisterLotteryEventSerializer,
    PurchaseLotteryBallotSerializer,
    LotteryWinnerSerializer,
)
from user.serializers.user_serializers import UserSerializer

logger = logging.getLogger(__name__)


class PingView(APIView):
    """
    ## This checks application health with a ping
    ## and returns a response with pong.
    """

    def get(self, request):
        content = {"message": "Pong!", "data": send_message()}
        return Response(content)


class CloseLotteryView(APIView):
    """
    ## Close any currently active lottery and
    ## select a winner for it.
    """

    def get(self, request):
        close_active_lottery()
        return Response(status=200)


class LotteryEventView(viewsets.ModelViewSet):
    """
    ## CRUD endpoints for Lottery Events:
    ## list, create, update, and delete.
    """

    queryset = LotteryEvent.objects.all()
    serializer_class = LotteryEventReadSerializer

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return LotteryEventWriteSerializer
        return self.serializer_class


class RegisterLotteryView(generics.CreateAPIView):
    serializer_class = RegisterLotteryEventSerializer
    lottery_event_manager = LotteryEventManager()

    def post(self, request):
        """
        ## user can register to a lottery event via this endpoint.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_id = serializer.data["user_id"]
        lottery_event_id = serializer.data["lottery_event_id"]

        lottery_object = self.lottery_event_manager.get_lottery_event_by_id(
            lottery_event_id
        )
        lottery_object.participants.add(user_id)
        return Response(data={"msg": "Successfully registered"}, status=200)


class PurchaseLotteryBallotView(generics.CreateAPIView):
    serializer_class = PurchaseLotteryBallotSerializer
    ballot_manager = BallotManager()

    def post(self, request):
        """
        ## Purchase a ballot for a particular lottery event.
        ## First, call api/payments/make-payment to ensure payment succeeds.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        ballot_data = {
            "ballot_number": generate_customized_uuid(
                str(serializer.data["lottery_event_id"])
            ),
            "owner": serializer.data["user_id"],
        }
        ballot = self.ballot_manager.create_ballot(ballot_data)
        return Response(data=ballot, status=200)


class LotteryWinnerView(generics.ListAPIView):
    serializer_class = LotteryWinnerSerializer
    lottery_event_manger = LotteryEventManager()

    def get(self, request):
        """
        ## View the winning ballot and winner for a lottery event on a
        ## particular date.
        """
        search_date = request.GET.get("search_date")
        winners = self.lottery_event_manger.get_lottery_winner_by_date(search_date)
        serialized_data = self.serializer_class(winners, many=True)
        return Response(data=serialized_data.data, status=200)


class LotteryParticipantView(APIView):
    user_manager = UserManager()

    def get(self, request, pk):
        """
        ## View the participants list of a particular lottery event.
        """
        participants = self.user_manager.get_participants_of_lottery_event(
            lottery_event_id=pk
        )
        return Response(UserSerializer(participants, many=True).data)
