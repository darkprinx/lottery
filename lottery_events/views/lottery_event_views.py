import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from lottery_events.models import LotteryEvent
from lottery_events.serializers.lottery_event_serializers import LotteryEventSerializer

logger = logging.getLogger(__name__)


class PingView(APIView):

    def get(self, request):
        content = {'message': 'Pong!'}
        return Response(content)


class LotteryEventView(viewsets.ModelViewSet):
    queryset = LotteryEvent.objects.all()
    serializer_class = LotteryEventSerializer

