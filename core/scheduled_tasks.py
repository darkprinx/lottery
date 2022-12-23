from common.helpers.email_helper import AWSEmailService
from common.managers.lottery_event_manager import LotteryEventManager
from common.managers.ballot_manager import BallotManager
from common.helpers.ballot_selector_algorithm_helper import NaiveBallotSelectorStrategy
from lottery_event.models import LotteryEventStatus
from lottery_event.serializers.ballot_serializer import BallotMinimalSerializer


def close_active_lottery():
    lottery_event_manager = LotteryEventManager()
    ballot_manager = BallotManager()
    ballot_selector = NaiveBallotSelectorStrategy()
    email_helper = AWSEmailService()

    active_lottery_events = lottery_event_manager.get_active_lottery_events()

    for lottery_event in active_lottery_events:
        winning_ballot_id = ballot_selector.select(lottery_event.id)

        if winning_ballot_id:
            ballot = ballot_manager.get_ballot_by_id(winning_ballot_id)
            serialized_ballot = BallotMinimalSerializer(ballot).data
            lottery_event.winning_ballot = ballot
            lottery_event.status = LotteryEventStatus.CLOSED
            lottery_event.save()

            # todo: make email template folder
            email_body = f"Congrats! you have won a lottery! Details are shared bellow:\n" \
                         f"Lottery Event Title: {lottery_event.title}\n" \
                         f"Ballot Number: {ballot.ballot_number}\n"\
                         f"Prize Money: {lottery_event.prize_money}"

            email_helper.send_email(user_info=serialized_ballot['owner'], email_body=email_body)

