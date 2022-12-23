from rest_framework import serializers

from common.managers.lottery_event_manager import LotteryEventManager
from lottery_events.models.lottery_event import LotteryEvent
from common.managers.user_manager import UserManager
from lottery_events.serializers.ballot_serializer import BallotMinimalSerializer
from user.serializers.user_serializers import UserSerializer


class LotteryEventWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = LotteryEvent
        fields = ('id', 'title', 'status', 'ballot_price', 'prize_money')


class LotteryEventReadSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True)
    winning_ballot = BallotMinimalSerializer()

    class Meta:
        model = LotteryEvent
        fields = '__all__'


class RegisterLotteryEventSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=True)
    user_manager = UserManager()

    def validate(self, data):
        user_id = data.get('user_id')
        if not self.user_manager.is_user_exists(user_id):
            raise serializers.ValidationError({"user_id": "User doesn't exist"})
        return data


class PurchaseLotteryBallotSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=True)
    lottery_event_id = serializers.IntegerField(required=True)

    user_manager = UserManager()
    lottery_event_manager = LotteryEventManager()

    def validate(self, data):
        user_id = data.get('user_id')
        lottery_event_id = data.get('lottery_event_id')

        if not self.lottery_event_manager.is_active_lottery_event(lottery_event_id):
            raise serializers.ValidationError({"lottery_event_id": "Lottery event doesn't exists or is closed"})

        if not self.user_manager.is_user_exists(user_id):
            raise serializers.ValidationError({"user_id": "User doesn't exist"})

        if not self.lottery_event_manager.is_user_registered(user_id, lottery_event_id):
            raise serializers.ValidationError({"user_id": "User not registered to the lottery event"})
        return data


class LotteryWinnerSerializer(serializers.ModelSerializer):
    winning_ballot = BallotMinimalSerializer()

    class Meta:
        model = LotteryEvent
        fields = ('title', 'prize_money', 'winning_ballot')