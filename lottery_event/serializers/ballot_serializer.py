from rest_framework import serializers
from lottery_event.models.ballot import Ballot
from user.serializers.user_serializers import UserNameEmailSerializer


class BallotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ballot
        fields = "__all__"


class BallotMinimalSerializer(serializers.ModelSerializer):
    owner = UserNameEmailSerializer()

    class Meta:
        model = Ballot
        fields = ("ballot_number", "owner")
