from rest_framework import serializers

from event.models.event import Event
from event.serializers.ballot_serializer import BallotMinimalSerializer
from user.serializers.user_serializers import UserSerializer
from utils.managers.event_manager import EventManager
from utils.managers.user_manager import UserManager

"""
this file contains multiple variations of serializers for the Event model, each serving a different purpose
"""


class EventLinkedSerializer(serializers.HyperlinkedModelSerializer):
    winning_ballot = BallotMinimalSerializer()
    participants_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = (
            "id",
            "url",
            "title",
            "status",
            "ballot_price",
            "prize_money",
            "winning_ballot",
            "participants",
            "participants_count",
            "comments_count",
            "created_at",
            "updated_at",
        )

    def get_participants_count(self, obj):
        return obj.participants.count()

    def get_comments_count(self, obj):
        return obj.comments.count()


class EventWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("id", "title", "status", "ballot_price", "prize_money")


class EventReadSerializer(serializers.ModelSerializer):
    winning_ballot = BallotMinimalSerializer()
    participants = UserSerializer(many=True, read_only=True)
    participants_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = (
            "id",
            "title",
            "status",
            "ballot_price",
            "prize_money",
            "winning_ballot",
            "participants",
            "participants_count",
            "comments_count",
        )

    def get_participants_count(self, obj):
        return obj.participants.count()

    def get_comments_count(self, obj):
        return obj.comments.count()


class RegisterEventSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=True)
    lottery_event_id = serializers.IntegerField(required=True)

    user_manager = UserManager()
    lottery_event_manager = EventManager()

    def validate(self, data):
        user_id = data.get("user_id")
        lottery_event_id = data.get("lottery_event_id")

        if not self.lottery_event_manager.is_active_lottery_event(lottery_event_id):
            raise serializers.ValidationError(
                {"lottery_event_id": "Lottery event doesn't exists or is closed"}
            )

        if not self.user_manager.is_user_exists(user_id):
            raise serializers.ValidationError({"user_id": "User doesn't exist"})

        if self.lottery_event_manager.is_user_registered(user_id, lottery_event_id):
            raise serializers.ValidationError(
                {"user_id": "User is already registered to this lottery event"}
            )
        return data


class PurchaseLotteryBallotSerializer(RegisterEventSerializer):
    user_id = serializers.IntegerField(required=True)
    lottery_event_id = serializers.IntegerField(required=True)

    user_manager = UserManager()
    lottery_event_manager = EventManager()

    def validate(self, data):
        user_id = data.get("user_id")
        lottery_event_id = data.get("lottery_event_id")

        if not self.lottery_event_manager.is_active_lottery_event(lottery_event_id):
            raise serializers.ValidationError(
                {"lottery_event_id": "Lottery event doesn't exists or is closed"}
            )

        if not self.user_manager.is_user_exists(user_id):
            raise serializers.ValidationError({"user_id": "User doesn't exist"})

        if not self.lottery_event_manager.is_user_registered(user_id, lottery_event_id):
            raise serializers.ValidationError(
                {"user_id": "User not registered to the lottery event"}
            )
        return data


class LotteryWinnerSerializer(serializers.ModelSerializer):
    winning_ballot = BallotMinimalSerializer()

    class Meta:
        model = Event
        fields = ("title", "prize_money", "winning_ballot")
