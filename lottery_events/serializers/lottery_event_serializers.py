from rest_framework import serializers
from lottery_events.models.lottery_event import LotteryEvent
from common.managers.user_manager import UserManager


class LotteryEventWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = LotteryEvent
        fields = ('id', 'title', 'status', 'ballot_price', 'prize_money', 'created_at')


class LotteryEventReadSerializer(serializers.ModelSerializer):
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
