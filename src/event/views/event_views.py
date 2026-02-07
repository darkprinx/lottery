import logging

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db.models import Count, OuterRef, Subquery
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from common.models.comment import Comment

# from core.scheduled_tasks import close_active_lottery
from event.models import Event
from event.serializers.event_serializers import (
    EventLinkedSerializer,
    EventReadSerializer,
    EventWriteSerializer,
    LotteryWinnerSerializer,
    PurchaseLotteryBallotSerializer,
    RegisterEventSerializer,
)
from user.serializers.user_serializers import UserSerializer
from utils.helpers.random_number_generator_helper import generate_customized_uuid
from utils.managers.ballot_manager import BallotManager
from utils.managers.event_manager import EventManager
from utils.managers.user_manager import UserManager

logger = logging.getLogger(__name__)


class CloseLotteryView(APIView):
    """
    ## Close any currently active lottery and
    ## select a winner for it.
    """

    def get(self, request):
        # close_active_lottery()
        return Response(status=200)


class EventView(viewsets.ModelViewSet):
    """
    ## CRUD endpoints for Lottery Events:
    ## list, create, update, and delete.
    """

    queryset = Event.objects.all()
    serializer_class = EventLinkedSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        qs = super().get_queryset()
        # option 1
        # qs = qs.prefetch_related("participants", "comments")
        # qs = qs.annotate(
        #     participant_count_from_qs=Count("participants", distinct=True),
        #     all_comment_count_from_qs=Count("comments", distinct=True),
        # )

        """
        option 2:
        The concept is explained how it's working.
        1. For participant_count_from_qs:
           - We filter the User model to find users who are participants of the event (using events=OuterRef("pk")).
           - The values "events" is used to group the results by event, and then we annotate the count of events for each user.
           - Finally, we select the count value to get the total number of participants for each event.
        2. For all_comment_count_from_qs:
            - We filter the Comment model to find comments related to the event (using object_id=OuterRef("pk") and content_type for Event).
            - The values "object_id" is used to group the results by event, and then we annotate the count of comments for each event.
        """
        User = get_user_model()
        qs = qs.prefetch_related("participants", "comments").annotate(
            participant_count_from_qs=Subquery(
                User.objects.filter(events=OuterRef("pk"))
                .values("events")
                .annotate(count=Count("events"))
                .values("count")
            ),
            all_comment_count_from_qs=Subquery(
                Comment.objects.filter(
                    object_id=OuterRef("pk"),
                    content_type=ContentType.objects.get_for_model(Event),
                )
                .values("object_id")
                .annotate(count=Count("object_id"))
                .values("count")
            ),
            first_comment=Subquery(
                Comment.objects.filter(
                    object_id=OuterRef("pk"),
                    content_type=ContentType.objects.get_for_model(Event),
                )
                .order_by("created_at")
                .values("content")[:1]
            ),
        )

        return qs

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return EventWriteSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAdminUser()]
        return []

    # custom APIs
    # todo: add one view with bulk create from csv file, only for admin users with parser classes

    # export event data file, only for admin users
    @action(
        detail=False,
        methods=["get"],
        url_path="export-csv",
        serializer_class=EventReadSerializer,
        permission_classes=[IsAdminUser],
    )
    def export_csv(self, request, pk=None):
        events = self.get_queryset()
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)


class RegisterLotteryView(generics.CreateAPIView):
    serializer_class = RegisterEventSerializer
    lottery_event_manager = EventManager()

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
    lottery_event_manger = EventManager()

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
