from utils.email_templates.lottery_templates import LotteryEmailTemplate
from utils.helpers.email_helper import AWSEmailService
from utils.managers.lottery_event_manager import LotteryEventManager
from utils.managers.ballot_manager import BallotManager
from utils.helpers.ballot_selector_algorithm_helper import NaiveBallotSelectorStrategy
from lottery_event.models import LotteryEventStatus
from lottery_event.serializers.ballot_serializer import BallotMinimalSerializer
import logging

logger = logging.getLogger(__name__)


def close_active_lottery():
    try:
        lottery_event_manager = LotteryEventManager()
        ballot_manager = BallotManager()
        ballot_selector = NaiveBallotSelectorStrategy()
        email_helper = AWSEmailService()

        active_lottery_events = lottery_event_manager.get_active_lottery_events()

        for lottery_event in active_lottery_events:
            winning_ballot_id = ballot_selector.select(lottery_event.id)

            try:
                if winning_ballot_id:
                    ballot = ballot_manager.get_ballot_by_id(winning_ballot_id)
                    serialized_ballot = BallotMinimalSerializer(ballot).data
                    lottery_event.winning_ballot = ballot

                    email_body = LotteryEmailTemplate().lottery_win_template_1(
                        lottery_event, ballot
                    )
                    email_helper.send_email(
                        user_info=serialized_ballot["owner"], email_body=email_body
                    )

                lottery_event.status = LotteryEventStatus.CLOSED
                lottery_event.save()
            except Exception as error:
                logger.error(str(error), exc_info=True)
    except Exception as error:
        logger.error(str(error), exc_info=True)
