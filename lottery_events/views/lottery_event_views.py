import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, generics
from common.managers.lottery_event_manager import LotteryEventManager
from lottery_events.models import LotteryEvent
from lottery_events.serializers.lottery_event_serializers import LotteryEventReadSerializer, \
    LotteryEventWriteSerializer, RegisterLotteryEventSerializer


logger = logging.getLogger(__name__)


class PingView(APIView):

    def get(self, request):
        content = {'message': 'Pong!'}
        return Response(content)

    def post(self, request):
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
    lottery_manager = LotteryEventManager()

    def post(self, request, pk):
        participant_serializer = self.serializer_class(data=request.data)
        participant_serializer.is_valid(raise_exception=True)
        user_id = participant_serializer.data['user_id']

        lottery_object = self.get_object()
        if lottery_object.participants.filter(id=user_id).exists():
            return Response(data={'msg': "User already registered"}, status=200)

        lottery_object.participants.add(user_id)
        return Response(data={'msg': "Successfully registered"}, status=201)
