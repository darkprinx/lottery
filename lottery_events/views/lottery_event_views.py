import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, generics

from common.helpers.random_number_generator_helper import generate_customized_uuid
from common.managers.ballot_manager import BallotManager
from core.scheduled_tasks import close_active_lottery
from lottery_events.models import LotteryEvent, LotteryEventStatus
from lottery_events.serializers.lottery_event_serializers import LotteryEventReadSerializer, \
    LotteryEventWriteSerializer, RegisterLotteryEventSerializer, PurchaseLotteryBallotSerializer

logger = logging.getLogger(__name__)


class PingView(APIView):

    def get(self, request):
        content = {'message': 'Pong!'}
        return Response(content)

    def post(self, request):
        close_active_lottery()
        return Response({})


class LotteryEventView(viewsets.ModelViewSet):
    queryset = LotteryEvent.objects.all()
    serializer_class = LotteryEventReadSerializer

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return LotteryEventWriteSerializer
        return self.serializer_class


class RegisterLotteryView(generics.CreateAPIView):
    queryset = LotteryEvent.objects.all()
    serializer_class = RegisterLotteryEventSerializer

    def post(self, request, pk):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_id = serializer.data['user_id']

        lottery_object = self.get_object()
        if lottery_object.status == LotteryEventStatus.CLOSED:
            return Response(data={'msg': "Sorry! The lottery event has been closed"}, status=400)

        if lottery_object.participants.filter(id=user_id).exists():
            return Response(data={'msg': "User already registered"}, status=400)

        lottery_object.participants.add(user_id)
        return Response(data={'msg': "Successfully registered"}, status=201)


class PurchaseLotteryBallotView(generics.CreateAPIView):
    queryset = LotteryEvent.objects.all()
    serializer_class = PurchaseLotteryBallotSerializer
    ballot_manager = BallotManager()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # make payment here
        ballot_data = {
            'ballot_number': generate_customized_uuid(str(serializer.data['lottery_event_id'])),
            'owner': serializer.data['user_id']
        }
        ballot = self.ballot_manager.create_ballot(ballot_data)
        return Response(data=ballot)
