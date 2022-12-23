from lottery_events.models import Ballot
from lottery_events.serializers.ballot_serializer import BallotSerializer


class BallotManager:
    def __init__(self, request=None):
        self.request = request

    def create_ballot(self, ballot_data):
        ballot_serializer = BallotSerializer(data=ballot_data)
        ballot_serializer.is_valid(raise_exception=True)
        ballot_serializer.save()
        return ballot_serializer.data

    def get_ballot_by_id(self, ballot_id):
        return Ballot.objects.select_related('owner').filter(id=ballot_id).first()


