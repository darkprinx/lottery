from rest_framework import serializers
from lottery_events.models.lottery_event import LotteryEvent


class LotteryEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = LotteryEvent
        fields = '__all__'
